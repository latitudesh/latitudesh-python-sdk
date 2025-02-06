"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
from latitudesh_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateServerReinstallServersType(str, Enum):
    REINSTALLS = "reinstalls"


class CreateServerReinstallServersOperatingSystem(str, Enum):
    r"""The OS selected for the reinstall process"""

    IPXE = "ipxe"
    WINDOWS_SERVER_2019_STD_V1 = "windows_server_2019_std_v1"
    UBUNTU_22_04_X64_LTS = "ubuntu_22_04_x64_lts"
    DEBIAN_11 = "debian_11"
    DEBIAN_10 = "debian_10"
    RHEL8 = "rhel8"
    WINDOWS_SERVER_2012_R2_STD_V28 = "windows_server_2012_r2_std_v28"
    WINDOWS_SERVER_2012_R2_DC_V5 = "windows_server_2012_r2_dc_v5"
    ESXI_6_7 = "esxi_6_7"
    DEBIAN_9_4_X64 = "debian_9_4_x64"
    CENTOS_7_4_X64 = "centos_7_4_x64"
    CENTOS_8_X64 = "centos_8_x64"
    UBUNTU_16_04_X64_LTS = "ubuntu_16_04_x64_lts"
    UBUNTU_20_04_X64_LTS = "ubuntu_20_04_x64_lts"
    WINDOWS_SERVER_2016_STD_V1 = "windows_server_2016_std_v1"
    WINDOWS_SERVER_2016_DC_V1 = "windows_server_2016_dc_v1"
    WINDOWS_SERVER_2019_DC_V1 = "windows_server_2019_dc_v1"
    DEBIAN_12 = "debian_12"
    UBUNTU22_ML_IN_A_BOX = "ubuntu22_ml_in_a_box"
    UBUNTU_18_04_X64_LTS = "ubuntu_18_04_x64_lts"
    WINDOWS_SERVER_2019_STD_UEFI = "windows_server_2019_std_uefi"
    WINDOWS_2022_STD_UEFI = "windows_2022_std_uefi"
    WINDOWS_2022_STD = "windows_2022_std"
    UBUNTU_24_04_X64_LTS = "ubuntu_24_04_x64_lts"
    ROCKYLINUX_8 = "rockylinux_8"


class CreateServerReinstallServersPartitionsTypedDict(TypedDict):
    size_in_gb: NotRequired[int]
    path: NotRequired[str]
    filesystem_type: NotRequired[str]


class CreateServerReinstallServersPartitions(BaseModel):
    size_in_gb: Optional[int] = None

    path: Optional[str] = None

    filesystem_type: Optional[str] = None


class CreateServerReinstallServersRaid(str, Enum):
    r"""RAID mode for the server"""

    RAID_0 = "raid-0"
    RAID_1 = "raid-1"


class CreateServerReinstallServersAttributesTypedDict(TypedDict):
    operating_system: NotRequired[CreateServerReinstallServersOperatingSystem]
    r"""The OS selected for the reinstall process"""
    hostname: NotRequired[str]
    r"""The server hostname to set upon reinstall"""
    partitions: NotRequired[List[CreateServerReinstallServersPartitionsTypedDict]]
    ssh_keys: NotRequired[List[str]]
    r"""SSH Keys to set upon reinstall"""
    user_data: NotRequired[int]
    r"""User data to set upon reinstall"""
    raid: NotRequired[CreateServerReinstallServersRaid]
    r"""RAID mode for the server"""
    ipxe: NotRequired[str]
    r"""URL where iPXE script is stored on, OR the iPXE script encoded in base64. This attribute is required when operating system iPXE is selected."""


class CreateServerReinstallServersAttributes(BaseModel):
    operating_system: Optional[CreateServerReinstallServersOperatingSystem] = None
    r"""The OS selected for the reinstall process"""

    hostname: Optional[str] = None
    r"""The server hostname to set upon reinstall"""

    partitions: Optional[List[CreateServerReinstallServersPartitions]] = None

    ssh_keys: Optional[List[str]] = None
    r"""SSH Keys to set upon reinstall"""

    user_data: Optional[int] = None
    r"""User data to set upon reinstall"""

    raid: Optional[CreateServerReinstallServersRaid] = None
    r"""RAID mode for the server"""

    ipxe: Optional[str] = None
    r"""URL where iPXE script is stored on, OR the iPXE script encoded in base64. This attribute is required when operating system iPXE is selected."""


class CreateServerReinstallServersDataTypedDict(TypedDict):
    type: CreateServerReinstallServersType
    attributes: NotRequired[CreateServerReinstallServersAttributesTypedDict]


class CreateServerReinstallServersData(BaseModel):
    type: CreateServerReinstallServersType

    attributes: Optional[CreateServerReinstallServersAttributes] = None


class CreateServerReinstallServersRequestBodyTypedDict(TypedDict):
    data: CreateServerReinstallServersDataTypedDict


class CreateServerReinstallServersRequestBody(BaseModel):
    data: CreateServerReinstallServersData


class CreateServerReinstallRequestTypedDict(TypedDict):
    server_id: str
    request_body: NotRequired[CreateServerReinstallServersRequestBodyTypedDict]


class CreateServerReinstallRequest(BaseModel):
    server_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[CreateServerReinstallServersRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
