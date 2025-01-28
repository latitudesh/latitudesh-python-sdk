"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateFirewallType(str, Enum):
    FIREWALLS = "firewalls"


class Protocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"


class CreateFirewallRulesTypedDict(TypedDict):
    from_: NotRequired[str]
    to: NotRequired[str]
    protocol: NotRequired[Protocol]
    port: NotRequired[str]
    r"""Port number or range (e.g., \"80\", \"80-443\")"""


class CreateFirewallRules(BaseModel):
    from_: Annotated[Optional[str], pydantic.Field(alias="from")] = None

    to: Optional[str] = None

    protocol: Optional[Protocol] = None

    port: Optional[str] = None
    r"""Port number or range (e.g., \"80\", \"80-443\")"""


class CreateFirewallAttributesTypedDict(TypedDict):
    name: str
    project: str
    rules: NotRequired[List[CreateFirewallRulesTypedDict]]


class CreateFirewallAttributes(BaseModel):
    name: str

    project: str

    rules: Optional[List[CreateFirewallRules]] = None


class CreateFirewallDataTypedDict(TypedDict):
    type: CreateFirewallType
    attributes: NotRequired[CreateFirewallAttributesTypedDict]


class CreateFirewallData(BaseModel):
    type: CreateFirewallType

    attributes: Optional[CreateFirewallAttributes] = None


class CreateFirewallRequestBodyTypedDict(TypedDict):
    data: CreateFirewallDataTypedDict


class CreateFirewallRequestBody(BaseModel):
    data: CreateFirewallData
