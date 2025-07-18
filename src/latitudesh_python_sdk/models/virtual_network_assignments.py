"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .virtual_network_assignment_data import (
    VirtualNetworkAssignmentData,
    VirtualNetworkAssignmentDataTypedDict,
)
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class VirtualNetworkAssignmentsMetaTypedDict(TypedDict):
    pass


class VirtualNetworkAssignmentsMeta(BaseModel):
    pass


class VirtualNetworkAssignmentsTypedDict(TypedDict):
    data: NotRequired[List[VirtualNetworkAssignmentDataTypedDict]]
    meta: NotRequired[VirtualNetworkAssignmentsMetaTypedDict]


class VirtualNetworkAssignments(BaseModel):
    data: Optional[List[VirtualNetworkAssignmentData]] = None

    meta: Optional[VirtualNetworkAssignmentsMeta] = None
