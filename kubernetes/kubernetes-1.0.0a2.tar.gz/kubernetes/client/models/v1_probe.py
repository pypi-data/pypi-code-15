# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1Probe(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, failure_threshold=None, initial_delay_seconds=None, period_seconds=None, success_threshold=None, timeout_seconds=None):
        """
        V1Probe - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'failure_threshold': 'int',
            'initial_delay_seconds': 'int',
            'period_seconds': 'int',
            'success_threshold': 'int',
            'timeout_seconds': 'int'
        }

        self.attribute_map = {
            'failure_threshold': 'failureThreshold',
            'initial_delay_seconds': 'initialDelaySeconds',
            'period_seconds': 'periodSeconds',
            'success_threshold': 'successThreshold',
            'timeout_seconds': 'timeoutSeconds'
        }

        self._failure_threshold = failure_threshold
        self._initial_delay_seconds = initial_delay_seconds
        self._period_seconds = period_seconds
        self._success_threshold = success_threshold
        self._timeout_seconds = timeout_seconds


    @property
    def failure_threshold(self):
        """
        Gets the failure_threshold of this V1Probe.
        Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.

        :return: The failure_threshold of this V1Probe.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """
        Sets the failure_threshold of this V1Probe.
        Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.

        :param failure_threshold: The failure_threshold of this V1Probe.
        :type: int
        """

        self._failure_threshold = failure_threshold

    @property
    def initial_delay_seconds(self):
        """
        Gets the initial_delay_seconds of this V1Probe.
        Number of seconds after the container has started before liveness probes are initiated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :return: The initial_delay_seconds of this V1Probe.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        """
        Sets the initial_delay_seconds of this V1Probe.
        Number of seconds after the container has started before liveness probes are initiated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :param initial_delay_seconds: The initial_delay_seconds of this V1Probe.
        :type: int
        """

        self._initial_delay_seconds = initial_delay_seconds

    @property
    def period_seconds(self):
        """
        Gets the period_seconds of this V1Probe.
        How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.

        :return: The period_seconds of this V1Probe.
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        """
        Sets the period_seconds of this V1Probe.
        How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.

        :param period_seconds: The period_seconds of this V1Probe.
        :type: int
        """

        self._period_seconds = period_seconds

    @property
    def success_threshold(self):
        """
        Gets the success_threshold of this V1Probe.
        Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1.

        :return: The success_threshold of this V1Probe.
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """
        Sets the success_threshold of this V1Probe.
        Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1.

        :param success_threshold: The success_threshold of this V1Probe.
        :type: int
        """

        self._success_threshold = success_threshold

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this V1Probe.
        Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :return: The timeout_seconds of this V1Probe.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this V1Probe.
        Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes

        :param timeout_seconds: The timeout_seconds of this V1Probe.
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
