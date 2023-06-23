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


class SpamStatsOut(object):
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
        'spams': 'list[SpamEventOut]',
        'duration_millis': 'int',
        'spam': 'int',
        'non_spam': 'int'
    }

    attribute_map = {
        'spams': 'spams',
        'duration_millis': 'durationMillis',
        'spam': 'spam',
        'non_spam': 'nonSpam'
    }

    def __init__(self, spams=None, duration_millis=None, spam=None, non_spam=None):  # noqa: E501
        """SpamStatsOut - a model defined in OpenAPI"""  # noqa: E501

        self._spams = None
        self._duration_millis = None
        self._spam = None
        self._non_spam = None
        self.discriminator = None

        if spams is not None:
            self.spams = spams
        if duration_millis is not None:
            self.duration_millis = duration_millis
        if spam is not None:
            self.spam = spam
        if non_spam is not None:
            self.non_spam = non_spam

    @property
    def spams(self):
        """Gets the spams of this SpamStatsOut.  # noqa: E501


        :return: The spams of this SpamStatsOut.  # noqa: E501
        :rtype: list[SpamEventOut]
        """
        return self._spams

    @spams.setter
    def spams(self, spams):
        """Sets the spams of this SpamStatsOut.


        :param spams: The spams of this SpamStatsOut.  # noqa: E501
        :type: list[SpamEventOut]
        """

        self._spams = spams

    @property
    def duration_millis(self):
        """Gets the duration_millis of this SpamStatsOut.  # noqa: E501


        :return: The duration_millis of this SpamStatsOut.  # noqa: E501
        :rtype: int
        """
        return self._duration_millis

    @duration_millis.setter
    def duration_millis(self, duration_millis):
        """Sets the duration_millis of this SpamStatsOut.


        :param duration_millis: The duration_millis of this SpamStatsOut.  # noqa: E501
        :type: int
        """

        self._duration_millis = duration_millis

    @property
    def spam(self):
        """Gets the spam of this SpamStatsOut.  # noqa: E501


        :return: The spam of this SpamStatsOut.  # noqa: E501
        :rtype: int
        """
        return self._spam

    @spam.setter
    def spam(self, spam):
        """Sets the spam of this SpamStatsOut.


        :param spam: The spam of this SpamStatsOut.  # noqa: E501
        :type: int
        """

        self._spam = spam

    @property
    def non_spam(self):
        """Gets the non_spam of this SpamStatsOut.  # noqa: E501


        :return: The non_spam of this SpamStatsOut.  # noqa: E501
        :rtype: int
        """
        return self._non_spam

    @non_spam.setter
    def non_spam(self, non_spam):
        """Sets the non_spam of this SpamStatsOut.


        :param non_spam: The non_spam of this SpamStatsOut.  # noqa: E501
        :type: int
        """

        self._non_spam = non_spam

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
        if not isinstance(other, SpamStatsOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other