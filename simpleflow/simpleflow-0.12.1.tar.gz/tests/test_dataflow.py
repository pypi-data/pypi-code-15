# -*- coding: utf-8 -*-
from __future__ import absolute_import
from builtins import range

import functools
from mock import patch

import boto
from moto import mock_swf

import swf.models
import swf.models.decision
from simpleflow.utils import json_dumps
from swf.models.history import builder
from swf.responses import Response

from simpleflow import (
    Workflow,
    futures,
)
from simpleflow.history import History
from simpleflow.swf import constants
from simpleflow.swf.executor import Executor

from .data import (
    DOMAIN,
    double,
    increment,
    increment_retry,
    raise_error,
    raise_on_failure,
    triple,
    Tetra,
)


class ATestWorkflow(Workflow):
    name = 'test_workflow'
    version = 'test_version'
    task_list = 'test_task_list'
    decision_tasks_timeout = '300'
    execution_timeout = '3600'
    tag_list = None  # FIXME should be optional
    child_policy = None  # FIXME should be optional


def check_task_scheduled_decision(decision, task):
    """
    Asserts that *decision* schedules *task*.
    """
    assert decision['decisionType'] == 'ScheduleActivityTask'

    attributes = decision['scheduleActivityTaskDecisionAttributes']
    assert attributes['activityType'] == {
        'name': task.name,
        'version': task.version
    }


class ATestDefinitionWithInput(ATestWorkflow):
    """
    Execute a single task with an argument passed as the workflow's input.
    """

    def run(self, a):
        b = self.submit(increment, a)
        return b.result


@mock_swf
def test_workflow_with_input():
    workflow = ATestDefinitionWithInput
    executor = Executor(DOMAIN, workflow)

    result = 5
    history = builder.History(workflow,
                              input={'args': (4,)})

    # The executor should only schedule the *increment* task.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 1},
                        result=result)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # As there is only a single task, the executor should now complete the
    # workflow and set its result accordingly.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(result))

    assert decisions[0] == workflow_completed


@mock_swf
def test_workflow_with_repair_if_task_successful():
    workflow = ATestDefinitionWithInput
    history = builder.History(workflow, input={'args': [4]})

    # Now let's build the history to repair
    previous_history = builder.History(workflow, input={'args': [4]})
    decision_id = previous_history.last_id
    (previous_history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 4},
                        result=57)  # obviously wrong but helps see if things work
     )
    to_repair = History(previous_history)
    to_repair.parse()

    executor = Executor(DOMAIN, workflow, repair_with=to_repair)

    # The executor should not schedule anything, it should use previous history
    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == 1
    assert decisions[0]['decisionType'] == 'ScheduleActivityTask'
    attrs = decisions[0]['scheduleActivityTaskDecisionAttributes']
    assert attrs['taskList']['name'].startswith("FAKE-")


@mock_swf
def test_workflow_with_repair_if_task_failed():
    workflow = ATestDefinitionWithInput
    history = builder.History(workflow, input={'args': [4]})

    # Now let's build the history to repair
    previous_history = builder.History(workflow, input={'args': [4]})
    decision_id = previous_history.last_id
    (previous_history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='failed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 4},
                        result=57)  # obviously wrong but helps see if things work
     )
    to_repair = History(previous_history)
    to_repair.parse()

    executor = Executor(DOMAIN, workflow, repair_with=to_repair)

    # The executor should not schedule anything, it should use previous history
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)


@mock_swf
def test_workflow_with_repair_and_force_activities():
    workflow = ATestDefinitionWithInput
    history = builder.History(workflow, input={'args': [4]})

    # Now let's build the history to repair
    previous_history = builder.History(workflow, input={'args': [4]})
    decision_id = previous_history.last_id
    (previous_history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 4},
                        result=57)  # obviously wrong but helps see if things work
     )
    to_repair = History(previous_history)
    to_repair.parse()

    executor = Executor(DOMAIN, workflow, repair_with=to_repair,
                        force_activities="increment|something_else")

    # The executor should not schedule anything, it should use previous history
    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == 1
    assert decisions[0]['decisionType'] == 'ScheduleActivityTask'
    attrs = decisions[0]['scheduleActivityTaskDecisionAttributes']
    assert not attrs['taskList']['name'].startswith("FAKE-")
    check_task_scheduled_decision(decisions[0], increment)


