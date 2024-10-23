from __future__ import annotations

from typing import TypedDict, List, Optional
from typing_extensions import NotRequired

from .user import User
from .team import Team
from .snowflake import Snowflake
from .emoji import Emoji


class InstallParams(TypedDict):
    scopes: List[str]
    permissions: str


class BaseAppInfo(TypedDict):
    id: Snowflake
    name: str
    verify_key: str
    icon: Optional[str]
    summary: str
    description: str
    flags: int
    approximate_user_install_count: NotRequired[int]
    cover_image: NotRequired[str]
    terms_of_service_url: NotRequired[str]
    privacy_policy_url: NotRequired[str]
    rpc_origins: NotRequired[List[str]]
    interactions_endpoint_url: NotRequired[Optional[str]]
    redirect_uris: NotRequired[List[str]]
    role_connections_verification_url: NotRequired[Optional[str]]


class AppInfo(BaseAppInfo):
    owner: User
    bot_public: bool
    bot_require_code_grant: bool
    team: NotRequired[Team]
    guild_id: NotRequired[Snowflake]
    primary_sku_id: NotRequired[Snowflake]
    slug: NotRequired[str]
    hook: NotRequired[bool]
    max_participants: NotRequired[int]
    tags: NotRequired[List[str]]
    install_params: NotRequired[InstallParams]
    custom_install_url: NotRequired[str]


class PartialAppInfo(BaseAppInfo, total=False):
    hook: bool
    max_participants: int
    approximate_guild_count: int


class GatewayAppInfo(TypedDict):
    id: Snowflake
    flags: int


class ListAppEmojis(TypedDict):
    items: List[Emoji]