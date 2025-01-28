"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .team import Team, TeamTypedDict
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TeamsMetaTypedDict(TypedDict):
    pass


class TeamsMeta(BaseModel):
    pass


class TeamsTypedDict(TypedDict):
    data: NotRequired[List[TeamTypedDict]]
    meta: NotRequired[TeamsMetaTypedDict]


class Teams(BaseModel):
    data: Optional[List[Team]] = None

    meta: Optional[TeamsMeta] = None