class ATestDefinitionWithBeforeReplay(ATestWorkflow):
    """
    Execute a single task with an argument passed as the workflow's input.
    """

    def before_replay(self, history):
        self.a = history.events[0].input['args'][0]

    def run(self, a):
        b = self.submit(increment, a)
        return b.result


@mock_swf
def test_workflow_with_before_replay():
    workflow = ATestDefinitionWithBeforeReplay
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow,
                              input={'args': (4,)})

    # The executor should only schedule the *increment* task.
    assert not hasattr(executor.workflow, 'a')
    decisions, _ = executor.replay(Response(history=history))
    assert executor.workflow.a == 4


class ATestDefinitionWithAfterReplay(ATestWorkflow):
    """
    Execute a single task with an argument passed as the workflow's input.
    """

    def after_replay(self, history):
        self.b = history.events[0].input['args'][0] + 1

    def after_closed(self, history):
        self.c = history.events[0].input['args'][0] + 1

    def run(self, a):
        b = self.submit(increment, a)
        return b.result


@mock_swf
def test_workflow_with_after_replay():
    workflow = ATestDefinitionWithAfterReplay
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow,
                              input={'args': (4,)})

    # The executor should only schedule the *increment* task.
    assert not hasattr(executor.workflow, 'b')
    decisions, _ = executor.replay(Response(history=history))
    assert executor.workflow.b == 5
    # Check that workflow is not marked as finished
    assert not hasattr(executor.workflow, 'c')


class ATestDefinitionWithAfterClosed(ATestWorkflow):
    """
    Execute a single task with an argument passed as the workflow's input.
    """

    def after_closed(self, history):
        self.b = history.events[0].input['args'][0] + 1

    def run(self, a):
        b = self.submit(increment, a)
        return b.result


@mock_swf
def test_workflow_with_after_closed():
    workflow = ATestDefinitionWithAfterClosed
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow,
                              input={'args': (4,)})

    # The executor should only schedule the *increment* task.
    assert not hasattr(executor.workflow, 'b')
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 4},
                        result=5)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # *double* has completed and the ``b.result``is now available. The executor
    # should complete the workflow and its result to ``b.result``.
    assert not hasattr(executor.workflow, 'b')
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(5))

    assert decisions[0] == workflow_completed
    assert executor.workflow.b == 5


class ATestDefinition(ATestWorkflow):
    """
    Executes two tasks. The second depends on the first.
    """

    def run(self):
        a = self.submit(increment, 1)
        assert isinstance(a, futures.Future)

        b = self.submit(double, a)

        return b.result


@mock_swf
def test_workflow_with_two_tasks():
    workflow = ATestDefinition
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)

    # *double* requires the result of *increment*, hold by the *a* future.
    # Hence the executor schedule *increment*.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 1},
                        result=2)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # Now ``a.result``contains the result of *increment*'s that is finished.
    # The line ``return b.result`` requires the computation of *double* with
    # ``a.result``, then the executor should schedule *double*.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], double)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(double,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.double-1',
                        input={'args': 2},
                        result=4)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # *double* has completed and the ``b.result``is now available. The executor
    # should complete the workflow and its result to ``b.result``.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(4))

    assert decisions[0] == workflow_completed


