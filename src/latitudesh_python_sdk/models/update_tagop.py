"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
from latitudesh_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateTagType(str, Enum):
    TAGS = "tags"


class UpdateTagAttributesTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name of the Tag"""
    description: NotRequired[str]
    r"""Description of the Tag"""
    color: NotRequired[str]
    r"""Color of the Tag"""


class UpdateTagAttributes(BaseModel):
    name: Optional[str] = None
    r"""Name of the Tag"""

    description: Optional[str] = None
    r"""Description of the Tag"""

    color: Optional[str] = "#ffffff"
    r"""Color of the Tag"""


class UpdateTagDataTypedDict(TypedDict):
    id: NotRequired[str]
    type: NotRequired[UpdateTagType]
    attributes: NotRequired[UpdateTagAttributesTypedDict]


class UpdateTagData(BaseModel):
    id: Optional[str] = None

    type: Optional[UpdateTagType] = None

    attributes: Optional[UpdateTagAttributes] = None


class UpdateTagRequestBodyTypedDict(TypedDict):
    data: NotRequired[UpdateTagDataTypedDict]


class UpdateTagRequestBody(BaseModel):
    data: Optional[UpdateTagData] = None


class UpdateTagRequestTypedDict(TypedDict):
    tag_id: str
    request_body: NotRequired[UpdateTagRequestBodyTypedDict]


class UpdateTagRequest(BaseModel):
    tag_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[UpdateTagRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
