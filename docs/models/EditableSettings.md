# openapi_client.model.editable_settings.EditableSettings

Base class for settings, allowing values to be overridden by environment variables.  This is useful in production for secrets you do not wish to save in code, it plays nicely with docker(-compose), Heroku and any 12 factor app design.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Base class for settings, allowing values to be overridden by environment variables.  This is useful in production for secrets you do not wish to save in code, it plays nicely with docker(-compose), Heroku and any 12 factor app design. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**lightning_invoice_expiry** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 600
**boltz_network** | str,  | str,  |  | [optional] if omitted the server will use the default value of "main"
**boltz_url** | str,  | str,  |  | [optional] if omitted the server will use the default value of "https://boltz.exchange/api"
**boltz_mempool_space_url** | str,  | str,  |  | [optional] if omitted the server will use the default value of "https://mempool.space"
**boltz_mempool_space_url_ws** | str,  | str,  |  | [optional] if omitted the server will use the default value of "wss://mempool.space"
**lntips_api_endpoint** | str,  | str,  |  | [optional] 
**lntips_api_key** | str,  | str,  |  | [optional] 
**lntips_admin_key** | str,  | str,  |  | [optional] 
**lntips_invoice_key** | str,  | str,  |  | [optional] 
**spark_url** | str,  | str,  |  | [optional] 
**spark_token** | str,  | str,  |  | [optional] 
**opennode_api_endpoint** | str,  | str,  |  | [optional] 
**opennode_key** | str,  | str,  |  | [optional] 
**opennode_admin_key** | str,  | str,  |  | [optional] 
**opennode_invoice_key** | str,  | str,  |  | [optional] 
**lnpay_api_endpoint** | str,  | str,  |  | [optional] 
**lnpay_api_key** | str,  | str,  |  | [optional] 
**lnpay_wallet_key** | str,  | str,  |  | [optional] 
**lnpay_admin_key** | str,  | str,  |  | [optional] 
**lnd_grpc_endpoint** | str,  | str,  |  | [optional] 
**lnd_grpc_cert** | str,  | str,  |  | [optional] 
**lnd_grpc_port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**lnd_grpc_admin_macaroon** | str,  | str,  |  | [optional] 
**lnd_grpc_invoice_macaroon** | str,  | str,  |  | [optional] 
**lnd_grpc_macaroon** | str,  | str,  |  | [optional] 
**lnd_grpc_macaroon_encrypted** | str,  | str,  |  | [optional] 
**lnd_rest_endpoint** | str,  | str,  |  | [optional] 
**lnd_rest_cert** | str,  | str,  |  | [optional] 
**lnd_rest_macaroon** | str,  | str,  |  | [optional] 
**lnd_rest_macaroon_encrypted** | str,  | str,  |  | [optional] 
**lnd_cert** | str,  | str,  |  | [optional] 
**lnd_admin_macaroon** | str,  | str,  |  | [optional] 
**lnd_invoice_macaroon** | str,  | str,  |  | [optional] 
**lnd_rest_admin_macaroon** | str,  | str,  |  | [optional] 
**lnd_rest_invoice_macaroon** | str,  | str,  |  | [optional] 
**eclair_url** | str,  | str,  |  | [optional] 
**eclair_pass** | str,  | str,  |  | [optional] 
**corelightning_rpc** | str,  | str,  |  | [optional] 
**clightning_rpc** | str,  | str,  |  | [optional] 
**cliche_endpoint** | str,  | str,  |  | [optional] 
**lnbits_endpoint** | str,  | str,  |  | [optional] if omitted the server will use the default value of "https://legend.lnbits.com"
**lnbits_key** | str,  | str,  |  | [optional] 
**lnbits_admin_key** | str,  | str,  |  | [optional] 
**lnbits_invoice_key** | str,  | str,  |  | [optional] 
**fake_wallet_secret** | str,  | str,  |  | [optional] if omitted the server will use the default value of "ToTheMoon1"
**lnbits_backend_wallet_class** | str,  | str,  |  | [optional] if omitted the server will use the default value of "VoidWallet"
**lnbits_rate_limit_no** | str,  | str,  |  | [optional] if omitted the server will use the default value of "200"
**lnbits_rate_limit_unit** | str,  | str,  |  | [optional] if omitted the server will use the default value of "minute"
**[lnbits_allowed_ips](#lnbits_allowed_ips)** | list, tuple,  | tuple,  |  | [optional] 
**[lnbits_blocked_ips](#lnbits_blocked_ips)** | list, tuple,  | tuple,  |  | [optional] 
**lnbits_notifications** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**lnbits_killswitch** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**lnbits_killswitch_interval** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 60
**lnbits_watchdog** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**lnbits_watchdog_interval** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 60
**lnbits_watchdog_delta** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 1000000
**lnbits_status_manifest** | str,  | str,  |  | [optional] if omitted the server will use the default value of "https://raw.githubusercontent.com/lnbits/lnbits-status/main/manifest.json"
**lnbits_baseurl** | str,  | str,  |  | [optional] if omitted the server will use the default value of "http://127.0.0.1:5000/"
**lnbits_reserve_fee_min** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 2000
**lnbits_reserve_fee_percent** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 1.0
**lnbits_service_fee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**lnbits_hide_api** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**lnbits_denomination** | str,  | str,  |  | [optional] if omitted the server will use the default value of "sats"
**lnbits_site_title** | str,  | str,  |  | [optional] if omitted the server will use the default value of "LNbits"
**lnbits_site_tagline** | str,  | str,  |  | [optional] if omitted the server will use the default value of "free and open-source lightning wallet"
**lnbits_site_description** | str,  | str,  |  | [optional] 
**lnbits_default_wallet_name** | str,  | str,  |  | [optional] if omitted the server will use the default value of "LNbits wallet"
**[lnbits_theme_options](#lnbits_theme_options)** | list, tuple,  | tuple,  |  | [optional] 
**lnbits_custom_logo** | str,  | str,  |  | [optional] 
**lnbits_ad_space_title** | str,  | str,  |  | [optional] if omitted the server will use the default value of "Supported by"
**lnbits_ad_space** | str,  | str,  |  | [optional] if omitted the server will use the default value of "https://shop.lnbits.com/;/static/images/lnbits-shop-light.png;/static/images/lnbits-shop-dark.png"
**lnbits_ad_space_enabled** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**[lnbits_allowed_currencies](#lnbits_allowed_currencies)** | list, tuple,  | tuple,  |  | [optional] 
**[lnbits_admin_extensions](#lnbits_admin_extensions)** | list, tuple,  | tuple,  |  | [optional] 
**[lnbits_extensions_manifests](#lnbits_extensions_manifests)** | list, tuple,  | tuple,  |  | [optional] 
**[lnbits_admin_users](#lnbits_admin_users)** | list, tuple,  | tuple,  |  | [optional] 
**[lnbits_allowed_users](#lnbits_allowed_users)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lnbits_allowed_ips

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# lnbits_blocked_ips

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# lnbits_theme_options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# lnbits_allowed_currencies

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# lnbits_admin_extensions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# lnbits_extensions_manifests

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# lnbits_admin_users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# lnbits_allowed_users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

