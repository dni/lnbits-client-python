# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ADMIN_API_V1_AUDIT = "/admin/api/v1/audit"
    ADMIN_API_V1_SETTINGS_ = "/admin/api/v1/settings/"
    ADMIN_API_V1_RESTART_ = "/admin/api/v1/restart/"
    ADMIN_API_V1_TOPUP_ = "/admin/api/v1/topup/"
    ADMIN_API_V1_BACKUP_ = "/admin/api/v1/backup/"
    API_V1_HEALTH = "/api/v1/health"
    API_V1_WALLET = "/api/v1/wallet"
    API_V1_WALLET_NEW_NAME = "/api/v1/wallet/{new_name}"
    API_V1_PAYMENTS = "/api/v1/payments"
    API_V1_PAYMENTS_PAGINATED = "/api/v1/payments/paginated"
    API_V1_PAYMENTS_LNURL = "/api/v1/payments/lnurl"
    API_V1_PAYMENTS_SSE = "/api/v1/payments/sse"
    API_V1_PAYMENTS_PAYMENT_HASH = "/api/v1/payments/{payment_hash}"
    API_V1_LNURLSCAN_CODE = "/api/v1/lnurlscan/{code}"
    API_V1_PAYMENTS_DECODE = "/api/v1/payments/decode"
    API_V1_LNURLAUTH = "/api/v1/lnurlauth"
    API_V1_CURRENCIES = "/api/v1/currencies"
    API_V1_CONVERSION = "/api/v1/conversion"
    API_V1_QRCODE_DATA = "/api/v1/qrcode/{data}"
    API_V1_WS_ITEM_ID = "/api/v1/ws/{item_id}"
    API_V1_WS_ITEM_ID_DATA = "/api/v1/ws/{item_id}/{data}"
    API_V1_EXTENSION = "/api/v1/extension"
    API_V1_EXTENSION_EXT_ID = "/api/v1/extension/{ext_id}"
    API_V1_EXTENSION_EXT_ID_RELEASES = "/api/v1/extension/{ext_id}/releases"
    API_V1_EXTENSION_RELEASE_ORG_REPO_TAG_NAME = "/api/v1/extension/release/{org}/{repo}/{tag_name}"
    API_V1_EXTENSION_EXT_ID_DB = "/api/v1/extension/{ext_id}/db"
    API_V1_TINYURL = "/api/v1/tinyurl"
    API_V1_TINYURL_TINYURL_ID = "/api/v1/tinyurl/{tinyurl_id}"
    T_TINYURL_ID = "/t/{tinyurl_id}"
    PUBLIC_V1_PAYMENT_PAYMENT_HASH = "/public/v1/payment/{payment_hash}"