@mock_swf
def test_workflow_with_two_tasks_not_completed():
    """
    This test checks how the executor behaves when a task is still running.
    """
    workflow = ATestDefinitionWithInput
    executor = Executor(DOMAIN, workflow)

    arg = 4
    result = 5
    history = builder.History(workflow,
                              input={'args': (arg,)})

    # The executor should schedule *increment*.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task in state ``started`` to the history.
    decision_id = history.last_id
    scheduled_id = decision_id + 1
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='started',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 1},
                        result=5)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # The executor cannot schedule any other task, it returns an empty
    # decision.
    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == 0

    # Let's now set the task as ``completed`` in the history.
    decision_id = history.last_id
    (history
     .add_activity_task_completed(scheduled=scheduled_id,
                                  started=scheduled_id + 1,
                                  result=result)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # As there is a single task and it is now finished, the executor should
    # complete the workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(result))

    assert decisions[0] == workflow_completed


class ATestDefinitionSameTask(ATestWorkflow):
    """
    This workflow executes the same task with a different argument.
    """

    def run(self, *args, **kwargs):
        a = self.submit(increment, 1)
        b = self.submit(increment, a)

        return b.result


@mock_swf
def test_workflow_with_same_task_called_two_times():
    """
    This test checks how the executor behaves when the same task is executed
    two times with a different argument.
    """
    workflow = ATestDefinitionSameTask
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)

    # As the second task depends on the first, the executor should only
    # schedule the first task.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 1},
                        result=2)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # The first task is finished, the executor should schedule the second one.
    decision_id = history.last_id
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-2',
                        input={'args': 2},
                        result=3)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # The executor should now complete the workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(3))

    assert decisions[0] == workflow_completed


class ATestDefinitionSameFuture(ATestWorkflow):
    """
    This workflow uses a single variable to hold the future of two different
    tasks.
    """

    def run(self, *args, **kwargs):
        a = self.submit(increment, 1)
        a = self.submit(double, a)

        return a.result


@mock_swf
def test_workflow_reuse_same_future():
    workflow = ATestDefinitionSameFuture
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)

    # *double* depends on *increment*, then the executor should only schedule
    # *increment* at first.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        input={'args': 1},
                        activity_id='activity-tests.data.activities.increment-1',
                        result=2)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # *increment* is finished, the executor should schedule *double*.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], double)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(double,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.double-1',
                        input={'args': 2},
                        result=4)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # The executor should now complete the workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(4))

    assert decisions[0] == workflow_completed


class ATestDefinitionTwoTasksSameFuture(ATestWorkflow):
    """
    This test checks how the executor behaves when two tasks depends on the
    same task.
    """

    def run(self, *args, **kwargs):
        a = self.submit(increment, 1)
        b = self.submit(double, a)
        c = self.submit(increment, a)

        return (b.result, c.result)


@mock_swf
def test_workflow_with_two_tasks_same_future():
    workflow = ATestDefinitionTwoTasksSameFuture
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)

    # ``b.result`` and ``c.result`` requires the execution of ``double(a)`` and
    # ``increment(a)``. They both depend on the execution of ``increment(1)``so
    # the executor should schedule ``increment(1)``.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)

    # Let's add the task to the history to simulate its completion.
    decision_id = history.last_id
    (history
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-1',
                        input={'args': 1},
                        result=2)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # Now ``a.result`` is available and the executor should schedule the
    # execution of ``double(a)`` and ``increment(a)`` at the same time.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], double)
    check_task_scheduled_decision(decisions[1], increment)

    # Let's add both tasks to the history to simulate their completion.
    decision_id = history.last_id
    (history
     .add_activity_task(double,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.double-1',
                        input={'args': 2},
                        result=4)
     .add_activity_task(increment,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment-2',
                        input={'args': 2},
                        result=3)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # Both tasks completed, hence the executor should complete the workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps((4, 3)))

    assert decisions[0] == workflow_completed


class ATestDefinitionMap(ATestWorkflow):
    """
    This workflow only maps a task on several values, they wait for the
    availability of their result.
    """
    nb_parts = 3

    def run(self, *args, **kwargs):
        xs = self.map(increment, range(self.nb_parts))
        values = futures.wait(*xs)

        return values


@mock_swf
def test_workflow_map():
    workflow = ATestDefinitionMap
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)

    nb_parts = ATestDefinitionMap.nb_parts

    # All the futures returned by the map are passed to wait().
    # The executor should then schedule all of them.
    decisions, _ = executor.replay(Response(history=history))
    for i in range(nb_parts):
        check_task_scheduled_decision(decisions[i], increment)

    # Let's add all tasks of the map to the history to simulate their
    # completion.
    decision_id = history.last_id
    for i in range(nb_parts):
        history.add_activity_task(
            increment,
            decision_id=decision_id,
            activity_id='activity-tests.data.activities.increment-{}'.format(
                i + 1),
            last_state='completed',
            input={'args': i},
            result=i + 1)
    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # All tasks are finished, the executor should complete the workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(
        result=json_dumps([i + 1 for i in range(nb_parts)]))

    assert decisions[0] == workflow_completed


