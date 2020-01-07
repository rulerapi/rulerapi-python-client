# openapi_client.GetRuleApi

All URIs are relative to *https://frcrules.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rule**](GetRuleApi.md#get_rule) | **GET** /rule/{rule_id} | 


# **get_rule**
> str get_rule(rule_id)



Returns the content of a rule.

### Example

```python
from __future__ import print_function
import time
import frcrules
from frcrules.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = frcrules.GetRuleApi()
rule_id = 'rule_id_example' # str | Rule ID to get

try:
    api_response = api_instance.get_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetRuleApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule ID to get | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

