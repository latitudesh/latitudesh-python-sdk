"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ServerActionType(str, Enum):
    ACTIONS = "actions"


class ServerActionAttributesTypedDict(TypedDict):
    status: NotRequired[str]


class ServerActionAttributes(BaseModel):
    status: Optional[str] = None


class ServerActionDataTypedDict(TypedDict):
    id: NotRequired[str]
    type: NotRequired[ServerActionType]
    attributes: NotRequired[ServerActionAttributesTypedDict]


class ServerActionData(BaseModel):
    id: Optional[str] = None

    type: Optional[ServerActionType] = None

    attributes: Optional[ServerActionAttributes] = None


class ServerActionMetaTypedDict(TypedDict):
    pass


class ServerActionMeta(BaseModel):
    pass


class ServerActionTypedDict(TypedDict):
    data: NotRequired[ServerActionDataTypedDict]
    meta: NotRequired[ServerActionMetaTypedDict]


class ServerAction(BaseModel):
    data: Optional[ServerActionData] = None

    meta: Optional[ServerActionMeta] = None
