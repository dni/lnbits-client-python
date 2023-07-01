import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.admin_api_v1_audit import AdminApiV1Audit
from openapi_client.apis.paths.admin_api_v1_settings_ import AdminApiV1Settings
from openapi_client.apis.paths.admin_api_v1_restart_ import AdminApiV1Restart
from openapi_client.apis.paths.admin_api_v1_topup_ import AdminApiV1Topup
from openapi_client.apis.paths.admin_api_v1_backup_ import AdminApiV1Backup
from openapi_client.apis.paths.api_v1_health import ApiV1Health
from openapi_client.apis.paths.api_v1_wallet import ApiV1Wallet
from openapi_client.apis.paths.api_v1_wallet_new_name import ApiV1WalletNewName
from openapi_client.apis.paths.api_v1_payments import ApiV1Payments
from openapi_client.apis.paths.api_v1_payments_paginated import ApiV1PaymentsPaginated
from openapi_client.apis.paths.api_v1_payments_lnurl import ApiV1PaymentsLnurl
from openapi_client.apis.paths.api_v1_payments_sse import ApiV1PaymentsSse
from openapi_client.apis.paths.api_v1_payments_payment_hash import ApiV1PaymentsPaymentHash
from openapi_client.apis.paths.api_v1_lnurlscan_code import ApiV1LnurlscanCode
from openapi_client.apis.paths.api_v1_payments_decode import ApiV1PaymentsDecode
from openapi_client.apis.paths.api_v1_lnurlauth import ApiV1Lnurlauth
from openapi_client.apis.paths.api_v1_currencies import ApiV1Currencies
from openapi_client.apis.paths.api_v1_conversion import ApiV1Conversion
from openapi_client.apis.paths.api_v1_qrcode_data import ApiV1QrcodeData
from openapi_client.apis.paths.api_v1_ws_item_id import ApiV1WsItemId
from openapi_client.apis.paths.api_v1_ws_item_id_data import ApiV1WsItemIdData
from openapi_client.apis.paths.api_v1_extension import ApiV1Extension
from openapi_client.apis.paths.api_v1_extension_ext_id import ApiV1ExtensionExtId
from openapi_client.apis.paths.api_v1_extension_ext_id_releases import ApiV1ExtensionExtIdReleases
from openapi_client.apis.paths.api_v1_extension_release_org_repo_tag_name import ApiV1ExtensionReleaseOrgRepoTagName
from openapi_client.apis.paths.api_v1_extension_ext_id_db import ApiV1ExtensionExtIdDb
from openapi_client.apis.paths.api_v1_tinyurl import ApiV1Tinyurl
from openapi_client.apis.paths.api_v1_tinyurl_tinyurl_id import ApiV1TinyurlTinyurlId
from openapi_client.apis.paths.t_tinyurl_id import TTinyurlId
from openapi_client.apis.paths.public_v1_payment_payment_hash import PublicV1PaymentPaymentHash

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ADMIN_API_V1_AUDIT: AdminApiV1Audit,
        PathValues.ADMIN_API_V1_SETTINGS_: AdminApiV1Settings,
        PathValues.ADMIN_API_V1_RESTART_: AdminApiV1Restart,
        PathValues.ADMIN_API_V1_TOPUP_: AdminApiV1Topup,
        PathValues.ADMIN_API_V1_BACKUP_: AdminApiV1Backup,
        PathValues.API_V1_HEALTH: ApiV1Health,
        PathValues.API_V1_WALLET: ApiV1Wallet,
        PathValues.API_V1_WALLET_NEW_NAME: ApiV1WalletNewName,
        PathValues.API_V1_PAYMENTS: ApiV1Payments,
        PathValues.API_V1_PAYMENTS_PAGINATED: ApiV1PaymentsPaginated,
        PathValues.API_V1_PAYMENTS_LNURL: ApiV1PaymentsLnurl,
        PathValues.API_V1_PAYMENTS_SSE: ApiV1PaymentsSse,
        PathValues.API_V1_PAYMENTS_PAYMENT_HASH: ApiV1PaymentsPaymentHash,
        PathValues.API_V1_LNURLSCAN_CODE: ApiV1LnurlscanCode,
        PathValues.API_V1_PAYMENTS_DECODE: ApiV1PaymentsDecode,
        PathValues.API_V1_LNURLAUTH: ApiV1Lnurlauth,
        PathValues.API_V1_CURRENCIES: ApiV1Currencies,
        PathValues.API_V1_CONVERSION: ApiV1Conversion,
        PathValues.API_V1_QRCODE_DATA: ApiV1QrcodeData,
        PathValues.API_V1_WS_ITEM_ID: ApiV1WsItemId,
        PathValues.API_V1_WS_ITEM_ID_DATA: ApiV1WsItemIdData,
        PathValues.API_V1_EXTENSION: ApiV1Extension,
        PathValues.API_V1_EXTENSION_EXT_ID: ApiV1ExtensionExtId,
        PathValues.API_V1_EXTENSION_EXT_ID_RELEASES: ApiV1ExtensionExtIdReleases,
        PathValues.API_V1_EXTENSION_RELEASE_ORG_REPO_TAG_NAME: ApiV1ExtensionReleaseOrgRepoTagName,
        PathValues.API_V1_EXTENSION_EXT_ID_DB: ApiV1ExtensionExtIdDb,
        PathValues.API_V1_TINYURL: ApiV1Tinyurl,
        PathValues.API_V1_TINYURL_TINYURL_ID: ApiV1TinyurlTinyurlId,
        PathValues.T_TINYURL_ID: TTinyurlId,
        PathValues.PUBLIC_V1_PAYMENT_PAYMENT_HASH: PublicV1PaymentPaymentHash,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ADMIN_API_V1_AUDIT: AdminApiV1Audit,
        PathValues.ADMIN_API_V1_SETTINGS_: AdminApiV1Settings,
        PathValues.ADMIN_API_V1_RESTART_: AdminApiV1Restart,
        PathValues.ADMIN_API_V1_TOPUP_: AdminApiV1Topup,
        PathValues.ADMIN_API_V1_BACKUP_: AdminApiV1Backup,
        PathValues.API_V1_HEALTH: ApiV1Health,
        PathValues.API_V1_WALLET: ApiV1Wallet,
        PathValues.API_V1_WALLET_NEW_NAME: ApiV1WalletNewName,
        PathValues.API_V1_PAYMENTS: ApiV1Payments,
        PathValues.API_V1_PAYMENTS_PAGINATED: ApiV1PaymentsPaginated,
        PathValues.API_V1_PAYMENTS_LNURL: ApiV1PaymentsLnurl,
        PathValues.API_V1_PAYMENTS_SSE: ApiV1PaymentsSse,
        PathValues.API_V1_PAYMENTS_PAYMENT_HASH: ApiV1PaymentsPaymentHash,
        PathValues.API_V1_LNURLSCAN_CODE: ApiV1LnurlscanCode,
        PathValues.API_V1_PAYMENTS_DECODE: ApiV1PaymentsDecode,
        PathValues.API_V1_LNURLAUTH: ApiV1Lnurlauth,
        PathValues.API_V1_CURRENCIES: ApiV1Currencies,
        PathValues.API_V1_CONVERSION: ApiV1Conversion,
        PathValues.API_V1_QRCODE_DATA: ApiV1QrcodeData,
        PathValues.API_V1_WS_ITEM_ID: ApiV1WsItemId,
        PathValues.API_V1_WS_ITEM_ID_DATA: ApiV1WsItemIdData,
        PathValues.API_V1_EXTENSION: ApiV1Extension,
        PathValues.API_V1_EXTENSION_EXT_ID: ApiV1ExtensionExtId,
        PathValues.API_V1_EXTENSION_EXT_ID_RELEASES: ApiV1ExtensionExtIdReleases,
        PathValues.API_V1_EXTENSION_RELEASE_ORG_REPO_TAG_NAME: ApiV1ExtensionReleaseOrgRepoTagName,
        PathValues.API_V1_EXTENSION_EXT_ID_DB: ApiV1ExtensionExtIdDb,
        PathValues.API_V1_TINYURL: ApiV1Tinyurl,
        PathValues.API_V1_TINYURL_TINYURL_ID: ApiV1TinyurlTinyurlId,
        PathValues.T_TINYURL_ID: TTinyurlId,
        PathValues.PUBLIC_V1_PAYMENT_PAYMENT_HASH: PublicV1PaymentPaymentHash,
    }
)
