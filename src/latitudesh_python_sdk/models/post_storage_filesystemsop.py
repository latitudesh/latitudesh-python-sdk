"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .filesystem_data import FilesystemData, FilesystemDataTypedDict
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PostStorageFilesystemsStorageType(str, Enum):
    FILESYSTEMS = "filesystems"


class PostStorageFilesystemsStorageAttributesTypedDict(TypedDict):
    project: str
    r"""Project ID or slug"""
    name: str
    r"""Storage name"""
    size_in_gb: NotRequired[int]
    r"""Size in GB (not required, default is 1500)"""


class PostStorageFilesystemsStorageAttributes(BaseModel):
    project: str
    r"""Project ID or slug"""

    name: str
    r"""Storage name"""

    size_in_gb: Optional[int] = 1500
    r"""Size in GB (not required, default is 1500)"""


class PostStorageFilesystemsStorageDataTypedDict(TypedDict):
    type: PostStorageFilesystemsStorageType
    attributes: PostStorageFilesystemsStorageAttributesTypedDict


class PostStorageFilesystemsStorageData(BaseModel):
    type: PostStorageFilesystemsStorageType

    attributes: PostStorageFilesystemsStorageAttributes


class PostStorageFilesystemsStorageRequestBodyTypedDict(TypedDict):
    data: PostStorageFilesystemsStorageDataTypedDict


class PostStorageFilesystemsStorageRequestBody(BaseModel):
    data: PostStorageFilesystemsStorageData


class PostStorageFilesystemsResponseBodyTypedDict(TypedDict):
    r"""Created"""

    data: NotRequired[FilesystemDataTypedDict]


class PostStorageFilesystemsResponseBody(BaseModel):
    r"""Created"""

    data: Optional[FilesystemData] = None
