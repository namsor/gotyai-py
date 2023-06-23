# coding: utf-8

"""
    Gotyai API v3

    Gotyai API : the Spartan explainable AI   # noqa: E501

    OpenAPI spec version: 3.0.2
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class APIPlanOut(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'plan_name': 'str',
        'plan_quota': 'int',
        'price': 'float',
        'price_overage': 'float'
    }

    attribute_map = {
        'plan_name': 'planName',
        'plan_quota': 'planQuota',
        'price': 'price',
        'price_overage': 'priceOverage'
    }

    def __init__(self, plan_name=None, plan_quota=None, price=None, price_overage=None):  # noqa: E501
        """APIPlanOut - a model defined in OpenAPI"""  # noqa: E501

        self._plan_name = None
        self._plan_quota = None
        self._price = None
        self._price_overage = None
        self.discriminator = None

        if plan_name is not None:
            self.plan_name = plan_name
        if plan_quota is not None:
            self.plan_quota = plan_quota
        if price is not None:
            self.price = price
        if price_overage is not None:
            self.price_overage = price_overage

    @property
    def plan_name(self):
        """Gets the plan_name of this APIPlanOut.  # noqa: E501

        The API Plan name.  # noqa: E501

        :return: The plan_name of this APIPlanOut.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this APIPlanOut.

        The API Plan name.  # noqa: E501

        :param plan_name: The plan_name of this APIPlanOut.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

    @property
    def plan_quota(self):
        """Gets the plan_quota of this APIPlanOut.  # noqa: E501

        The API Plan's include free quota in number of units (NB/ not in number of names).  # noqa: E501

        :return: The plan_quota of this APIPlanOut.  # noqa: E501
        :rtype: int
        """
        return self._plan_quota

    @plan_quota.setter
    def plan_quota(self, plan_quota):
        """Sets the plan_quota of this APIPlanOut.

        The API Plan's include free quota in number of units (NB/ not in number of names).  # noqa: E501

        :param plan_quota: The plan_quota of this APIPlanOut.  # noqa: E501
        :type: int
        """

        self._plan_quota = plan_quota

    @property
    def price(self):
        """Gets the price of this APIPlanOut.  # noqa: E501

        The API Plan monthly price.  # noqa: E501

        :return: The price of this APIPlanOut.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this APIPlanOut.

        The API Plan monthly price.  # noqa: E501

        :param price: The price of this APIPlanOut.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def price_overage(self):
        """Gets the price_overage of this APIPlanOut.  # noqa: E501

        The API Plan's overages (additional cost on top of free quota).  # noqa: E501

        :return: The price_overage of this APIPlanOut.  # noqa: E501
        :rtype: float
        """
        return self._price_overage

    @price_overage.setter
    def price_overage(self, price_overage):
        """Sets the price_overage of this APIPlanOut.

        The API Plan's overages (additional cost on top of free quota).  # noqa: E501

        :param price_overage: The price_overage of this APIPlanOut.  # noqa: E501
        :type: float
        """

        self._price_overage = price_overage

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, APIPlanOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other