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


class V1beta1HorizontalPodAutoscaler(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, metadata=None, spec=None, status=None):
        """
        V1beta1HorizontalPodAutoscaler - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metadata': 'V1ObjectMeta',
            'spec': 'V1beta1HorizontalPodAutoscalerSpec',
            'status': 'V1beta1HorizontalPodAutoscalerStatus'
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'spec': 'spec',
            'status': 'status'
        }

        self._metadata = metadata
        self._spec = spec
        self._status = status


    @property
    def metadata(self):
        """
        Gets the metadata of this V1beta1HorizontalPodAutoscaler.
        Standard object metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1beta1HorizontalPodAutoscaler.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1beta1HorizontalPodAutoscaler.
        Standard object metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1beta1HorizontalPodAutoscaler.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self):
        """
        Gets the spec of this V1beta1HorizontalPodAutoscaler.
        behaviour of autoscaler. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status.

        :return: The spec of this V1beta1HorizontalPodAutoscaler.
        :rtype: V1beta1HorizontalPodAutoscalerSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """
        Sets the spec of this V1beta1HorizontalPodAutoscaler.
        behaviour of autoscaler. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status.

        :param spec: The spec of this V1beta1HorizontalPodAutoscaler.
        :type: V1beta1HorizontalPodAutoscalerSpec
        """

        self._spec = spec

    @property
    def status(self):
        """
        Gets the status of this V1beta1HorizontalPodAutoscaler.
        current information about the autoscaler.

        :return: The status of this V1beta1HorizontalPodAutoscaler.
        :rtype: V1beta1HorizontalPodAutoscalerStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1beta1HorizontalPodAutoscaler.
        current information about the autoscaler.

        :param status: The status of this V1beta1HorizontalPodAutoscaler.
        :type: V1beta1HorizontalPodAutoscalerStatus
        """

        self._status = status

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
