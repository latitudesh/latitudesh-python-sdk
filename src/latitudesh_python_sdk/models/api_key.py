"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class Type(str, Enum):
    API_KEYS = "api_keys"


class APIKeyUserTypedDict(TypedDict):
    r"""The owner of the API Key"""

    id: NotRequired[str]
    email: NotRequired[str]


class APIKeyUser(BaseModel):
    r"""The owner of the API Key"""

    id: Optional[str] = None

    email: Optional[str] = None


class AttributesTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name of the API Key"""
    api_version: NotRequired[str]
    r"""The API version associated with this API Key"""
    token_last_slice: NotRequired[str]
    r"""The last 5 characters of the token created for this API Key"""
    last_used_at: NotRequired[datetime]
    r"""The last time a request was made to the API using this API Key"""
    user: NotRequired[APIKeyUserTypedDict]
    r"""The owner of the API Key"""
    created_at: NotRequired[datetime]
    r"""The time when the API Key was created"""
    updated_at: NotRequired[datetime]
    r"""The time when the API Key was updated"""


class Attributes(BaseModel):
    name: Optional[str] = None
    r"""Name of the API Key"""

    api_version: Optional[str] = None
    r"""The API version associated with this API Key"""

    token_last_slice: Optional[str] = None
    r"""The last 5 characters of the token created for this API Key"""

    last_used_at: Optional[datetime] = None
    r"""The last time a request was made to the API using this API Key"""

    user: Optional[APIKeyUser] = None
    r"""The owner of the API Key"""

    created_at: Optional[datetime] = None
    r"""The time when the API Key was created"""

    updated_at: Optional[datetime] = None
    r"""The time when the API Key was updated"""


class APIKeyTypedDict(TypedDict):
    id: NotRequired[str]
    type: NotRequired[Type]
    attributes: NotRequired[AttributesTypedDict]


class APIKey(BaseModel):
    id: Optional[str] = None

    type: Optional[Type] = None

    attributes: Optional[Attributes] = None
