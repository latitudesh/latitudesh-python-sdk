"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .operating_system_data import OperatingSystemData, OperatingSystemDataTypedDict
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class FeaturesTypedDict(TypedDict):
    raid: NotRequired[bool]
    ssh_keys: NotRequired[bool]
    user_data: NotRequired[bool]


class Features(BaseModel):
    raid: Optional[bool] = None

    ssh_keys: Optional[bool] = None

    user_data: Optional[bool] = None


class OperatingSystemsAttributesTypedDict(TypedDict):
    features: NotRequired[FeaturesTypedDict]
    name: NotRequired[str]
    slug: NotRequired[str]
    distro: NotRequired[str]
    user: NotRequired[str]
    version: NotRequired[str]
    provisionable_on: NotRequired[List[str]]


class OperatingSystemsAttributes(BaseModel):
    features: Optional[Features] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    distro: Optional[str] = None

    user: Optional[str] = None

    version: Optional[str] = None

    provisionable_on: Optional[List[str]] = None


class OperatingSystemsMetaTypedDict(TypedDict):
    pass


class OperatingSystemsMeta(BaseModel):
    pass


class OperatingSystemsTypedDict(TypedDict):
    id: NotRequired[str]
    attributes: NotRequired[OperatingSystemsAttributesTypedDict]
    data: NotRequired[List[OperatingSystemDataTypedDict]]
    meta: NotRequired[OperatingSystemsMetaTypedDict]


class OperatingSystems(BaseModel):
    id: Optional[str] = None

    attributes: Optional[OperatingSystemsAttributes] = None

    data: Optional[List[OperatingSystemData]] = None

    meta: Optional[OperatingSystemsMeta] = None