class ATestDefinitionRetryActivity(ATestWorkflow):
    """
    This workflow executes a task that is retried on failure.
    """

    def run(self, *args, **kwargs):
        a = self.submit(increment_retry, 7)

        return a.result


@mock_swf
def test_workflow_retry_activity():
    workflow = ATestDefinitionRetryActivity
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)

    # There is a single task, hence the executor should schedule it first.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment_retry)

    # Let's add the task in ``failed`` state.
    decision_id = history.last_id
    (history
     .add_activity_task(increment_retry,
                        decision_id=decision_id,
                        last_state='failed',
                        activity_id='activity-tests.data.activities.increment_retry-1')
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # As the retry value is one, the executor should retry i.e. schedule the
    # task again.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment_retry)

    # Let's add the task in ``completed`` state.
    decision_id = history.last_id
    (history
     .add_activity_task(increment_retry,
                        decision_id=decision_id,
                        last_state='completed',
                        activity_id='activity-tests.data.activities.increment_retry-1',
                        input={'args': 7},
                        result=8)
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # Now the task is finished and the executor should complete the workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(8))

    assert decisions[0] == workflow_completed


@mock_swf
def test_workflow_retry_activity_failed_again():
    workflow = ATestDefinitionRetryActivity
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)

    # There is a single task, hence the executor should schedule it first.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment_retry)

    # Let's add the task in ``failed`` state.
    decision_id = history.last_id
    (history
     .add_activity_task(
        increment_retry,
        decision_id=decision_id,
        last_state='failed',
        activity_id='activity-tests.data.activities.increment_retry-1')
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # As the retry value is one, the executor should retry i.e. schedule the
    # task again.
    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment_retry)

    # Let's add the task in ``failed`` state again.
    decision_id = history.last_id
    (history
     .add_activity_task(
        increment_retry,
        decision_id=decision_id,
        last_state='failed',
        activity_id='activity-tests.data.activities.increment_retry-1')
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # There is no more retry. The executor should set `Future.exception` and
    # complete the workflow as there is no further task.
    decisions, _ = executor.replay(Response(history=history))

    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    # ``a.result`` is ``None`` because it was not set.
    workflow_completed.complete(result=json_dumps(None))

    assert decisions[0] == workflow_completed


class ATestDefinitionChildWorkflow(ATestWorkflow):
    """
    This workflow executes a child workflow.
    """

    def run(self, x):
        y = self.submit(ATestDefinition, x)
        return y.result


@mock_swf
def test_workflow_with_child_workflow():
    workflow = ATestDefinitionChildWorkflow
    executor = Executor(DOMAIN, workflow)

    # FIXME the original test only contains args, and check both keys are present.
    # FIXME But their order is unspecified from one execution to the next
    input = {'args': (1,), 'kwargs': {}}
    history = builder.History(workflow, input=input)

    # The executor should schedule the execution of a child workflow.
    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == 1
    assert decisions == [{
        'startChildWorkflowExecutionDecisionAttributes': {
            'workflowId': 'workflow-test_workflow-1',
            'taskList': {
                'name': 'test_task_list'
            },
            'executionStartToCloseTimeout': '3600',
            'input': json_dumps(input),
            'workflowType': {
                'version': 'test_version',
                'name': 'test_workflow'
            },
            'taskStartToCloseTimeout': '300'
        },
        'decisionType': 'StartChildWorkflowExecution'
    }]

    # Let's add the child workflow to the history to simulate its completion.
    (history
        .add_decision_task()
        .add_child_workflow(
        workflow,
        workflow_id='workflow-test_workflow-1',
        task_list=ATestWorkflow.task_list,
        input='"{\\"args\\": [1], \\"kwargs\\": {}}"',
        result='4'
    ))

    # Now the child workflow is finished and the executor should complete the
    # workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result=json_dumps(4))

    assert decisions[0] == workflow_completed


class ATestDefinitionMoreThanMaxDecisions(ATestWorkflow):
    """
    This workflow executes more tasks than the maximum number of decisions a
    decider can take once.
    """

    def run(self):
        results = self.map(increment, range(constants.MAX_DECISIONS + 5))
        futures.wait(*results)


@mock_swf
def test_workflow_with_more_than_max_decisions():
    workflow = ATestDefinitionMoreThanMaxDecisions
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)

    # The first time, the executor should schedule ``constants.MAX_DECISIONS``
    # decisions and a timer to force the scheduling of the remaining tasks.
    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == constants.MAX_DECISIONS
    assert decisions[-1].type == 'StartTimer'

    decision_id = history.last_id
    for i in range(constants.MAX_DECISIONS):
        history.add_activity_task(
            increment,
            decision_id=decision_id,
            activity_id='activity-tests.data.activities.increment-{}'.format(
                i + 1),
            last_state='completed',
            result=i + 1)
    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # Once the first batch of ``constants.MAX_DECISIONS`` tasks is finished,
    # the executor should schedule the 5 remaining ones.
    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == 5

    for i in range(constants.MAX_DECISIONS - 1, constants.MAX_DECISIONS + 5):
        history.add_activity_task(
            increment,
            decision_id=decision_id,
            activity_id='activity-tests.data.activities.increment-{}'.format(
                i + 1),
            last_state='completed',
            result=i + 1)
    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # All tasks are finised, the executor should complete the workflow.
    decisions, _ = executor.replay(Response(history=history))
    workflow_completed = swf.models.decision.WorkflowExecutionDecision()
    workflow_completed.complete(result='null')

    assert decisions[0] == workflow_completed


class OnFailureMixin(object):
    failed = False

    def on_failure(self, history, reason, details=None):
        self.failed = True


class ATestDefinitionFailWorkflow(OnFailureMixin, ATestWorkflow):
    """
    This workflow executes a single task that fails, then it explicitly fails
    the whole workflow.
    """

    def run(self):
        result = self.submit(raise_error)
        if result.exception:
            self.fail('error')

        return result.result


@mock_swf
def test_workflow_failed_from_definition():
    workflow = ATestDefinitionFailWorkflow
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)

    # Let's directly add the task in state ``failed`` to make the executor fail
    # the workflow.
    history.add_activity_task(
        raise_error,
        decision_id=history.last_id,
        activity_id='activity-tests.data.activities.raise_error-1',
        last_state='failed',
        result=json_dumps(None))

    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # Now the workflow definition calls ``Workflow.fail('error')`` that should
    # fail the whole workflow.
    decisions, _ = executor.replay(Response(history=history))

    assert executor.workflow.failed is True

    workflow_failed = swf.models.decision.WorkflowExecutionDecision()
    workflow_failed.fail(reason='Workflow execution failed: error')

    assert decisions[0] == workflow_failed


