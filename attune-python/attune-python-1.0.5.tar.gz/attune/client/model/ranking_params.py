# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class RankingParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        """
        RankingParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entity_type': 'str',
            'entity_source': 'str',
            'ids': 'list[str]',
            'application': 'str',
            'ip': 'str',
            'customer': 'str',
            'view': 'str',
            'quantities': 'list[Int]',
            'anonymous': 'str',
            'user_agent': 'str',
            'scope': 'list[str]'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'entity_source': 'entitySource',
            'ids': 'ids',
            'application': 'application',
            'ip': 'ip',
            'customer': 'customer',
            'view': 'view',
            'quantities': 'quantities',
            'anonymous': 'anonymous',
            'user_agent': 'userAgent',
            'scope': 'scope'
        }

        self._entity_type = None
        self._entity_source = None
        self._ids = None
        self._application = None
        self._ip = None
        self._customer = None
        self._view = None
        self._quantities = None
        self._anonymous = None
        self._user_agent = None
        self._scope = None

    @property
    def entity_type(self):
        """
        Gets the entity_type of this RankingParams.


        :return: The entity_type of this RankingParams.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this RankingParams.


        :param entity_type: The entity_type of this RankingParams.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def entity_source(self):
        """
        Gets the entity_source of this RankingParams.


        :return: The entity_source of this RankingParams.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this RankingParams.


        :param entity_source: The entity_source of this RankingParams.
        :type: str
        """
        self._entity_source = entity_source

    @property
    def ids(self):
        """
        Gets the ids of this RankingParams.


        :return: The ids of this RankingParams.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """
        Sets the ids of this RankingParams.


        :param ids: The ids of this RankingParams.
        :type: list[str]
        """
        self._ids = ids

    @property
    def application(self):
        """
        Gets the application of this RankingParams.


        :return: The application of this RankingParams.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """
        Sets the application of this RankingParams.


        :param application: The application of this RankingParams.
        :type: str
        """
        self._application = application

    @property
    def ip(self):
        """
        Gets the ip of this RankingParams.


        :return: The ip of this RankingParams.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this RankingParams.


        :param ip: The ip of this RankingParams.
        :type: str
        """
        self._ip = ip

    @property
    def customer(self):
        """
        Gets the customer of this RankingParams.


        :return: The customer of this RankingParams.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this RankingParams.


        :param customer: The customer of this RankingParams.
        :type: str
        """
        self._customer = customer

    @property
    def view(self):
        """
        Gets the view of this RankingParams.


        :return: The view of this RankingParams.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this RankingParams.


        :param view: The view of this RankingParams.
        :type: str
        """
        self._view = view

    @property
    def quantities(self):
        """
        Gets the quantities of this RankingParams.


        :return: The quantities of this RankingParams.
        :rtype: list[Int]
        """
        return self._quantities

    @quantities.setter
    def quantities(self, quantities):
        """
        Sets the quantities of this RankingParams.


        :param quantities: The quantities of this RankingParams.
        :type: list[Int]
        """
        self._quantities = quantities

    @property
    def anonymous(self):
        """
        Gets the anonymous of this RankingParams.


        :return: The anonymous of this RankingParams.
        :rtype: str
        """
        return self._anonymous

    @anonymous.setter
    def anonymous(self, anonymous):
        """
        Sets the anonymous of this RankingParams.


        :param anonymous: The anonymous of this RankingParams.
        :type: str
        """
        self._anonymous = anonymous

    @property
    def user_agent(self):
        """
        Gets the user_agent of this RankingParams.


        :return: The user_agent of this RankingParams.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this RankingParams.


        :param user_agent: The user_agent of this RankingParams.
        :type: str
        """
        self._user_agent = user_agent

    @property
    def scope(self):
        """
        Gets the scope of this RankingParams.


        :return: The scope of this RankingParams.
        :rtype: list[ScopeEntry]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this RankingParams.


        :param scope: The scope of this RankingParams.
        :type: list[ScopeEntry]
        """
        self._scope = scope

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
