# coding: utf-8

"""
    lnbits

    API for LNbits, the free and open source bitcoin wallet and accounts system with plugins.  # noqa: E501

    The version of the OpenAPI document: 0.10.9
    Generated by: https://openapi-generator.tech
"""

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


class CreateLNURLData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "amount",
            "description_hash",
            "callback",
        }
        
        class properties:
            description_hash = schemas.StrSchema
            callback = schemas.StrSchema
            amount = schemas.IntSchema
            comment = schemas.StrSchema
            description = schemas.StrSchema
            __annotations__ = {
                "description_hash": description_hash,
                "callback": callback,
                "amount": amount,
                "comment": comment,
                "description": description,
            }
    
    amount: MetaOapg.properties.amount
    description_hash: MetaOapg.properties.description_hash
    callback: MetaOapg.properties.callback
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description_hash"]) -> MetaOapg.properties.description_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callback"]) -> MetaOapg.properties.callback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description_hash", "callback", "amount", "comment", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description_hash"]) -> MetaOapg.properties.description_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callback"]) -> MetaOapg.properties.callback: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description_hash", "callback", "amount", "comment", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        description_hash: typing.Union[MetaOapg.properties.description_hash, str, ],
        callback: typing.Union[MetaOapg.properties.callback, str, ],
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateLNURLData':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            description_hash=description_hash,
            callback=callback,
            comment=comment,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )