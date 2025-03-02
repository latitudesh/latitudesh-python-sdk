"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UserIncludeRoleTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]


class UserIncludeRole(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None


class UserIncludeTypedDict(TypedDict):
    id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    authentication_factor_id: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    role: NotRequired[UserIncludeRoleTypedDict]


class UserInclude(BaseModel):
    id: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    email: Optional[str] = None

    authentication_factor_id: Optional[str] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    role: Optional[UserIncludeRole] = None
