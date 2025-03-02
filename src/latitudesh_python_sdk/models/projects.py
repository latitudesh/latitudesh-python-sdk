"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .project import Project, ProjectTypedDict
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ProjectsTypedDict(TypedDict):
    data: NotRequired[List[ProjectTypedDict]]


class Projects(BaseModel):
    data: Optional[List[Project]] = None
