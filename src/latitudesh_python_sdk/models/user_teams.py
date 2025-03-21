"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .user_team import UserTeam, UserTeamTypedDict
from latitudesh_python_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class UserTeamsMetaTypedDict(TypedDict):
    pass


class UserTeamsMeta(BaseModel):
    pass


class UserTeamsTypedDict(TypedDict):
    data: NotRequired[List[UserTeamTypedDict]]
    meta: NotRequired[UserTeamsMetaTypedDict]


class UserTeams(BaseModel):
    data: Optional[List[UserTeam]] = None

    meta: Optional[UserTeamsMeta] = None
