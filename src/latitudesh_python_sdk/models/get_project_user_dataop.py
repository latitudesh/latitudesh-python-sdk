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


class GetProjectUserDataRequestTypedDict(TypedDict):
    project_id: str
    r"""Project ID or Slug"""
    user_data_id: str
    extra_fields_user_data: NotRequired[str]
    r"""The `decoded_content` is provided as an extra attribute that shows content in decoded form."""


class GetProjectUserDataRequest(BaseModel):
    project_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Project ID or Slug"""

    user_data_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    extra_fields_user_data: Annotated[
        Optional[str],
        pydantic.Field(alias="extra_fields[user_data]"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "decoded_content"
    r"""The `decoded_content` is provided as an extra attribute that shows content in decoded form."""
