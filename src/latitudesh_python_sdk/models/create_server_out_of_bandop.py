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


class CreateServerOutOfBandServersType(str, Enum):
    OUT_OF_BAND = "out_of_band"


class CreateServerOutOfBandServersAttributesTypedDict(TypedDict):
    ssh_key_id: NotRequired[str]
    r"""SSH Key ID to set for out of band"""


class CreateServerOutOfBandServersAttributes(BaseModel):
    ssh_key_id: Optional[str] = None
    r"""SSH Key ID to set for out of band"""


class CreateServerOutOfBandServersDataTypedDict(TypedDict):
    type: CreateServerOutOfBandServersType
    attributes: NotRequired[CreateServerOutOfBandServersAttributesTypedDict]


class CreateServerOutOfBandServersData(BaseModel):
    type: CreateServerOutOfBandServersType

    attributes: Optional[CreateServerOutOfBandServersAttributes] = None


class CreateServerOutOfBandServersRequestBodyTypedDict(TypedDict):
    data: CreateServerOutOfBandServersDataTypedDict


class CreateServerOutOfBandServersRequestBody(BaseModel):
    data: CreateServerOutOfBandServersData


class CreateServerOutOfBandRequestTypedDict(TypedDict):
    server_id: str
    request_body: NotRequired[CreateServerOutOfBandServersRequestBodyTypedDict]


class CreateServerOutOfBandRequest(BaseModel):
    server_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[CreateServerOutOfBandServersRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
