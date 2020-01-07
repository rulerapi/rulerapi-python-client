# openapi_client.GetRuleListApi

All URIs are relative to *https://frcrules.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rules**](GetRuleListApi.md#get_rules) | **GET** /rules | 


# **get_rules**
> list[str] get_rules()



Returns the list of rules.

### Example

```python
from __future__ import print_function
import time
import frcrules
from frcrules.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = frcrules.GetRuleListApi()

try:
    api_response = api_instance.get_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetRuleListApi->get_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

