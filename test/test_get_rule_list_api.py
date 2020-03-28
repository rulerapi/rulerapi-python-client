# coding: utf-8

"""
    Ruler API

    Ruler API is a flexible API for rules. Originally designed for FIRST Robotics Competition, it is flexible in nature to allow for any program to use it.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import frcrules
from frcrules.api.get_rule_list_api import GetRuleListApi  # noqa: E501
from frcrules.rest import ApiException


class TestGetRuleListApi(unittest.TestCase):
    """GetRuleListApi unit test stubs"""

    def setUp(self):
        self.api = frcrules.api.get_rule_list_api.GetRuleListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_rules(self):
        """Test case for get_rules

        """
        result = self.api.get_rules()
        assert type(result) == list
        assert type(result[0]) == str


if __name__ == '__main__':
    unittest.main()
