"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RegionCountryTypedDict(TypedDict):
    slug: NotRequired[str]
    name: NotRequired[str]


class RegionCountry(BaseModel):
    slug: Optional[str] = None

    name: Optional[str] = None


class RegionAttributesTypedDict(TypedDict):
    slug: NotRequired[str]
    name: NotRequired[str]
    country: NotRequired[RegionCountryTypedDict]


class RegionAttributes(BaseModel):
    slug: Optional[str] = None

    name: Optional[str] = None

    country: Optional[RegionCountry] = None


class RegionDataTypedDict(TypedDict):
    id: NotRequired[str]
    attributes: NotRequired[RegionAttributesTypedDict]


class RegionData(BaseModel):
    id: Optional[str] = None

    attributes: Optional[RegionAttributes] = None


class RegionTypedDict(TypedDict):
    data: NotRequired[RegionDataTypedDict]


class Region(BaseModel):
    data: Optional[RegionData] = None