class ATestDefinitionActivityRaisesOnFailure(OnFailureMixin, ATestWorkflow):
    """
    This workflow executes a task that fails and has the ``raises_on_failure``
    flag set to ``True``. It means it will raise an exception in addition to
    filling the ``Future.exception``'s attribute.
    """

    def run(self):
        return self.submit(raise_on_failure).result


@mock_swf
def test_workflow_activity_raises_on_failure():
    workflow = ATestDefinitionActivityRaisesOnFailure
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)

    history.add_activity_task(
        raise_on_failure,
        decision_id=history.last_id,
        activity_id='activity-tests.data.activities.raise_on_failure-1',
        last_state='failed',
        reason='error')

    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # The executor should fail the workflow and extract the reason from the
    # exception raised in the workflow definition.
    decisions, _ = executor.replay(Response(history=history))

    assert executor.workflow.failed is True

    workflow_failed = swf.models.decision.WorkflowExecutionDecision()
    workflow_failed.fail(
        reason='Workflow execution error in task '
               'activity-tests.data.activities.raise_on_failure: '
               '"error"')

    assert decisions[0] == workflow_failed


class ATestOnFailureDefinition(OnFailureMixin, ATestWorkflow):
    def run(self):
        if self.submit(raise_error).exception:
            self.fail('FAIL')


