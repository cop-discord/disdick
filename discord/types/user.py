"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from .snowflake import Snowflake
from typing import Literal, Optional, Any, TypedDict
from typing_extensions import NotRequired

class PartialUser(TypedDict):
    id: Snowflake
    username: str
    discriminator: str
    avatar: Optional[str]


ConnectionType = Literal[
    'battlenet',
    'contacts',
    'crunchyroll',
    'ebay',
    'epicgames',
    'facebook',
    'github',
    'instagram',
    'leagueoflegends',
    'paypal',
    'playstation',
    'reddit',
    'riotgames',
    'samsung',
    'spotify',
    'skype',
    'steam',
    'tiktok',
    'twitch',
    'twitter',
    'youtube',
    'xbox',
]
ConnectionVisibilty = Literal[0, 1]

class PartialWorkerUser(TypedDict):
    id: Snowflake
    username: str
    discriminator: str
    avatar: Optional[str]
    avatar_decoration: NotRequired[Optional[str]]
    public_flags: NotRequired[int]
    bot: NotRequired[bool]
    system: NotRequired[bool]

class APIUser(TypedDict):
    banner: Optional[str]
    accent_color: Optional[int]

WorkerPremiumType = Literal[0, 1, 2, 3]

class WorkerUser(APIUser, total=False):
    mfa_enabled: bool
    locale: str
    verified: bool
    email: Optional[str]
    flags: int
    purchased_flags: int
    premium_usage_flags: int
    premium_type: WorkerPremiumType
    bio: str
    analytics_token: str
    phone: Optional[str]
    token: str
    nsfw_allowed: Optional[bool]


class PartialConnection(TypedDict):
    id: str
    type: ConnectionType
    name: str
    verified: bool
    metadata: NotRequired[dict[str, Any]]


class Connection(PartialConnection):
    revoked: bool
    visibility: Literal[0, 1]
    metadata_visibility: Literal[0, 1]
    show_activity: bool
    friend_sync: bool
    two_way_link: bool
    integrations: NotRequired[List[Any]]
    access_token: NotRequired[str]

PremiumType = Literal[0, 1, 2]


class User(PartialUser, total=False):
    bot: bool
    system: bool
    mfa_enabled: bool
    local: str
    verified: bool
    email: Optional[str]
    flags: int
    premium_type: PremiumType
    public_flags: int
