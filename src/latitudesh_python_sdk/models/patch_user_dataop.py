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


class PatchUserDataUserDataType(str, Enum):
    USER_DATA = "user_data"


class PatchUserDataUserDataAttributesTypedDict(TypedDict):
    description: NotRequired[str]
    r"""description dummy user data"""
    content: NotRequired[str]
    r"""encoded content of the User Data"""


class PatchUserDataUserDataAttributes(BaseModel):
    description: Optional[str] = None
    r"""description dummy user data"""

    content: Optional[str] = None
    r"""encoded content of the User Data"""


class PatchUserDataUserDataDataTypedDict(TypedDict):
    id: str
    type: PatchUserDataUserDataType
    attributes: NotRequired[PatchUserDataUserDataAttributesTypedDict]


class PatchUserDataUserDataData(BaseModel):
    id: str

    type: PatchUserDataUserDataType

    attributes: Optional[PatchUserDataUserDataAttributes] = None


class PatchUserDataUserDataRequestBodyTypedDict(TypedDict):
    data: PatchUserDataUserDataDataTypedDict


class PatchUserDataUserDataRequestBody(BaseModel):
    data: PatchUserDataUserDataData


class PatchUserDataRequestTypedDict(TypedDict):
    user_data_id: str
    request_body: NotRequired[PatchUserDataUserDataRequestBodyTypedDict]


class PatchUserDataRequest(BaseModel):
    user_data_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[PatchUserDataUserDataRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
