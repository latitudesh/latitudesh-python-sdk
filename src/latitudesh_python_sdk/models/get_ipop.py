"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from latitudesh_python_sdk.types import BaseModel
from latitudesh_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetIPRequestTypedDict(TypedDict):
    ip_id: str
    r"""The IP Address ID"""
    extra_fields_ip_addresses: NotRequired[str]
    r"""The `region` and `server` are provided as extra attributes that is lazy loaded. To request it, just set `extra_fields[ip_addresses]=region,server` in the query string."""


class GetIPRequest(BaseModel):
    ip_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The IP Address ID"""

    extra_fields_ip_addresses: Annotated[
        Optional[str],
        pydantic.Field(alias="extra_fields[ip_addresses]"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The `region` and `server` are provided as extra attributes that is lazy loaded. To request it, just set `extra_fields[ip_addresses]=region,server` in the query string."""
