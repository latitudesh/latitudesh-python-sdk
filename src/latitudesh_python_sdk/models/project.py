"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .team_include import TeamInclude, TeamIncludeTypedDict
from enum import Enum
from latitudesh_python_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BillingType(str, Enum):
    YEARLY = "Yearly"
    MONTHLY = "Monthly"
    HOURLY = "Hourly"
    NORMAL = "Normal"


class BillingMethod(str, Enum):
    NORMAL = "Normal"
    NINETY_FIVETH_PERCENTILE = "95th percentile"


class Environment(str, Enum):
    DEVELOPMENT = "Development"
    STAGING = "Staging"
    PRODUCTION = "Production"


class ProjectStatsTypedDict(TypedDict):
    ip_addresses: NotRequired[float]
    r"""The number of IP addresses assigned to the project"""
    prefixes: NotRequired[float]
    r"""The IP address prefixes in the project"""
    servers: NotRequired[float]
    r"""The number of servers assigned to the project"""
    containers: NotRequired[float]
    r"""The number of containers assigned to the project"""
    vlans: NotRequired[float]
    r"""The number of VLANs assigned to the project"""


class ProjectStats(BaseModel):
    ip_addresses: Optional[float] = None
    r"""The number of IP addresses assigned to the project"""

    prefixes: Optional[float] = None
    r"""The IP address prefixes in the project"""

    servers: Optional[float] = None
    r"""The number of servers assigned to the project"""

    containers: Optional[float] = None
    r"""The number of containers assigned to the project"""

    vlans: Optional[float] = None
    r"""The number of VLANs assigned to the project"""


class ProjectBillingTypedDict(TypedDict):
    subscription_id: NotRequired[str]
    type: NotRequired[str]
    method: NotRequired[str]


class ProjectBilling(BaseModel):
    subscription_id: Optional[str] = None

    type: Optional[str] = None

    method: Optional[str] = None


class ProjectAttributesTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The project name"""
    slug: NotRequired[str]
    r"""A unique project identifier"""
    description: NotRequired[str]
    r"""The project description"""
    billing_type: NotRequired[BillingType]
    billing_method: NotRequired[BillingMethod]
    cost: NotRequired[str]
    environment: NotRequired[Environment]
    stats: NotRequired[ProjectStatsTypedDict]
    billing: NotRequired[ProjectBillingTypedDict]
    team: NotRequired[TeamIncludeTypedDict]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]


class ProjectAttributes(BaseModel):
    name: Optional[str] = None
    r"""The project name"""

    slug: Optional[str] = None
    r"""A unique project identifier"""

    description: Optional[str] = None
    r"""The project description"""

    billing_type: Optional[BillingType] = None

    billing_method: Optional[BillingMethod] = None

    cost: Optional[str] = None

    environment: Optional[Environment] = None

    stats: Optional[ProjectStats] = None

    billing: Optional[ProjectBilling] = None

    team: Optional[TeamInclude] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None


class ProjectTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The project ID"""
    attributes: NotRequired[ProjectAttributesTypedDict]


class Project(BaseModel):
    id: Optional[str] = None
    r"""The project ID"""

    attributes: Optional[ProjectAttributes] = None
