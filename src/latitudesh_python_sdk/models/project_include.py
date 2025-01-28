"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BillingModelTypedDict(TypedDict):
    subscription_id: NotRequired[str]
    type: NotRequired[str]
    method: NotRequired[str]


class BillingModel(BaseModel):
    subscription_id: Optional[str] = None

    type: Optional[str] = None

    method: Optional[str] = None


class StatsTypedDict(TypedDict):
    ip_addresses: NotRequired[int]
    prefixes: NotRequired[int]
    servers: NotRequired[int]
    vlans: NotRequired[int]


class Stats(BaseModel):
    ip_addresses: Optional[int] = None

    prefixes: Optional[int] = None

    servers: Optional[int] = None

    vlans: Optional[int] = None


class ProjectIncludeTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    slug: NotRequired[str]
    description: NotRequired[str]
    billing_type: NotRequired[str]
    billing_method: NotRequired[str]
    bandwidth_alert: NotRequired[bool]
    environment: NotRequired[str]
    billing: NotRequired[BillingModelTypedDict]
    stats: NotRequired[StatsTypedDict]


class ProjectInclude(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    description: Optional[str] = None

    billing_type: Optional[str] = None

    billing_method: Optional[str] = None

    bandwidth_alert: Optional[bool] = None

    environment: Optional[str] = None

    billing: Optional[BillingModel] = None

    stats: Optional[Stats] = None
