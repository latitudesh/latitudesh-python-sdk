"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .virtual_network import VirtualNetwork, VirtualNetworkTypedDict
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class VirtualNetworksMetaTypedDict(TypedDict):
    pass


class VirtualNetworksMeta(BaseModel):
    pass


class VirtualNetworksTypedDict(TypedDict):
    data: NotRequired[List[VirtualNetworkTypedDict]]
    meta: NotRequired[VirtualNetworksMetaTypedDict]


class VirtualNetworks(BaseModel):
    data: Optional[List[VirtualNetwork]] = None

    meta: Optional[VirtualNetworksMeta] = None