@mock_swf
def test_on_failure_callback():
    workflow = ATestOnFailureDefinition
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)

    history.add_activity_task(
        raise_error,
        decision_id=history.last_id,
        activity_id='activity-tests.data.activities.raise_error-1',
        last_state='failed',
        reason='error')

    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    # The executor should fail the workflow and extract the reason from the
    # exception raised in the workflow definition.
    decisions, _ = executor.replay(Response(history=history))

    assert executor.workflow.failed is True

    workflow_failed = swf.models.decision.WorkflowExecutionDecision()
    workflow_failed.fail(
        reason='Workflow execution failed: FAIL')

    assert decisions[0] == workflow_failed


class ATestMultipleScheduledActivitiesDefinition(ATestWorkflow):
    def run(self):
        a = self.submit(increment, 1)
        b = self.submit(increment, 2)
        c = self.submit(double, b)

        return [a.result, b.result, c.result]


@mock_swf
def test_multiple_scheduled_activities():
    """
    When ``Future.exception`` was made blocking if the future is not finished,
    :py:meth:`swf.executor.Executor.resume` did not check ``future.finished``
    before ``future.exception is None``. It mades the call to ``.resume()`` to
    block for the first scheduled task it encountered instead of returning it.
    This issue was fixed in commit 6398aa8.
    With the wrong behaviour, the call to ``executor.replay()`` would not
    schedule the ``double`` task even after the task represented by *b*
    (``self.submit(increment, 2)``) has completed.
    """
    workflow = ATestMultipleScheduledActivitiesDefinition
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)

    decision_id = history.last_id
    (history
        .add_activity_task_scheduled(
        increment,
        decision_id=decision_id,
        activity_id='activity-tests.data.activities.increment-1',
        input={'args': 1})
        # The right behaviour is to schedule the ``double`` task when *b* is in
        # state finished.
        .add_activity_task(
        increment,
        decision_id=decision_id,
        activity_id='activity-tests.data.activities.increment-2',
        last_state='completed',
        input={'args': 2},
        result='3'))

    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], double)


@mock_swf
def test_activity_task_timeout():
    workflow = ATestDefinition
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)
    decision_id = history.last_id
    (history
        .add_activity_task(
        increment,
        activity_id='activity-tests.data.activities.increment-1',
        decision_id=decision_id,
        last_state='timed_out',
        timeout_type='START_TO_CLOSE'))

    decisions, _ = executor.replay(Response(history=history))
    # The task timed out and there is no retry.
    assert len(decisions) == 1
    check_task_scheduled_decision(decisions[0], double)


@mock_swf
def test_activity_task_timeout_retry():
    workflow = ATestDefinitionRetryActivity
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)
    decision_id = history.last_id
    (history
        .add_activity_task(
        increment_retry,
        activity_id='activity-tests.data.activities.increment_retry-1',
        decision_id=decision_id,
        last_state='timed_out',
        timeout_type='START_TO_CLOSE'))

    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == 1
    check_task_scheduled_decision(decisions[0], increment_retry)


