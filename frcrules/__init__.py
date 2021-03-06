# coding: utf-8

# flake8: noqa

"""
    Ruler API

    Ruler API is a flexible API for rules. Originally designed for FIRST Robotics Competition, it is flexible in nature to allow for any program to use it.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from frcrules.api.get_rule_api import GetRuleApi
from frcrules.api.get_rule_list_api import GetRuleListApi

# import ApiClient
from frcrules.api_client import ApiClient
from frcrules.configuration import Configuration
from frcrules.exceptions import OpenApiException
from frcrules.exceptions import ApiTypeError
from frcrules.exceptions import ApiValueError
from frcrules.exceptions import ApiKeyError
from frcrules.exceptions import ApiException
# import models into sdk package

