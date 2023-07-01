<a id="__pageTop"></a>
# openapi_client.apis.tags.core_api.CoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_delete_settings_admin_api_v1_settings_delete**](#api_delete_settings_admin_api_v1_settings_delete) | **delete** /admin/api/v1/settings/ | Api Delete Settings
[**api_download_backup_admin_api_v1_backup_get**](#api_download_backup_admin_api_v1_backup_get) | **get** /admin/api/v1/backup/ | Api Download Backup
[**api_fiat_as_sats_api_v1_conversion_post**](#api_fiat_as_sats_api_v1_conversion_post) | **post** /api/v1/conversion | Api Fiat As Sats
[**api_get_settings_admin_api_v1_settings_get**](#api_get_settings_admin_api_v1_settings_get) | **get** /admin/api/v1/settings/ | Api Get Settings
[**api_install_extension_api_v1_extension_post**](#api_install_extension_api_v1_extension_post) | **post** /api/v1/extension | Api Install Extension
[**api_list_currencies_available_api_v1_currencies_get**](#api_list_currencies_available_api_v1_currencies_get) | **get** /api/v1/currencies | Api List Currencies Available
[**api_lnurlscan_api_v1_lnurlscan_code_get**](#api_lnurlscan_api_v1_lnurlscan_code_get) | **get** /api/v1/lnurlscan/{code} | Api Lnurlscan
[**api_payment_api_v1_payments_payment_hash_get**](#api_payment_api_v1_payments_payment_hash_get) | **get** /api/v1/payments/{payment_hash} | Api Payment
[**api_payments_create_api_v1_payments_post**](#api_payments_create_api_v1_payments_post) | **post** /api/v1/payments | Api Payments Create
[**api_payments_decode_api_v1_payments_decode_post**](#api_payments_decode_api_v1_payments_decode_post) | **post** /api/v1/payments/decode | Api Payments Decode
[**api_payments_pay_lnurl_api_v1_payments_lnurl_post**](#api_payments_pay_lnurl_api_v1_payments_lnurl_post) | **post** /api/v1/payments/lnurl | Api Payments Pay Lnurl
[**api_payments_sse_api_v1_payments_sse_get**](#api_payments_sse_api_v1_payments_sse_get) | **get** /api/v1/payments/sse | Api Payments Sse
[**api_perform_lnurlauth_api_v1_lnurlauth_post**](#api_perform_lnurlauth_api_v1_lnurlauth_post) | **post** /api/v1/lnurlauth | Api Perform Lnurlauth
[**api_public_payment_longpolling_public_v1_payment_payment_hash_get**](#api_public_payment_longpolling_public_v1_payment_payment_hash_get) | **get** /public/v1/payment/{payment_hash} | Api Public Payment Longpolling
[**api_restart_server_admin_api_v1_restart_get**](#api_restart_server_admin_api_v1_restart_get) | **get** /admin/api/v1/restart/ | Api Restart Server
[**api_uninstall_extension_api_v1_extension_ext_id_delete**](#api_uninstall_extension_api_v1_extension_ext_id_delete) | **delete** /api/v1/extension/{ext_id} | Api Uninstall Extension
[**api_update_settings_admin_api_v1_settings_put**](#api_update_settings_admin_api_v1_settings_put) | **put** /admin/api/v1/settings/ | Api Update Settings
[**api_update_wallet_api_v1_wallet_new_name_put**](#api_update_wallet_api_v1_wallet_new_name_put) | **put** /api/v1/wallet/{new_name} | Api Update Wallet
[**api_wallet_api_v1_wallet_get**](#api_wallet_api_v1_wallet_get) | **get** /api/v1/wallet | Api Wallet
[**audit_admin_api_v1_audit_get**](#audit_admin_api_v1_audit_get) | **get** /admin/api/v1/audit | Audit
[**delete_extension_db_api_v1_extension_ext_id_db_delete**](#delete_extension_db_api_v1_extension_ext_id_db_delete) | **delete** /api/v1/extension/{ext_id}/db | Delete Extension Db
[**get_extension_release_api_v1_extension_release_org_repo_tag_name_get**](#get_extension_release_api_v1_extension_release_org_repo_tag_name_get) | **get** /api/v1/extension/release/{org}/{repo}/{tag_name} | Get Extension Release
[**get_extension_releases_api_v1_extension_ext_id_releases_get**](#get_extension_releases_api_v1_extension_ext_id_releases_get) | **get** /api/v1/extension/{ext_id}/releases | Get Extension Releases
[**health_api_v1_health_get**](#health_api_v1_health_get) | **get** /api/v1/health | Health
[**img_api_v1_qrcode_data_get**](#img_api_v1_qrcode_data_get) | **get** /api/v1/qrcode/{data} | Img
[**payment_list_api_v1_payments_get**](#payment_list_api_v1_payments_get) | **get** /api/v1/payments | get list of payments
[**payment_list_api_v1_payments_paginated_get**](#payment_list_api_v1_payments_paginated_get) | **get** /api/v1/payments/paginated | get paginated list of payments
[**tinyurl_api_v1_tinyurl_post**](#tinyurl_api_v1_tinyurl_post) | **post** /api/v1/tinyurl | Tinyurl
[**tinyurl_api_v1_tinyurl_tinyurl_id_delete**](#tinyurl_api_v1_tinyurl_tinyurl_id_delete) | **delete** /api/v1/tinyurl/{tinyurl_id} | Tinyurl
[**tinyurl_api_v1_tinyurl_tinyurl_id_get**](#tinyurl_api_v1_tinyurl_tinyurl_id_get) | **get** /api/v1/tinyurl/{tinyurl_id} | Tinyurl
[**tinyurl_t_tinyurl_id_get**](#tinyurl_t_tinyurl_id_get) | **get** /t/{tinyurl_id} | Tinyurl
[**topup_admin_api_v1_topup_put**](#topup_admin_api_v1_topup_put) | **put** /admin/api/v1/topup/ | Topup
[**websocket_update_get_api_v1_ws_item_id_data_get**](#websocket_update_get_api_v1_ws_item_id_data_get) | **get** /api/v1/ws/{item_id}/{data} | Websocket Update Get
[**websocket_update_post_api_v1_ws_item_id_post**](#websocket_update_post_api_v1_ws_item_id_post) | **post** /api/v1/ws/{item_id} | Websocket Update Post

# **api_delete_settings_admin_api_v1_settings_delete**
<a id="api_delete_settings_admin_api_v1_settings_delete"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_delete_settings_admin_api_v1_settings_delete(usr)

Api Delete Settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Api Delete Settings
        api_response = api_instance.api_delete_settings_admin_api_v1_settings_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_delete_settings_admin_api_v1_settings_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_delete_settings_admin_api_v1_settings_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_delete_settings_admin_api_v1_settings_delete.ApiResponseFor422) | Validation Error

#### api_delete_settings_admin_api_v1_settings_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_delete_settings_admin_api_v1_settings_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_download_backup_admin_api_v1_backup_get**
<a id="api_download_backup_admin_api_v1_backup_get"></a>
> api_download_backup_admin_api_v1_backup_get(usr)

Api Download Backup

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Api Download Backup
        api_response = api_instance.api_download_backup_admin_api_v1_backup_get(
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_download_backup_admin_api_v1_backup_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_download_backup_admin_api_v1_backup_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_download_backup_admin_api_v1_backup_get.ApiResponseFor422) | Validation Error

#### api_download_backup_admin_api_v1_backup_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_download_backup_admin_api_v1_backup_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_fiat_as_sats_api_v1_conversion_post**
<a id="api_fiat_as_sats_api_v1_conversion_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_fiat_as_sats_api_v1_conversion_post(conversion_data)

Api Fiat As Sats

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.conversion_data import ConversionData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    body = ConversionData(
        _from="sat",
        amount=3.14,
        to="usd",
    )
    try:
        # Api Fiat As Sats
        api_response = api_instance.api_fiat_as_sats_api_v1_conversion_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_fiat_as_sats_api_v1_conversion_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConversionData**](../../models/ConversionData.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_fiat_as_sats_api_v1_conversion_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_fiat_as_sats_api_v1_conversion_post.ApiResponseFor422) | Validation Error

#### api_fiat_as_sats_api_v1_conversion_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_fiat_as_sats_api_v1_conversion_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_get_settings_admin_api_v1_settings_get**
<a id="api_get_settings_admin_api_v1_settings_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_get_settings_admin_api_v1_settings_get(usr)

Api Get Settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Api Get Settings
        api_response = api_instance.api_get_settings_admin_api_v1_settings_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_get_settings_admin_api_v1_settings_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_get_settings_admin_api_v1_settings_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_get_settings_admin_api_v1_settings_get.ApiResponseFor422) | Validation Error

#### api_get_settings_admin_api_v1_settings_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_get_settings_admin_api_v1_settings_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_install_extension_api_v1_extension_post**
<a id="api_install_extension_api_v1_extension_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_install_extension_api_v1_extension_post(usrcreate_extension)

Api Install Extension

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.create_extension import CreateExtension
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    body = CreateExtension(
        ext_id="ext_id_example",
        archive="archive_example",
        source_repo="source_repo_example",
    )
    try:
        # Api Install Extension
        api_response = api_instance.api_install_extension_api_v1_extension_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_install_extension_api_v1_extension_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateExtension**](../../models/CreateExtension.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_install_extension_api_v1_extension_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_install_extension_api_v1_extension_post.ApiResponseFor422) | Validation Error

#### api_install_extension_api_v1_extension_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_install_extension_api_v1_extension_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_list_currencies_available_api_v1_currencies_get**
<a id="api_list_currencies_available_api_v1_currencies_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_list_currencies_available_api_v1_currencies_get()

Api List Currencies Available

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Api List Currencies Available
        api_response = api_instance.api_list_currencies_available_api_v1_currencies_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_list_currencies_available_api_v1_currencies_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_list_currencies_available_api_v1_currencies_get.ApiResponseFor200) | Successful Response

#### api_list_currencies_available_api_v1_currencies_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_lnurlscan_api_v1_lnurlscan_code_get**
<a id="api_lnurlscan_api_v1_lnurlscan_code_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_lnurlscan_api_v1_lnurlscan_code_get(code)

Api Lnurlscan

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'code': "code_example",
    }
    try:
        # Api Lnurlscan
        api_response = api_instance.api_lnurlscan_api_v1_lnurlscan_code_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_lnurlscan_api_v1_lnurlscan_code_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
code | CodeSchema | | 

# CodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_lnurlscan_api_v1_lnurlscan_code_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_lnurlscan_api_v1_lnurlscan_code_get.ApiResponseFor422) | Validation Error

#### api_lnurlscan_api_v1_lnurlscan_code_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_lnurlscan_api_v1_lnurlscan_code_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_payment_api_v1_payments_payment_hash_get**
<a id="api_payment_api_v1_payments_payment_hash_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_payment_api_v1_payments_payment_hash_get(payment_hash)

Api Payment

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'payment_hash': None,
    }
    header_params = {
    }
    try:
        # Api Payment
        api_response = api_instance.api_payment_api_v1_payments_payment_hash_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_payment_api_v1_payments_payment_hash_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'payment_hash': None,
    }
    header_params = {
        'X-Api-Key': "X-Api-Key_example",
    }
    try:
        # Api Payment
        api_response = api_instance.api_payment_api_v1_payments_payment_hash_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_payment_api_v1_payments_payment_hash_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Api-Key | XApiKeySchema | | optional

# XApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
payment_hash | PaymentHashSchema | | 

# PaymentHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_payment_api_v1_payments_payment_hash_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_payment_api_v1_payments_payment_hash_get.ApiResponseFor422) | Validation Error

#### api_payment_api_v1_payments_payment_hash_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_payment_api_v1_payments_payment_hash_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_payments_create_api_v1_payments_post**
<a id="api_payments_create_api_v1_payments_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_payments_create_api_v1_payments_post(create_invoice_data)

Api Payments Create

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.create_invoice_data import CreateInvoiceData
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateInvoiceData(
        out=True,
        amount=0.0,
        memo="memo_example",
        unit="sat",
        description_hash="description_hash_example",
        unhashed_description="unhashed_description_example",
        expiry=1,
        lnurl_callback="lnurl_callback_example",
        lnurl_balance_check="lnurl_balance_check_example",
        extra=dict(),
        webhook="webhook_example",
        internal=False,
        bolt11="bolt11_example",
    )
    try:
        # Api Payments Create
        api_response = api_instance.api_payments_create_api_v1_payments_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_payments_create_api_v1_payments_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInvoiceData**](../../models/CreateInvoiceData.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#api_payments_create_api_v1_payments_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#api_payments_create_api_v1_payments_post.ApiResponseFor422) | Validation Error

#### api_payments_create_api_v1_payments_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_payments_create_api_v1_payments_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_payments_decode_api_v1_payments_decode_post**
<a id="api_payments_decode_api_v1_payments_decode_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_payments_decode_api_v1_payments_decode_post(decode_payment)

Api Payments Decode

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.decode_payment import DecodePayment
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    body = DecodePayment(
        data="data_example",
    )
    try:
        # Api Payments Decode
        api_response = api_instance.api_payments_decode_api_v1_payments_decode_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_payments_decode_api_v1_payments_decode_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DecodePayment**](../../models/DecodePayment.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_payments_decode_api_v1_payments_decode_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_payments_decode_api_v1_payments_decode_post.ApiResponseFor422) | Validation Error

#### api_payments_decode_api_v1_payments_decode_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_payments_decode_api_v1_payments_decode_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_payments_pay_lnurl_api_v1_payments_lnurl_post**
<a id="api_payments_pay_lnurl_api_v1_payments_lnurl_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_payments_pay_lnurl_api_v1_payments_lnurl_post(create_lnurl_data)

Api Payments Pay Lnurl

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.create_lnurl_data import CreateLNURLData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateLNURLData(
        description_hash="description_hash_example",
        callback="callback_example",
        amount=1,
        comment="comment_example",
        description="description_example",
    )
    try:
        # Api Payments Pay Lnurl
        api_response = api_instance.api_payments_pay_lnurl_api_v1_payments_lnurl_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_payments_pay_lnurl_api_v1_payments_lnurl_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLNURLData**](../../models/CreateLNURLData.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_payments_pay_lnurl_api_v1_payments_lnurl_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_payments_pay_lnurl_api_v1_payments_lnurl_post.ApiResponseFor422) | Validation Error

#### api_payments_pay_lnurl_api_v1_payments_lnurl_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_payments_pay_lnurl_api_v1_payments_lnurl_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_payments_sse_api_v1_payments_sse_get**
<a id="api_payments_sse_api_v1_payments_sse_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_payments_sse_api_v1_payments_sse_get()

Api Payments Sse

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Api Payments Sse
        api_response = api_instance.api_payments_sse_api_v1_payments_sse_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_payments_sse_api_v1_payments_sse_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_payments_sse_api_v1_payments_sse_get.ApiResponseFor200) | Successful Response

#### api_payments_sse_api_v1_payments_sse_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_perform_lnurlauth_api_v1_lnurlauth_post**
<a id="api_perform_lnurlauth_api_v1_lnurlauth_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_perform_lnurlauth_api_v1_lnurlauth_post(create_lnurl_auth)

Api Perform Lnurlauth

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.create_lnurl_auth import CreateLnurlAuth
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateLnurlAuth(
        callback="callback_example",
    )
    try:
        # Api Perform Lnurlauth
        api_response = api_instance.api_perform_lnurlauth_api_v1_lnurlauth_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_perform_lnurlauth_api_v1_lnurlauth_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLnurlAuth**](../../models/CreateLnurlAuth.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_perform_lnurlauth_api_v1_lnurlauth_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_perform_lnurlauth_api_v1_lnurlauth_post.ApiResponseFor422) | Validation Error

#### api_perform_lnurlauth_api_v1_lnurlauth_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_perform_lnurlauth_api_v1_lnurlauth_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_public_payment_longpolling_public_v1_payment_payment_hash_get**
<a id="api_public_payment_longpolling_public_v1_payment_payment_hash_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_public_payment_longpolling_public_v1_payment_payment_hash_get(payment_hash)

Api Public Payment Longpolling

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'payment_hash': None,
    }
    try:
        # Api Public Payment Longpolling
        api_response = api_instance.api_public_payment_longpolling_public_v1_payment_payment_hash_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_public_payment_longpolling_public_v1_payment_payment_hash_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
payment_hash | PaymentHashSchema | | 

# PaymentHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_public_payment_longpolling_public_v1_payment_payment_hash_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_public_payment_longpolling_public_v1_payment_payment_hash_get.ApiResponseFor422) | Validation Error

#### api_public_payment_longpolling_public_v1_payment_payment_hash_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_public_payment_longpolling_public_v1_payment_payment_hash_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_restart_server_admin_api_v1_restart_get**
<a id="api_restart_server_admin_api_v1_restart_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_restart_server_admin_api_v1_restart_get(usr)

Api Restart Server

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Api Restart Server
        api_response = api_instance.api_restart_server_admin_api_v1_restart_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_restart_server_admin_api_v1_restart_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_restart_server_admin_api_v1_restart_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_restart_server_admin_api_v1_restart_get.ApiResponseFor422) | Validation Error

#### api_restart_server_admin_api_v1_restart_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_restart_server_admin_api_v1_restart_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_uninstall_extension_api_v1_extension_ext_id_delete**
<a id="api_uninstall_extension_api_v1_extension_ext_id_delete"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_uninstall_extension_api_v1_extension_ext_id_delete(ext_idusr)

Api Uninstall Extension

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ext_id': "ext_id_example",
    }
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Api Uninstall Extension
        api_response = api_instance.api_uninstall_extension_api_v1_extension_ext_id_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_uninstall_extension_api_v1_extension_ext_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ext_id | ExtIdSchema | | 

# ExtIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_uninstall_extension_api_v1_extension_ext_id_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_uninstall_extension_api_v1_extension_ext_id_delete.ApiResponseFor422) | Validation Error

#### api_uninstall_extension_api_v1_extension_ext_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_uninstall_extension_api_v1_extension_ext_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_update_settings_admin_api_v1_settings_put**
<a id="api_update_settings_admin_api_v1_settings_put"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_update_settings_admin_api_v1_settings_put(usreditable_settings)

Api Update Settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.editable_settings import EditableSettings
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    body = EditableSettings(
        lightning_invoice_expiry=600,
        boltz_network="main",
        boltz_url="https://boltz.exchange/api",
        boltz_mempool_space_url="https://mempool.space",
        boltz_mempool_space_url_ws="wss://mempool.space",
        lntips_api_endpoint="lntips_api_endpoint_example",
        lntips_api_key="lntips_api_key_example",
        lntips_admin_key="lntips_admin_key_example",
        lntips_invoice_key="lntips_invoice_key_example",
        spark_url="spark_url_example",
        spark_token="spark_token_example",
        opennode_api_endpoint="opennode_api_endpoint_example",
        opennode_key="opennode_key_example",
        opennode_admin_key="opennode_admin_key_example",
        opennode_invoice_key="opennode_invoice_key_example",
        lnpay_api_endpoint="lnpay_api_endpoint_example",
        lnpay_api_key="lnpay_api_key_example",
        lnpay_wallet_key="lnpay_wallet_key_example",
        lnpay_admin_key="lnpay_admin_key_example",
        lnd_grpc_endpoint="lnd_grpc_endpoint_example",
        lnd_grpc_cert="lnd_grpc_cert_example",
        lnd_grpc_port=1,
        lnd_grpc_admin_macaroon="lnd_grpc_admin_macaroon_example",
        lnd_grpc_invoice_macaroon="lnd_grpc_invoice_macaroon_example",
        lnd_grpc_macaroon="lnd_grpc_macaroon_example",
        lnd_grpc_macaroon_encrypted="lnd_grpc_macaroon_encrypted_example",
        lnd_rest_endpoint="lnd_rest_endpoint_example",
        lnd_rest_cert="lnd_rest_cert_example",
        lnd_rest_macaroon="lnd_rest_macaroon_example",
        lnd_rest_macaroon_encrypted="lnd_rest_macaroon_encrypted_example",
        lnd_cert="lnd_cert_example",
        lnd_admin_macaroon="lnd_admin_macaroon_example",
        lnd_invoice_macaroon="lnd_invoice_macaroon_example",
        lnd_rest_admin_macaroon="lnd_rest_admin_macaroon_example",
        lnd_rest_invoice_macaroon="lnd_rest_invoice_macaroon_example",
        eclair_url="eclair_url_example",
        eclair_pass="eclair_pass_example",
        corelightning_rpc="corelightning_rpc_example",
        clightning_rpc="clightning_rpc_example",
        cliche_endpoint="cliche_endpoint_example",
        lnbits_endpoint="https://legend.lnbits.com",
        lnbits_key="lnbits_key_example",
        lnbits_admin_key="lnbits_admin_key_example",
        lnbits_invoice_key="lnbits_invoice_key_example",
        fake_wallet_secret="ToTheMoon1",
        lnbits_backend_wallet_class="VoidWallet",
        lnbits_rate_limit_no="200",
        lnbits_rate_limit_unit="minute",
        lnbits_allowed_ips=[],
        lnbits_blocked_ips=[],
        lnbits_notifications=False,
        lnbits_killswitch=False,
        lnbits_killswitch_interval=60,
        lnbits_watchdog=False,
        lnbits_watchdog_interval=60,
        lnbits_watchdog_delta=1000000,
        lnbits_status_manifest="https://raw.githubusercontent.com/lnbits/lnbits-status/main/manifest.json",
        lnbits_baseurl="http://127.0.0.1:5000/",
        lnbits_reserve_fee_min=2000,
        lnbits_reserve_fee_percent=1.0,
        lnbits_service_fee=0,
        lnbits_hide_api=False,
        lnbits_denomination="sats",
        lnbits_site_title="LNbits",
        lnbits_site_tagline="free and open-source lightning wallet",
        lnbits_site_description="lnbits_site_description_example",
        lnbits_default_wallet_name="LNbits wallet",
        lnbits_theme_options=["classic","freedom","mint","salvador","monochrome","autumn","cyber"],
        lnbits_custom_logo="lnbits_custom_logo_example",
        lnbits_ad_space_title="Supported by",
        lnbits_ad_space="https://shop.lnbits.com/;/static/images/lnbits-shop-light.png;/static/images/lnbits-shop-dark.png",
        lnbits_ad_space_enabled=False,
        lnbits_allowed_currencies=[],
        lnbits_admin_extensions=[],
        lnbits_extensions_manifests=["https://raw.githubusercontent.com/lnbits/lnbits-extensions/main/extensions.json"],
        lnbits_admin_users=[],
        lnbits_allowed_users=[],
    )
    try:
        # Api Update Settings
        api_response = api_instance.api_update_settings_admin_api_v1_settings_put(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_update_settings_admin_api_v1_settings_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditableSettings**](../../models/EditableSettings.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_update_settings_admin_api_v1_settings_put.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_update_settings_admin_api_v1_settings_put.ApiResponseFor422) | Validation Error

#### api_update_settings_admin_api_v1_settings_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_update_settings_admin_api_v1_settings_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_update_wallet_api_v1_wallet_new_name_put**
<a id="api_update_wallet_api_v1_wallet_new_name_put"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_update_wallet_api_v1_wallet_new_name_put(new_name)

Api Update Wallet

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'new_name': "new_name_example",
    }
    try:
        # Api Update Wallet
        api_response = api_instance.api_update_wallet_api_v1_wallet_new_name_put(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_update_wallet_api_v1_wallet_new_name_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
new_name | NewNameSchema | | 

# NewNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_update_wallet_api_v1_wallet_new_name_put.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#api_update_wallet_api_v1_wallet_new_name_put.ApiResponseFor422) | Validation Error

#### api_update_wallet_api_v1_wallet_new_name_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### api_update_wallet_api_v1_wallet_new_name_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_wallet_api_v1_wallet_get**
<a id="api_wallet_api_v1_wallet_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type api_wallet_api_v1_wallet_get()

Api Wallet

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Api Wallet
        api_response = api_instance.api_wallet_api_v1_wallet_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->api_wallet_api_v1_wallet_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_wallet_api_v1_wallet_get.ApiResponseFor200) | Successful Response

#### api_wallet_api_v1_wallet_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **audit_admin_api_v1_audit_get**
<a id="audit_admin_api_v1_audit_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type audit_admin_api_v1_audit_get(usr)

Audit

show the current balance of the node and the LNbits database

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Audit
        api_response = api_instance.audit_admin_api_v1_audit_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->audit_admin_api_v1_audit_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#audit_admin_api_v1_audit_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#audit_admin_api_v1_audit_get.ApiResponseFor422) | Validation Error

#### audit_admin_api_v1_audit_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### audit_admin_api_v1_audit_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_extension_db_api_v1_extension_ext_id_db_delete**
<a id="delete_extension_db_api_v1_extension_ext_id_db_delete"></a>
> bool, date, datetime, dict, float, int, list, str, none_type delete_extension_db_api_v1_extension_ext_id_db_delete(ext_idusr)

Delete Extension Db

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ext_id': "ext_id_example",
    }
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Delete Extension Db
        api_response = api_instance.delete_extension_db_api_v1_extension_ext_id_db_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->delete_extension_db_api_v1_extension_ext_id_db_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ext_id | ExtIdSchema | | 

# ExtIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_extension_db_api_v1_extension_ext_id_db_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_extension_db_api_v1_extension_ext_id_db_delete.ApiResponseFor422) | Validation Error

#### delete_extension_db_api_v1_extension_ext_id_db_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### delete_extension_db_api_v1_extension_ext_id_db_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_extension_release_api_v1_extension_release_org_repo_tag_name_get**
<a id="get_extension_release_api_v1_extension_release_org_repo_tag_name_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_extension_release_api_v1_extension_release_org_repo_tag_name_get(orgrepotag_nameusr)

Get Extension Release

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'org': "org_example",
        'repo': "repo_example",
        'tag_name': "tag_name_example",
    }
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Get Extension Release
        api_response = api_instance.get_extension_release_api_v1_extension_release_org_repo_tag_name_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->get_extension_release_api_v1_extension_release_org_repo_tag_name_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
org | OrgSchema | | 
repo | RepoSchema | | 
tag_name | TagNameSchema | | 

# OrgSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RepoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_extension_release_api_v1_extension_release_org_repo_tag_name_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_extension_release_api_v1_extension_release_org_repo_tag_name_get.ApiResponseFor422) | Validation Error

#### get_extension_release_api_v1_extension_release_org_repo_tag_name_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_extension_release_api_v1_extension_release_org_repo_tag_name_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_extension_releases_api_v1_extension_ext_id_releases_get**
<a id="get_extension_releases_api_v1_extension_ext_id_releases_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_extension_releases_api_v1_extension_ext_id_releases_get(ext_idusr)

Get Extension Releases

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ext_id': "ext_id_example",
    }
    query_params = {
        'usr': "usr_example",
    }
    try:
        # Get Extension Releases
        api_response = api_instance.get_extension_releases_api_v1_extension_ext_id_releases_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->get_extension_releases_api_v1_extension_ext_id_releases_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ext_id | ExtIdSchema | | 

# ExtIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_extension_releases_api_v1_extension_ext_id_releases_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_extension_releases_api_v1_extension_ext_id_releases_get.ApiResponseFor422) | Validation Error

#### get_extension_releases_api_v1_extension_ext_id_releases_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_extension_releases_api_v1_extension_ext_id_releases_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **health_api_v1_health_get**
<a id="health_api_v1_health_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type health_api_v1_health_get()

Health

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health
        api_response = api_instance.health_api_v1_health_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->health_api_v1_health_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#health_api_v1_health_get.ApiResponseFor200) | Successful Response

#### health_api_v1_health_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **img_api_v1_qrcode_data_get**
<a id="img_api_v1_qrcode_data_get"></a>
> img_api_v1_qrcode_data_get(data)

Img

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'data': None,
    }
    try:
        # Img
        api_response = api_instance.img_api_v1_qrcode_data_get(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->img_api_v1_qrcode_data_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data | DataSchema | | 

# DataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#img_api_v1_qrcode_data_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#img_api_v1_qrcode_data_get.ApiResponseFor422) | Validation Error

#### img_api_v1_qrcode_data_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### img_api_v1_qrcode_data_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **payment_list_api_v1_payments_get**
<a id="payment_list_api_v1_payments_get"></a>
> [Payment] payment_list_api_v1_payments_get()

get list of payments

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.payment import Payment
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'offset': 1,
        'sortby': "sortby_example",
        'direction': "asc",
        'search': "search_example",
        'checking_id': "checking_id_example",
        'amount': 1,
        'fee': 1,
        'memo': "memo_example",
        'time': "1970-01-01T00:00:00.00Z",
        'bolt11': "bolt11_example",
        'preimage': "preimage_example",
        'payment_hash': "payment_hash_example",
        'expiry': "1970-01-01T00:00:00.00Z",
        'extra': dict(),
        'wallet_id': "wallet_id_example",
        'webhook': "webhook_example",
        'webhook_status': 1,
    }
    try:
        # get list of payments
        api_response = api_instance.payment_list_api_v1_payments_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->payment_list_api_v1_payments_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
sortby | SortbySchema | | optional
direction | DirectionSchema | | optional
search | SearchSchema | | optional
checking_id | CheckingIdSchema | | optional
amount | AmountSchema | | optional
fee | FeeSchema | | optional
memo | MemoSchema | | optional
time | TimeSchema | | optional
bolt11 | Bolt11Schema | | optional
preimage | PreimageSchema | | optional
payment_hash | PaymentHashSchema | | optional
expiry | ExpirySchema | | optional
extra | ExtraSchema | | optional
wallet_id | WalletIdSchema | | optional
webhook | WebhookSchema | | optional
webhook_status | WebhookStatusSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortbySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# SearchSchema

Text based search

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Text based search | 

# CheckingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AmountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MemoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# Bolt11Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PreimageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaymentHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ExpirySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# ExtraSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | if omitted the server will use the default value of {}

# WalletIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WebhookSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WebhookStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#payment_list_api_v1_payments_get.ApiResponseFor200) | list of payments
422 | [ApiResponseFor422](#payment_list_api_v1_payments_get.ApiResponseFor422) | Validation Error

#### payment_list_api_v1_payments_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Payment**]({{complexTypePrefix}}Payment.md) | [**Payment**]({{complexTypePrefix}}Payment.md) | [**Payment**]({{complexTypePrefix}}Payment.md) |  | 

#### payment_list_api_v1_payments_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **payment_list_api_v1_payments_paginated_get**
<a id="payment_list_api_v1_payments_paginated_get"></a>
> Page payment_list_api_v1_payments_paginated_get()

get paginated list of payments

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'offset': 1,
        'sortby': "sortby_example",
        'direction': "asc",
        'search': "search_example",
        'checking_id': "checking_id_example",
        'amount': 1,
        'fee': 1,
        'memo': "memo_example",
        'time': "1970-01-01T00:00:00.00Z",
        'bolt11': "bolt11_example",
        'preimage': "preimage_example",
        'payment_hash': "payment_hash_example",
        'expiry': "1970-01-01T00:00:00.00Z",
        'extra': dict(),
        'wallet_id': "wallet_id_example",
        'webhook': "webhook_example",
        'webhook_status': 1,
    }
    try:
        # get paginated list of payments
        api_response = api_instance.payment_list_api_v1_payments_paginated_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->payment_list_api_v1_payments_paginated_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
sortby | SortbySchema | | optional
direction | DirectionSchema | | optional
search | SearchSchema | | optional
checking_id | CheckingIdSchema | | optional
amount | AmountSchema | | optional
fee | FeeSchema | | optional
memo | MemoSchema | | optional
time | TimeSchema | | optional
bolt11 | Bolt11Schema | | optional
preimage | PreimageSchema | | optional
payment_hash | PaymentHashSchema | | optional
expiry | ExpirySchema | | optional
extra | ExtraSchema | | optional
wallet_id | WalletIdSchema | | optional
webhook | WebhookSchema | | optional
webhook_status | WebhookStatusSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortbySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# SearchSchema

Text based search

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Text based search | 

# CheckingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AmountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MemoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# Bolt11Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PreimageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaymentHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ExpirySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# ExtraSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | if omitted the server will use the default value of {}

# WalletIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WebhookSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WebhookStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#payment_list_api_v1_payments_paginated_get.ApiResponseFor200) | list of payments
422 | [ApiResponseFor422](#payment_list_api_v1_payments_paginated_get.ApiResponseFor422) | Validation Error

#### payment_list_api_v1_payments_paginated_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Page**](../../models/Page.md) |  | 


#### payment_list_api_v1_payments_paginated_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tinyurl_api_v1_tinyurl_post**
<a id="tinyurl_api_v1_tinyurl_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type tinyurl_api_v1_tinyurl_post(url)

Tinyurl

creates a tinyurl

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'url': "url_example",
    }
    try:
        # Tinyurl
        api_response = api_instance.tinyurl_api_v1_tinyurl_post(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->tinyurl_api_v1_tinyurl_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'url': "url_example",
        'endless': False,
    }
    try:
        # Tinyurl
        api_response = api_instance.tinyurl_api_v1_tinyurl_post(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->tinyurl_api_v1_tinyurl_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
url | UrlSchema | | 
endless | EndlessSchema | | optional


# UrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndlessSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tinyurl_api_v1_tinyurl_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#tinyurl_api_v1_tinyurl_post.ApiResponseFor422) | Validation Error

#### tinyurl_api_v1_tinyurl_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### tinyurl_api_v1_tinyurl_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tinyurl_api_v1_tinyurl_tinyurl_id_delete**
<a id="tinyurl_api_v1_tinyurl_tinyurl_id_delete"></a>
> bool, date, datetime, dict, float, int, list, str, none_type tinyurl_api_v1_tinyurl_tinyurl_id_delete(tinyurl_id)

Tinyurl

delete a tinyurl by id

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'tinyurl_id': "tinyurl_id_example",
    }
    try:
        # Tinyurl
        api_response = api_instance.tinyurl_api_v1_tinyurl_tinyurl_id_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->tinyurl_api_v1_tinyurl_tinyurl_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tinyurl_id | TinyurlIdSchema | | 

# TinyurlIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tinyurl_api_v1_tinyurl_tinyurl_id_delete.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#tinyurl_api_v1_tinyurl_tinyurl_id_delete.ApiResponseFor422) | Validation Error

#### tinyurl_api_v1_tinyurl_tinyurl_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### tinyurl_api_v1_tinyurl_tinyurl_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tinyurl_api_v1_tinyurl_tinyurl_id_get**
<a id="tinyurl_api_v1_tinyurl_tinyurl_id_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type tinyurl_api_v1_tinyurl_tinyurl_id_get(tinyurl_id)

Tinyurl

get a tinyurl by id

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (APIKeyQuery):
```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: APIKeyQuery
configuration.api_key['APIKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyQuery'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'tinyurl_id': "tinyurl_id_example",
    }
    try:
        # Tinyurl
        api_response = api_instance.tinyurl_api_v1_tinyurl_tinyurl_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->tinyurl_api_v1_tinyurl_tinyurl_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tinyurl_id | TinyurlIdSchema | | 

# TinyurlIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tinyurl_api_v1_tinyurl_tinyurl_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#tinyurl_api_v1_tinyurl_tinyurl_id_get.ApiResponseFor422) | Validation Error

#### tinyurl_api_v1_tinyurl_tinyurl_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### tinyurl_api_v1_tinyurl_tinyurl_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader), [APIKeyQuery](../../../README.md#APIKeyQuery)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tinyurl_t_tinyurl_id_get**
<a id="tinyurl_t_tinyurl_id_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type tinyurl_t_tinyurl_id_get(tinyurl_id)

Tinyurl

redirects a tinyurl by id

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'tinyurl_id': "tinyurl_id_example",
    }
    try:
        # Tinyurl
        api_response = api_instance.tinyurl_t_tinyurl_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->tinyurl_t_tinyurl_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tinyurl_id | TinyurlIdSchema | | 

# TinyurlIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tinyurl_t_tinyurl_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#tinyurl_t_tinyurl_id_get.ApiResponseFor422) | Validation Error

#### tinyurl_t_tinyurl_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### tinyurl_t_tinyurl_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **topup_admin_api_v1_topup_put**
<a id="topup_admin_api_v1_topup_put"></a>
> bool, date, datetime, dict, float, int, list, str, none_type topup_admin_api_v1_topup_put(usrcreate_topup)

Topup

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.create_topup import CreateTopup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'usr': "usr_example",
    }
    body = CreateTopup(
        wallet_id="wallet_id_example",
        amount=1,
    )
    try:
        # Topup
        api_response = api_instance.topup_admin_api_v1_topup_put(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->topup_admin_api_v1_topup_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTopup**](../../models/CreateTopup.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
usr | UsrSchema | | 


# UsrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#topup_admin_api_v1_topup_put.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#topup_admin_api_v1_topup_put.ApiResponseFor422) | Validation Error

#### topup_admin_api_v1_topup_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### topup_admin_api_v1_topup_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **websocket_update_get_api_v1_ws_item_id_data_get**
<a id="websocket_update_get_api_v1_ws_item_id_data_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type websocket_update_get_api_v1_ws_item_id_data_get(item_iddata)

Websocket Update Get

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'item_id': "item_id_example",
        'data': "data_example",
    }
    try:
        # Websocket Update Get
        api_response = api_instance.websocket_update_get_api_v1_ws_item_id_data_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->websocket_update_get_api_v1_ws_item_id_data_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
item_id | ItemIdSchema | | 
data | DataSchema | | 

# ItemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#websocket_update_get_api_v1_ws_item_id_data_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#websocket_update_get_api_v1_ws_item_id_data_get.ApiResponseFor422) | Validation Error

#### websocket_update_get_api_v1_ws_item_id_data_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### websocket_update_get_api_v1_ws_item_id_data_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **websocket_update_post_api_v1_ws_item_id_post**
<a id="websocket_update_post_api_v1_ws_item_id_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type websocket_update_post_api_v1_ws_item_id_post(item_iddata)

Websocket Update Post

### Example

```python
import openapi_client
from openapi_client.apis.tags import core_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core_api.CoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'item_id': "item_id_example",
    }
    query_params = {
        'data': "data_example",
    }
    try:
        # Websocket Update Post
        api_response = api_instance.websocket_update_post_api_v1_ws_item_id_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CoreApi->websocket_update_post_api_v1_ws_item_id_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data | DataSchema | | 


# DataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
item_id | ItemIdSchema | | 

# ItemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#websocket_update_post_api_v1_ws_item_id_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#websocket_update_post_api_v1_ws_item_id_post.ApiResponseFor422) | Validation Error

#### websocket_update_post_api_v1_ws_item_id_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### websocket_update_post_api_v1_ws_item_id_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