@mock_swf
def test_activity_task_timeout_raises():
    workflow = ATestDefinitionActivityRaisesOnFailure
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)
    decision_id = history.last_id
    (history
        .add_activity_task(
        raise_on_failure,
        activity_id='activity-tests.data.activities.raise_on_failure-1',
        decision_id=decision_id,
        last_state='timed_out',
        timeout_type='START_TO_CLOSE'))

    decisions, _ = executor.replay(Response(history=history))
    workflow_failed = swf.models.decision.WorkflowExecutionDecision()
    workflow_failed.fail(
        reason='Workflow execution error in task '
               'activity-tests.data.activities.raise_on_failure: '
               '"TimeoutError(START_TO_CLOSE)"')

    assert decisions[0] == workflow_failed


@mock_swf
def test_activity_not_found_schedule_failed():
    conn = boto.connect_swf()
    conn.register_domain("TestDomain", "50")

    workflow = ATestDefinition
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)
    decision_id = history.last_id
    (history
        .add_activity_task_schedule_failed(
        activity_id='activity-tests.data.activities.increment-1',
        decision_id=decision_id,
        activity_type={
            'name': increment.name,
            'version': increment.version
        },
        cause='ACTIVITY_TYPE_DOES_NOT_EXIST'))

    decisions, _ = executor.replay(Response(history=history))
    check_task_scheduled_decision(decisions[0], increment)


def raise_already_exists(activity):
    @functools.wraps(raise_already_exists)
    def wrapped(*args):
        raise swf.exceptions.AlreadyExistsError(
            '<ActivityType domain={} name={} version={} status=REGISTERED> '
            'already exists'.format(
                DOMAIN.name,
                activity.name,
                activity.version))

    return wrapped


@mock_swf
def test_activity_not_found_schedule_failed_already_exists():
    workflow = ATestDefinition
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow)
    decision_id = history.last_id
    (history
        .add_activity_task_schedule_failed(
        activity_id='activity-tests.data.activities.increment-1',
        decision_id=decision_id,
        activity_type={
            'name': increment.name,
            'version': increment.version
        },
        cause='ACTIVITY_TYPE_DOES_NOT_EXIST'))

    with patch(
            'swf.models.ActivityType.save',
            raise_already_exists(increment)):
        decisions, _ = executor.replay(Response(history=history))

    check_task_scheduled_decision(decisions[0], increment)


class ATestDefinitionMoreThanMaxOpenActivities(ATestWorkflow):
    """
    This workflow executes more tasks than the maximum number of decisions a
    decider can take once.
    """

    def run(self):
        results = self.map(
            increment,
            range(constants.MAX_OPEN_ACTIVITY_COUNT + 5))
        futures.wait(*results)


