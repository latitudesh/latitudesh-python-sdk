"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AuthorTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    email: NotRequired[str]


class Author(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    email: Optional[str] = None


class EventsProjectTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    slug: NotRequired[str]


class EventsProject(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None


class EventsTeamTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]


class EventsTeam(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class TargetTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]


class Target(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class EventsAttributesTypedDict(TypedDict):
    action: NotRequired[str]
    created_at: NotRequired[str]
    author: NotRequired[AuthorTypedDict]
    project: NotRequired[EventsProjectTypedDict]
    team: NotRequired[EventsTeamTypedDict]
    target: NotRequired[TargetTypedDict]


class EventsAttributes(BaseModel):
    action: Optional[str] = None

    created_at: Optional[str] = None

    author: Optional[Author] = None

    project: Optional[EventsProject] = None

    team: Optional[EventsTeam] = None

    target: Optional[Target] = None


class EventsTypedDict(TypedDict):
    id: NotRequired[str]
    attributes: NotRequired[EventsAttributesTypedDict]


class Events(BaseModel):
    id: Optional[str] = None

    attributes: Optional[EventsAttributes] = None
