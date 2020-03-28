# openapi_client.GetRuleListApi

All URIs are relative to *https://frcrules.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rules**](GetRuleListApi.md#get_rules) | **GET** /rules/{ruleset} | 


# **get_rules**
> list[str] get_rules(ruleset)



Returns the list of rules.

### Example

```python
from __future__ import print_function
import time
import frcrules
from frcrules.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with frcrules.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = frcrules.GetRuleListApi(api_client)
    ruleset = 'ruleset_example' # str | The ruleset to look up the rule from.

    try:
        api_response = api_instance.get_rules(ruleset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GetRuleListApi->get_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset** | **str**| The ruleset to look up the rule from. | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**304** | Not Modified - Use Local Cached Value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

