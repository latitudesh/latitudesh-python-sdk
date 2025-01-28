"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .user_include import UserInclude, UserIncludeTypedDict
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SSHKeyDataType(str, Enum):
    SSH_KEYS = "ssh_keys"


class SSHKeyDataAttributesTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name of the SSH Key"""
    public_key: NotRequired[str]
    r"""SSH Public Key"""
    fingerprint: NotRequired[str]
    r"""SSH Key fingerprint"""
    user: NotRequired[UserIncludeTypedDict]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]


class SSHKeyDataAttributes(BaseModel):
    name: Optional[str] = None
    r"""Name of the SSH Key"""

    public_key: Optional[str] = None
    r"""SSH Public Key"""

    fingerprint: Optional[str] = None
    r"""SSH Key fingerprint"""

    user: Optional[UserInclude] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None


class SSHKeyDataTypedDict(TypedDict):
    type: SSHKeyDataType
    id: NotRequired[str]
    attributes: NotRequired[SSHKeyDataAttributesTypedDict]


class SSHKeyData(BaseModel):
    type: SSHKeyDataType

    id: Optional[str] = None

    attributes: Optional[SSHKeyDataAttributes] = None
