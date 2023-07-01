import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.core_api import CoreApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CORE: CoreApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CORE: CoreApi,
    }
)
