# This file is part of jenkins-epo
#
# jenkins-epo is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or any later version.
#
# jenkins-epo is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# jenkins-epo.  If not, see <http://www.gnu.org/licenses/>.

from copy import deepcopy
import inspect
import logging
import pkg_resources
import random
import socket

from jenkins_yml.job import Job as JobSpec

from ..bot import Extension, Error
from ..github import GITHUB, ApiError, ApiNotFoundError
from ..repository import Branch, CommitStatus
from ..settings import SETTINGS
from ..utils import deepupdate, match, parse_patterns


logger = logging.getLogger(__name__)


class AutoCancelExtension(Extension):
    stage = '10'

    def run(self):
        payload = self.current.head.fetch_previous_commits()
        head = True
        for i, commit in enumerate(self.current.head.process_commits(payload)):
            commit_payload = commit.fetch_statuses()
            statuses = commit.process_statuses(commit_payload)
            for status in statuses.values():
                status = CommitStatus(status)
                if status.get('state') != 'pending':
                    continue

                if status.is_queueable:
                    continue

                if head:
                    self.current.poll_queue.append((commit, status))
                else:
                    logger.info("Queue cancel of %s on %s.", status, commit)
                    self.current.cancel_queue.append((commit, status))

            head = False


class HelpExtension(Extension):
    stage = '90'

    DEFAULTS = {
        'help_mentions': set(),
    }
    DISTRIBUTION = pkg_resources.get_distribution('jenkins-epo')
    HELP = """\
<!--
jenkins: ignore
-->

%(mentions)s: this is what I understand:

```yaml
# Build this PR first. Allowed only in PR description.
jenkins: urgent

%(help)s
```

You can mix instructions. Multiline instructions **must** be in code block.

--
*%(me)s for your service*

<!--
jenkins: [process, help-reset]

Running %(software)s==%(version)s on %(host)s
Extensions: %(extensions)s
-->
"""

    def process_instruction(self, instruction):
        if instruction.name in ('help', 'man'):
            self.current.help_mentions.add(instruction.author)
        elif instruction == 'help-reset':
            self.current.help_mentions = set()

    def generate_comment(self):
        docs = []
        for ext in self.bot.extensions:
            doc = ext.__class__.__doc__
            if not doc:
                continue
            docs.append(inspect.cleandoc(doc))
        help_ = '\n\n'.join(docs)
        return self.HELP % dict(
            extensions=','.join(sorted(self.bot.extensions_map.keys())),
            help=help_,
            host=socket.getfqdn(),
            me=self.current.head.repository.SETTINGS.NAME,
            mentions=', '.join(sorted([
                '@' + m for m in self.current.help_mentions
            ])),
            software=self.DISTRIBUTION.project_name,
            version=self.DISTRIBUTION.version,
        )

    def run(self):
        if self.current.help_mentions:
            self.current.head.comment(body=self.generate_comment())


class ErrorExtension(Extension):
    stage = '99'

    ERROR_COMMENT = """
%(emoji)s

%(error)s

<!--
jenkins: reset-errors
-->
"""  # noqa

    def process_instruction(self, instruction):
        if instruction == 'reset-errors':
            self.current.errors = [
                e for e in self.current.errors
                if e.date > instruction.date
            ]

    def run(self):
        for error in self.current.errors:
            self.current.head.comment(body=self.ERROR_COMMENT % dict(
                emoji=random.choice((
                    ':see_no_evil:', ':bangbang:', ':confused:',
                )),
                error=error.body,
            ))


class MergerExtension(Extension):
    """
    # Acknowledge for auto-merge
    jenkins: opm
    """

    stage = '90'

    DEFAULTS = {
        'opm': None,
        'opm_denied': [],
        'opm_processed': None,
        'last_merge_error': None,
    }

    SETTINGS = {
        'WIP_TITLE': 'wip*,[wip*',
    }

    OPM_COMMENT = """
%(mention)s, %(message)s %(emoji)s

<!--
jenkins: opm-processed
-->
"""

    MERGE_ERROR_COMMENT = """
%(mention)s, %(message)s %(emoji)s

<!--
jenkins: {last-merge-error: %(message)r}
-->
"""

    def begin(self):
        super(MergerExtension, self).begin()

        if hasattr(self.current.head, 'merge'):
            patterns = parse_patterns(self.current.SETTINGS.WIP_TITLE.lower())
            title = self.current.head.payload['title'].lower()
            self.current.wip = match(title, patterns)
            if self.current.wip:
                logger.debug("%s is a WIP.", self.current.head)

    def process_instruction(self, instruction):
        if instruction in {'lgtm', 'merge', 'opm'}:
            self.process_opm(instruction)
        elif instruction in {'lgtm-processed', 'opm-processed'}:
            self.current.opm_denied[:] = []
            self.current.opm_processed = instruction
        elif instruction == 'last-merge-error':
            self.current.last_merge_error = instruction

    def process_opm(self, opm):
        if not hasattr(self.current.head, 'merge'):
            return logger.debug("OPM on a non PR. Weird!")

        if opm.date < self.current.last_commit.date:
            return logger.debug("Skip outdated OPM.")

        if opm.author in self.current.SETTINGS.REVIEWERS:
            logger.info("Accept @%s as reviewer.", opm.author)
            self.current.opm = opm
        else:
            logger.info("Refuse OPM from @%s.", opm.author)
            self.current.opm_denied.append(opm)

    def run(self):
        denied = {i.author for i in self.current.opm_denied}
        if denied:
            self.current.head.comment(body=self.OPM_COMMENT % dict(
                emoji=random.choice((
                    ':confused:', ':cry:', ':disappointed:', ':frowning:',
                    ':scream:',
                )),
                mention=', '.join(sorted(['@' + a for a in denied])),
                message="you're not allowed to acknowledge PR",
            ))

        if not self.current.opm:
            return
        logger.debug("Accept to merge for @%s.", self.current.opm.author)

        if self.current.wip:
            logger.info("Not merging WIP PR.")
            proc = self.current.opm_processed
            if proc and proc.date > self.current.opm.date:
                return

            self.current.head.comment(body=self.OPM_COMMENT % dict(
                emoji=random.choice((
                    ':confused:', ':hushed:', ':no_mouth:', ':open_mouth:',
                )),
                mention='@' + self.current.opm.author,
                message="this PR is still WIP",
            ))
            return

        status = self.current.last_commit.fetch_combined_status()
        if status['state'] != 'success':
            return logger.debug("PR not green. Postpone merge.")

        try:
            self.current.head.merge()
        except ApiError as e:
            error = e.response['json']['message']
            if self.current.last_merge_error:
                last_error = self.current.last_merge_error.args
                if error == last_error:
                    return logger.debug("Merge still failing: %s", error)

            logger.warn("Failed to merge: %s", error)
            self.current.head.comment(body=self.MERGE_ERROR_COMMENT % dict(
                emoji=random.choice((':confused:', ':disappointed:')),
                mention='@' + self.current.opm.author, message=error,
            ))
        else:
            logger.warn("Merged %s!", self.current.head)
            self.current.head.delete_branch()


