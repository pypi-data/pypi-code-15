import os
from os import path, environ
import re
from time import time
from six import string_types
from json import load, dumps
import subprocess
from collections import defaultdict

try:
    from subprocess import DEVNULL  # py3k
except ImportError:
    DEVNULL = open(os.devnull, 'r+b')


class SlurmPipelineError(Exception):
    'Base class of all SlurmPipeline exceptions'


class SchedulingError(SlurmPipelineError):
    'An error in scheduling execution'


class SpecificationError(SlurmPipelineError):
    'An error was found in a specification'


class SlurmPipeline(object):
    """
    Read a pipeline execution specification and make it possible to schedule
    it via SLURM.

    @param specification: Either a C{str} giving the name of a file containing
        a JSON execution specification, or a C{dict} holding a correctly
        formatted execution specification. Note that in the latter case the
        passed specification C{dict} will be modified by this script.
    @param force: If C{True}, step scripts will be told (via the environment
        variable SP_FORCE=1) that they may overwrite pre-existing result files.
        I.e., that --force was used on the slurm-pipeline.py command line.
    @param firstStep: If not C{None}, the name of the first specification step
          to execute. Earlier steps will actually be executed but they will
          have SP_SIMULATE=1 in their environment, allowing them to skip doing
          actual work (while still emitting task names without job numbers so
          that later steps receive the correct tasks to operate on.
    @param lastStep: If not C{None}, the name of the last specification step
          to execute. See above docs for C{firstStep} for how this affects the
          calling of step scripts.
    @param scriptArgs: A C{list} of C{str} arguments that should be put on the
        command line of all steps that have no dependencies.
    """

    # In script output, look for lines of the form
    # TASK: NAME 297483 297485 297490
    # containing a task name (with no spaces) followed by zero or more numeric
    # job ids. The following regex just matches the first part of that.
    TASK_NAME_LINE = re.compile('^TASK:\s+(\S+)\s*')

    def __init__(self, specification, force=False, firstStep=None,
                 lastStep=None, scriptArgs=None):
        if isinstance(specification, string_types):
            specification = self._loadSpecification(specification)
        # self.steps will be keyed by step name, with values that are
        # self.specification step dicts. This is for convenient / direct
        # access to steps by name. It is initialized in
        # self._checkSpecification.
        self.steps = {}
        self.firstStep = firstStep
        self.lastStep = lastStep
        self._checkSpecification(specification)
        self.specification = specification
        self._scriptArgs = scriptArgs
        self._scriptArgsStr = (
            ' '.join(map(str, scriptArgs)) if scriptArgs else '')
        environ['SP_FORCE'] = str(int(force))
        self.specification['force'] = force
        self.specification['firstStep'] = firstStep
        self.specification['lastStep'] = lastStep

    def schedule(self):
        """
        Schedule the running of our execution specification.
        """
        if 'scheduledAt' in self.specification:
            raise SchedulingError('Specification has already been scheduled')
        else:
            self.specification['scheduledAt'] = time()

            firstStepFound = lastStepFound = False

            for step in self.specification['steps']:
                if self.firstStep is not None:
                    if firstStepFound:
                        if self.lastStep is not None:
                            if lastStepFound:
                                simulate = True
                            else:
                                if step['name'] == self.lastStep:
                                    simulate = False
                                    lastStepFound = True
                                else:
                                    simulate = True
                        else:
                            simulate = False
                    else:
                        if step['name'] == self.firstStep:
                            simulate = False
                            firstStepFound = True
                        else:
                            simulate = True
                else:
                    simulate = False

                self._scheduleStep(step, simulate)

    def _scheduleStep(self, step, simulate):
        """
        Schedule a single execution step.

        @param step: A C{dict} with a job specification.
        @param simulate: If C{True}, this step should be simulated. The step
            script is still run, but with SP_SIMULATE=1 in its environment.
            Else, SP_SIMULATE=0 will be in the environment.
        """
        assert 'scheduledAt' not in step
        assert 'tasks' not in step
        step['tasks'] = defaultdict(set)

        # taskDependencies is keyed by task name. These are the tasks
        # started by the steps that the current step depends on.  Its
        # values are sets of SLURM job ids the tasks that step started and
        # which this step therefore depends on.
        step['taskDependencies'] = taskDependencies = defaultdict(set)
        for stepName in step.get('dependencies', []):
            for taskName, jobIds in self.steps[stepName]['tasks'].items():
                taskDependencies[taskName].update(jobIds)

        if taskDependencies:
            if 'collect' in step:
                # This step is a 'collector'. I.e., it is dependent on all
                # tasks from all its dependencies and cannot run until they
                # have all finished. We will only run the script once, and tell
                # it about all job ids for all tasks that are depended on.
                env = environ.copy()
                env['SP_ORIGINAL_ARGS'] = self._scriptArgsStr
                env['SP_SIMULATE'] = str(int(simulate))
                dependencies = ','.join(
                    sorted(('afterok:%d' % jobId)
                           for jobIds in taskDependencies.values()
                           for jobId in jobIds))
                if dependencies:
                    env['SP_DEPENDENCY_ARG'] = '--dependency=' + dependencies
                else:
                    env.pop('SP_DEPENDENCY_ARG', None)
                self._runStepScript(step, sorted(taskDependencies), env)
            else:
                # The script for this step gets run once for each task in the
                # steps it depends on.
                for taskName in sorted(taskDependencies):
                    env = environ.copy()
                    env['SP_ORIGINAL_ARGS'] = self._scriptArgsStr
                    env['SP_SIMULATE'] = str(int(simulate))
                    jobIds = self.steps[stepName]['tasks'][taskName]
                    dependencies = ','.join(sorted(('afterok:%d' % jobId)
                                                   for jobId in jobIds))
                    if dependencies:
                        env['SP_DEPENDENCY_ARG'] = ('--dependency=' +
                                                    dependencies)
                    else:
                        env.pop('SP_DEPENDENCY_ARG', None)
                    self._runStepScript(step, [taskName], env)
        else:
            # Either this step has no dependencies or the steps it is
            # dependent on did not start any tasks. If there are no
            # dependencies, run the script with the originally passed
            # command line arguments. If there were dependencies but no
            # tasks have been started, run with no command line arguments.
            if 'dependencies' in step or self._scriptArgs is None:
                args = []
            else:
                args = list(map(str, self._scriptArgs))
            env = environ.copy()
            env['SP_ORIGINAL_ARGS'] = self._scriptArgsStr
            env['SP_SIMULATE'] = str(int(simulate))
            env.pop('SP_DEPENDENCY_ARG', None)
            self._runStepScript(step, args, env)

        step['scheduledAt'] = time()

    def _runStepScript(self, step, args, env):
        """
        Run the script for a step, using a given environment and parse its
        output for tasks it scheduled via sbatch.

        @param step: A C{dict} with a job specification.
        @param env: A C{str} key to C{str} value environment for the script.
        @param args: A C{list} of command-line arguments.
        @raise SchedulingError: If a script outputs a task name more than once.
        """
        script = step['script']
        try:
            cwd = step['cwd']
        except KeyError:
            # No working directory was given. Run the script from our
            # current directory.
            cwd = '.'
        else:
            # A working directory was given, so make sure we have an
            # absolute path to the script so we can run it from that
            # directory.
            if not path.isabs(script):
                script = path.abspath(script)

        step['stdout'] = subprocess.check_output(
            [script] + args, cwd=cwd, env=env, stdin=DEVNULL,
            universal_newlines=True)

        # Look at all output lines for task names and SLURM job ids created
        # (if any) by this script. Ignore any non-matching output.
        tasks = step['tasks']
        for line in step['stdout'].split('\n'):
            match = self.TASK_NAME_LINE.match(line)
            if match:
                taskName = match.group(1)
                # The job ids follow the 'TASK:' string and the task name.
                # They should not contain duplicates.
                jobIds = list(map(int, line.split()[2:]))
                if len(jobIds) != len(set(jobIds)):
                    raise SchedulingError(
                        'Task name %r was output with a duplicate in its job '
                        'ids %r by %r script in step named %r' %
                        (taskName, jobIds, script, step['name']))
                tasks[taskName].update(jobIds)

    def _loadSpecification(self, specificationFile):
        """
        Load a JSON execution specification.

        @param specificationFile: A C{str} file name containing a JSON
            execution specification.
        @raise ValueError: Will be raised (by L{json.load}) if
            C{specificationFile} does not contain valid JSON.
        @return: The parsed JSON specification as a C{dict}.
        """
        with open(specificationFile) as fp:
            return load(fp)

    def _checkSpecification(self, specification):
        """
        Check an execution specification is syntactically as expected.

        @param specification: A C{dict} containing an execution specification.
        @raise SpecificationError: if there is anything wrong with the
            specification.
        """
        if not isinstance(specification, dict):
            raise SpecificationError('The specification must be a dict (i.e., '
                                     'a JSON object when loaded from a file)')

        if 'steps' not in specification:
            raise SpecificationError(
                'The specification must have a top-level "steps" key')

        if not isinstance(specification['steps'], list):
            raise SpecificationError('The "steps" key must be a list')

        firstStepFound = lastStepFound = False

        for count, step in enumerate(specification['steps'], start=1):
            if not isinstance(step, dict):
                raise SpecificationError('Step %d is not a dictionary' % count)

            if 'script' not in step:
                raise SpecificationError(
                    'Step %d does not have a "script" key' % count)

            if not isinstance(step['script'], string_types):
                raise SpecificationError(
                    'The "script" key in step %d is not a string' % count)

            if not path.exists(step['script']):
                raise SpecificationError(
                    'The script %r in step %d does not exist' %
                    (step['script'], count))

            if not os.access(step['script'], os.X_OK):
                raise SpecificationError(
                    'The script %r in step %d is not executable' %
                    (step['script'], count))

            if 'name' not in step:
                raise SpecificationError(
                    'Step %d does not have a "name" key' % count)

            if not isinstance(step['name'], string_types):
                raise SpecificationError(
                    'The "name" key in step %d is not a string' % count)

            if step['name'] in self.steps:
                raise SpecificationError(
                    'The name %r of step %d was already used in '
                    'an earlier step' % (step['name'], count))

            self.steps[step['name']] = step

            if step['name'] == self.firstStep:
                firstStepFound = True

            if step['name'] == self.lastStep:
                if self.firstStep is not None and not firstStepFound:
                    raise SpecificationError(
                        'The lastStep %r occurs before the firstStep %r in '
                        'the specification' % (self.lastStep, self.firstStep))
                lastStepFound = True

            if 'dependencies' in step:
                dependencies = step['dependencies']
                if not isinstance(dependencies, list):
                    raise SpecificationError(
                        'Step %d has a non-list "dependencies" key' % count)

                # All named dependencies must already have been specified.
                for dependency in dependencies:
                    if dependency not in self.steps:
                        raise SpecificationError(
                            'Step %d depends on a non-existent (or '
                            'not-yet-defined) step: %r' % (count, dependency))

        if self.firstStep is not None and not firstStepFound:
            raise SpecificationError(
                'The firstStep %r was not found in the specification' %
                self.firstStep)

        if self.lastStep is not None and not lastStepFound:
            raise SpecificationError(
                'The lastStep %r was not found in the specification' %
                self.lastStep)

    def toJSON(self):
        """
        Return the specification as a JSON string.

        @return: A C{str} giving the specification in JSON form.
        """
        copy = self.specification.copy()
        for step in copy['steps']:
            for taskName, jobIds in step['tasks'].items():
                step['tasks'][taskName] = list(sorted(jobIds))
            for taskName, jobIds in step['taskDependencies'].items():
                step['taskDependencies'][taskName] = list(sorted(jobIds))
        return dumps(copy, sort_keys=True, indent=2, separators=(',', ': '))
