# openapi_client.model.create_invoice_data.CreateInvoiceData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**out** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of True
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**memo** | str,  | str,  |  | [optional] 
**unit** | str,  | str,  |  | [optional] if omitted the server will use the default value of "sat"
**description_hash** | str,  | str,  |  | [optional] 
**unhashed_description** | str,  | str,  |  | [optional] 
**expiry** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**lnurl_callback** | str,  | str,  |  | [optional] 
**lnurl_balance_check** | str,  | str,  |  | [optional] 
**[extra](#extra)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**webhook** | str,  | str,  |  | [optional] 
**internal** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**bolt11** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extra

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