class ReportExtension(Extension):
    stage = '90'

    ISSUE_TEMPLATE = """
Commit %(abbrev)s is broken on %(branch)s:

%(builds)s
"""
    COMMENT_TEMPLATE = """
Build failure reported at #%(issue)s.

<!--
jenkins: report-done
-->
"""

    DEFAULTS = {
        # Issue URL where the failed builds are reported.
        'report_done': False,
    }

    def process_instruction(self, instruction):
        if instruction == 'report-done':
            self.current.report_done = True

    def run(self):
        if self.current.report_done:
            return

        if not isinstance(self.current.head, Branch):
            return

        errored = [
            s for s in self.current.statuses.values()
            if s['state'] == 'failure'
        ]
        if not errored:
            return

        branch_name = self.current.head.ref[len('refs/heads/'):]
        builds = '- ' + '\n- '.join([s['target_url'] for s in errored])
        issue = self.current.head.repository.report_issue(
            title="%s is broken" % (branch_name,),
            body=self.ISSUE_TEMPLATE % dict(
                abbrev=self.current.head.sha[:7],
                branch=branch_name,
                builds=builds,
                sha=self.current.head.sha,
                ref=self.current.head.ref,
            )
        )

        self.current.head.comment(body=self.COMMENT_TEMPLATE % dict(
            issue=issue['number']
        ))


class YamlExtension(Extension):
    """
    # Ephemeral jobs parameters
    jenkins:
      parameters:
        job1:
          PARAM: value
    """
    stage = '00'

    DEFAULTS = {
        'yaml': {},
        'yaml_date': None,
    }

    SETTINGS = {
        # Jenkins credentials used to clone
        'JOBS_CREDENTIALS': None,
        # Jenkins node/label
        'JOBS_NODE': 'yml',
    }

    def process_instruction(self, instruction):
        if instruction.name in {'yaml', 'yml'}:
            if not isinstance(instruction.args, dict):
                self.current.errors.append(
                    Error("YAML args is not a mapping.", instruction.date)
                )
                return
            deepupdate(self.current.yaml, instruction.args)
            self.current.yaml_date = instruction.date
        elif instruction.name in {'parameters', 'params', 'param'}:
            args = {}
            for job, parameters in instruction.args.items():
                args[job] = dict(parameters=parameters)
            deepupdate(self.current.yaml, args)
            self.current.yaml_date = instruction.date

    def list_job_specs(self, jenkins_yml=None):
        defaults = dict(
            node=SETTINGS.JOBS_NODE,
            github_repository=self.current.head.repository.url,
            scm_credentials=SETTINGS.JOBS_CREDENTIALS,
            set_commit_status=not SETTINGS.DRY_RUN,
        )

        jenkins_yml = jenkins_yml or '{}'
        jobs = {}
        for job in JobSpec.parse_all(jenkins_yml, defaults=defaults):
            job.repository = self.current.head.repository
            jobs[job.name] = job

        return jobs

    def run(self):
        head = self.current.head

        try:
            jenkins_yml = GITHUB.fetch_file_contents(
                head.repository, 'jenkins.yml', ref=head.ref,
            )
            logger.debug("Loading jenkins.yml.")
        except ApiNotFoundError:
            jenkins_yml = None

        self.current.job_specs = self.list_job_specs(jenkins_yml)
        self.current.jobs = head.repository.jobs

        for name, args in self.current.yaml.items():
            if name not in self.current.job_specs:
                self.current.errors.append(Error(
                    body="Can't override unknown job %s." % (name,),
                    date=self.current.yaml_date,
                ))
                continue

            current_spec = self.current.job_specs[name]
            config = dict(deepcopy(current_spec.config), **args)
            overlay_spec = JobSpec(name, config)
            logger.info("Ephemeral update of %s spec.", name)
            self.current.job_specs[name] = overlay_spec