@mock_swf
def test_more_than_1000_open_activities_scheduled():
    workflow = ATestDefinitionMoreThanMaxOpenActivities
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)

    # The first time, the executor should schedule
    # ``constants.MAX_OPEN_ACTIVITY_COUNT`` decisions.
    # No timer because we wait for at least an activity to complete.
    for i in range(constants.MAX_OPEN_ACTIVITY_COUNT // constants.MAX_DECISIONS):
        decisions, _ = executor.replay(Response(history=history))
        assert len(decisions) == constants.MAX_DECISIONS

    decision_id = history.last_id
    for i in range(constants.MAX_OPEN_ACTIVITY_COUNT):
        history.add_activity_task(
            increment,
            decision_id=decision_id,
            activity_id='activity-tests.data.activities.increment-{}'.format(
                i + 1),
            last_state='scheduled',
            result=i + 1)
    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    decisions, _ = executor.replay(Response(history=history))
    assert executor._open_activity_count == constants.MAX_OPEN_ACTIVITY_COUNT
    assert len(decisions) == 0


@mock_swf
def test_more_than_1000_open_activities_scheduled_and_running():
    def get_random_state():
        import random
        return random.choice(['scheduled', 'started'])

    workflow = ATestDefinitionMoreThanMaxOpenActivities
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)

    # The first time, the executor should schedule
    # ``constants.MAX_OPEN_ACTIVITY_COUNT`` decisions.
    # No timer because we wait for at least an activity to complete.
    for i in range(constants.MAX_OPEN_ACTIVITY_COUNT // constants.MAX_DECISIONS):
        decisions, _ = executor.replay(Response(history=history))
        assert len(decisions) == constants.MAX_DECISIONS

    decision_id = history.last_id
    for i in range(constants.MAX_OPEN_ACTIVITY_COUNT):
        history.add_activity_task(
            increment,
            decision_id=decision_id,
            activity_id='activity-tests.data.activities.increment-{}'.format(
                i + 1),
            last_state=get_random_state(),
            result=i + 1)
    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    decisions, _ = executor.replay(Response(history=history))
    assert len(decisions) == 0


@mock_swf
def test_more_than_1000_open_activities_partial_max():
    workflow = ATestDefinitionMoreThanMaxOpenActivities
    executor = Executor(DOMAIN, workflow)
    history = builder.History(workflow)
    decisions, _ = executor.replay(Response(history=history))

    first_decision_id = history.last_id
    for i in range(constants.MAX_OPEN_ACTIVITY_COUNT - 2):
        history.add_activity_task(
            increment,
            decision_id=first_decision_id,
            activity_id='activity-tests.data.activities.increment-{}'.format(
                i + 1),
            last_state='scheduled',
            result=i + 1)
    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    decisions, _ = executor.replay(Response(history=history))
    assert executor._open_activity_count == constants.MAX_OPEN_ACTIVITY_COUNT
    assert len(decisions) == 2

    history.add_decision_task_completed()
    for i in range(2):
        id_ = constants.MAX_OPEN_ACTIVITY_COUNT - 2 + i + 1
        history.add_activity_task(
            increment,
            decision_id=history.last_id,
            activity_id='activity-tests.data.activities.increment-{}'.format(
                id_),
            last_state='scheduled',
            result=id_,
        )

    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    decisions, _ = executor.replay(Response(history=history))
    assert executor._open_activity_count == constants.MAX_OPEN_ACTIVITY_COUNT
    assert len(decisions) == 0

    history.add_decision_task_completed()

    for i in range(constants.MAX_OPEN_ACTIVITY_COUNT - 2):
        scheduled_id = first_decision_id + i + 1
        history.add_activity_task_started(scheduled_id)
        history.add_activity_task_completed(
            scheduled_id,
            started=history.last_id,
        )

    (history
     .add_decision_task_scheduled()
     .add_decision_task_started())

    decisions, _ = executor.replay(Response(history=history))
    # 2 already scheduled + 5 to schedule now
    assert executor._open_activity_count == 7
    assert len(decisions) == 5


class ATestTaskNaming(ATestWorkflow):
    """
    This workflow executes a few tasks and tests the naming (task ID
    assignation) depending on their idempotence.
    """

    def run(self):
        results = []
        results.append(self.submit(increment, 0))
        results.append(self.submit(increment, 0))
        results.append(self.submit(triple, 1))
        results.append(self.submit(triple, 2))
        results.append(self.submit(triple, 2))
        results.append(self.submit(Tetra, 1))
        futures.wait(*results)


@mock_swf
def test_task_naming():
    workflow = ATestTaskNaming
    executor = Executor(DOMAIN, workflow)

    history = builder.History(workflow, input={})

    decisions, _ = executor.replay(Response(history=history))
    expected = [
        # non idempotent task, should increment
        "activity-tests.data.activities.increment-1",
        # non idempotent task, should increment again
        "activity-tests.data.activities.increment-2",
        # idempotent task, with arg 1
        "activity-tests.data.activities.triple-bdc09455c37471e0ba7397350413a5e6",
        # idempotent task, with arg 2
        "activity-tests.data.activities.triple-12036b25db61ae6cadf7a003ff523029",
        # idempotent task, with arg 2 too => same task id
        "activity-tests.data.activities.triple-12036b25db61ae6cadf7a003ff523029",
        # class-based task, non idempotent
        "activity-tests.data.activities.Tetra-1",
    ]
    for i in range(0, len(expected)):
        decision = decisions[i]['scheduleActivityTaskDecisionAttributes']
        assert decision['activityId'] == expected[i]
