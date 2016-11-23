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


class V1beta1SubjectAccessReviewSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, extra=None, group=None, non_resource_attributes=None, resource_attributes=None, user=None):
        """
        V1beta1SubjectAccessReviewSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'extra': 'dict(str, list[str])',
            'group': 'list[str]',
            'non_resource_attributes': 'V1beta1NonResourceAttributes',
            'resource_attributes': 'V1beta1ResourceAttributes',
            'user': 'str'
        }

        self.attribute_map = {
            'extra': 'extra',
            'group': 'group',
            'non_resource_attributes': 'nonResourceAttributes',
            'resource_attributes': 'resourceAttributes',
            'user': 'user'
        }

        self._extra = extra
        self._group = group
        self._non_resource_attributes = non_resource_attributes
        self._resource_attributes = resource_attributes
        self._user = user


    @property
    def extra(self):
        """
        Gets the extra of this V1beta1SubjectAccessReviewSpec.
        Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.

        :return: The extra of this V1beta1SubjectAccessReviewSpec.
        :rtype: dict(str, list[str])
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """
        Sets the extra of this V1beta1SubjectAccessReviewSpec.
        Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.

        :param extra: The extra of this V1beta1SubjectAccessReviewSpec.
        :type: dict(str, list[str])
        """

        self._extra = extra

    @property
    def group(self):
        """
        Gets the group of this V1beta1SubjectAccessReviewSpec.
        Groups is the groups you're testing for.

        :return: The group of this V1beta1SubjectAccessReviewSpec.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this V1beta1SubjectAccessReviewSpec.
        Groups is the groups you're testing for.

        :param group: The group of this V1beta1SubjectAccessReviewSpec.
        :type: list[str]
        """

        self._group = group

    @property
    def non_resource_attributes(self):
        """
        Gets the non_resource_attributes of this V1beta1SubjectAccessReviewSpec.
        NonResourceAttributes describes information for a non-resource access request

        :return: The non_resource_attributes of this V1beta1SubjectAccessReviewSpec.
        :rtype: V1beta1NonResourceAttributes
        """
        return self._non_resource_attributes

    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes):
        """
        Sets the non_resource_attributes of this V1beta1SubjectAccessReviewSpec.
        NonResourceAttributes describes information for a non-resource access request

        :param non_resource_attributes: The non_resource_attributes of this V1beta1SubjectAccessReviewSpec.
        :type: V1beta1NonResourceAttributes
        """

        self._non_resource_attributes = non_resource_attributes

    @property
    def resource_attributes(self):
        """
        Gets the resource_attributes of this V1beta1SubjectAccessReviewSpec.
        ResourceAuthorizationAttributes describes information for a resource access request

        :return: The resource_attributes of this V1beta1SubjectAccessReviewSpec.
        :rtype: V1beta1ResourceAttributes
        """
        return self._resource_attributes

    @resource_attributes.setter
    def resource_attributes(self, resource_attributes):
        """
        Sets the resource_attributes of this V1beta1SubjectAccessReviewSpec.
        ResourceAuthorizationAttributes describes information for a resource access request

        :param resource_attributes: The resource_attributes of this V1beta1SubjectAccessReviewSpec.
        :type: V1beta1ResourceAttributes
        """

        self._resource_attributes = resource_attributes

    @property
    def user(self):
        """
        Gets the user of this V1beta1SubjectAccessReviewSpec.
        User is the user you're testing for. If you specify \"User\" but not \"Group\", then is it interpreted as \"What if User were not a member of any groups

        :return: The user of this V1beta1SubjectAccessReviewSpec.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1beta1SubjectAccessReviewSpec.
        User is the user you're testing for. If you specify \"User\" but not \"Group\", then is it interpreted as \"What if User were not a member of any groups

        :param user: The user of this V1beta1SubjectAccessReviewSpec.
        :type: str
        """

        self._user = user

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
