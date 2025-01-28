"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class StoragePlanPricingTypedDict(TypedDict):
    month: NotRequired[float]


class StoragePlanPricing(BaseModel):
    month: Optional[float] = None


class StoragePlanDataTypedDict(TypedDict):
    name: NotRequired[str]
    locations: NotRequired[List[str]]
    pricing: NotRequired[StoragePlanPricingTypedDict]


class StoragePlanData(BaseModel):
    name: Optional[str] = None

    locations: Optional[List[str]] = None

    pricing: Optional[StoragePlanPricing] = None


class StoragePlanTypedDict(TypedDict):
    data: NotRequired[List[StoragePlanDataTypedDict]]


class StoragePlan(BaseModel):
    data: Optional[List[StoragePlanData]] = None
