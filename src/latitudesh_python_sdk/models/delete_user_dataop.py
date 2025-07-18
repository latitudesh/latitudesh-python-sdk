"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from latitudesh_python_sdk.types import BaseModel
from latitudesh_python_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteUserDataRequestTypedDict(TypedDict):
    user_data_id: str


class DeleteUserDataRequest(BaseModel):
    user_data_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
