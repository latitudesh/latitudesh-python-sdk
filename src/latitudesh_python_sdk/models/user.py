"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .team_include import TeamInclude, TeamIncludeTypedDict
from datetime import datetime
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class UserRoleTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


class UserRole(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class UserAttributesTypedDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    authentication_factor_id: NotRequired[str]
    role: NotRequired[UserRoleTypedDict]
    teams: NotRequired[List[TeamIncludeTypedDict]]


class UserAttributes(BaseModel):
    first_name: Optional[str] = None

    last_name: Optional[str] = None

    email: Optional[str] = None

    authentication_factor_id: Optional[str] = None

    role: Optional[UserRole] = None

    teams: Optional[List[TeamInclude]] = None


class UserTypedDict(TypedDict):
    id: NotRequired[str]
    attributes: NotRequired[UserAttributesTypedDict]


class User(BaseModel):
    id: Optional[str] = None

    attributes: Optional[UserAttributes] = None
