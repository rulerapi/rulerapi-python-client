# openapi_client.GetRuleApi

All URIs are relative to *https://frcrules.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rule**](GetRuleApi.md#get_rule) | **GET** /rule/{ruleset}/{rule_id} | 


# **get_rule**
> str get_rule(rule_id, ruleset)



Returns the content of a rule.

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
    api_instance = frcrules.GetRuleApi(api_client)
    rule_id = 'rule_id_example' # str | Rule ID to get
ruleset = 'ruleset_example' # str | The ruleset to look up the rule from.

    try:
        api_response = api_instance.get_rule(rule_id, ruleset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GetRuleApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule ID to get | 
 **ruleset** | **str**| The ruleset to look up the rule from. | 

### Return type

**str**

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

