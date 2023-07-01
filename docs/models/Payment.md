# openapi_client.model.payment.Payment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**checking_id** | str,  | str,  |  | 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**wallet_id** | str,  | str,  |  | 
**preimage** | str,  | str,  |  | 
**fee** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**pending** | bool,  | BoolClass,  |  | 
**time** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**bolt11** | str,  | str,  |  | 
**payment_hash** | str,  | str,  |  | 
**memo** | str,  | str,  |  | [optional] 
**expiry** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[extra](#extra)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] if omitted the server will use the default value of {}
**webhook** | str,  | str,  |  | [optional] 
**webhook_status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extra

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | if omitted the server will use the default value of {}

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

