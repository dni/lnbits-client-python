# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.page import Page

# Query params
LimitSchema = schemas.IntSchema
OffsetSchema = schemas.IntSchema
SortbySchema = schemas.StrSchema


class DirectionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")
SearchSchema = schemas.StrSchema
CheckingIdSchema = schemas.StrSchema
AmountSchema = schemas.IntSchema
FeeSchema = schemas.IntSchema
MemoSchema = schemas.StrSchema
TimeSchema = schemas.DateTimeSchema
Bolt11Schema = schemas.StrSchema
PreimageSchema = schemas.StrSchema
PaymentHashSchema = schemas.StrSchema
ExpirySchema = schemas.DateTimeSchema
ExtraSchema = schemas.DictSchema
WalletIdSchema = schemas.StrSchema
WebhookSchema = schemas.StrSchema
WebhookStatusSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'sortby': typing.Union[SortbySchema, str, ],
        'direction': typing.Union[DirectionSchema, str, ],
        'search': typing.Union[SearchSchema, str, ],
        'checking_id': typing.Union[CheckingIdSchema, str, ],
        'amount': typing.Union[AmountSchema, decimal.Decimal, int, ],
        'fee': typing.Union[FeeSchema, decimal.Decimal, int, ],
        'memo': typing.Union[MemoSchema, str, ],
        'time': typing.Union[TimeSchema, str, datetime, ],
        'bolt11': typing.Union[Bolt11Schema, str, ],
        'preimage': typing.Union[PreimageSchema, str, ],
        'payment_hash': typing.Union[PaymentHashSchema, str, ],
        'expiry': typing.Union[ExpirySchema, str, datetime, ],
        'extra': typing.Union[ExtraSchema, dict, frozendict.frozendict, ],
        'wallet_id': typing.Union[WalletIdSchema, str, ],
        'webhook': typing.Union[WebhookSchema, str, ],
        'webhook_status': typing.Union[WebhookStatusSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_sortby = api_client.QueryParameter(
    name="sortby",
    style=api_client.ParameterStyle.FORM,
    schema=SortbySchema,
    explode=True,
)
request_query_direction = api_client.QueryParameter(
    name="direction",
    style=api_client.ParameterStyle.FORM,
    schema=DirectionSchema,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_checking_id = api_client.QueryParameter(
    name="checking_id",
    style=api_client.ParameterStyle.FORM,
    schema=CheckingIdSchema,
    explode=True,
)
request_query_amount = api_client.QueryParameter(
    name="amount",
    style=api_client.ParameterStyle.FORM,
    schema=AmountSchema,
    explode=True,
)
request_query_fee = api_client.QueryParameter(
    name="fee",
    style=api_client.ParameterStyle.FORM,
    schema=FeeSchema,
    explode=True,
)
request_query_memo = api_client.QueryParameter(
    name="memo",
    style=api_client.ParameterStyle.FORM,
    schema=MemoSchema,
    explode=True,
)
request_query_time = api_client.QueryParameter(
    name="time",
    style=api_client.ParameterStyle.FORM,
    schema=TimeSchema,
    explode=True,
)
request_query_bolt11 = api_client.QueryParameter(
    name="bolt11",
    style=api_client.ParameterStyle.FORM,
    schema=Bolt11Schema,
    explode=True,
)
request_query_preimage = api_client.QueryParameter(
    name="preimage",
    style=api_client.ParameterStyle.FORM,
    schema=PreimageSchema,
    explode=True,
)
request_query_payment_hash = api_client.QueryParameter(
    name="payment_hash",
    style=api_client.ParameterStyle.FORM,
    schema=PaymentHashSchema,
    explode=True,
)
request_query_expiry = api_client.QueryParameter(
    name="expiry",
    style=api_client.ParameterStyle.FORM,
    schema=ExpirySchema,
    explode=True,
)
request_query_extra = api_client.QueryParameter(
    name="extra",
    style=api_client.ParameterStyle.FORM,
    schema=ExtraSchema,
    explode=True,
)
request_query_wallet_id = api_client.QueryParameter(
    name="wallet_id",
    style=api_client.ParameterStyle.FORM,
    schema=WalletIdSchema,
    explode=True,
)
request_query_webhook = api_client.QueryParameter(
    name="webhook",
    style=api_client.ParameterStyle.FORM,
    schema=WebhookSchema,
    explode=True,
)
request_query_webhook_status = api_client.QueryParameter(
    name="webhook_status",
    style=api_client.ParameterStyle.FORM,
    schema=WebhookStatusSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = Page


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationError


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor422ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _payment_list_api_v1_payments_paginated_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _payment_list_api_v1_payments_paginated_get_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _payment_list_api_v1_payments_paginated_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _payment_list_api_v1_payments_paginated_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        get paginated list of payments
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_sortby,
            request_query_direction,
            request_query_search,
            request_query_checking_id,
            request_query_amount,
            request_query_fee,
            request_query_memo,
            request_query_time,
            request_query_bolt11,
            request_query_preimage,
            request_query_payment_hash,
            request_query_expiry,
            request_query_extra,
            request_query_wallet_id,
            request_query_webhook,
            request_query_webhook_status,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class PaymentListApiV1PaymentsPaginatedGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def payment_list_api_v1_payments_paginated_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def payment_list_api_v1_payments_paginated_get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def payment_list_api_v1_payments_paginated_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def payment_list_api_v1_payments_paginated_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._payment_list_api_v1_payments_paginated_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._payment_list_api_v1_payments_paginated_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

