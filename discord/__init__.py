"""
Discord API Wrapper
~~~~~~~~~~~~~~~~~~~

An advanced wrapper for the Discord API.

:copyright: (c) 2015-present Rapptz
:license: MIT, see LICENSE for more details.

"""
# FUCK GITHUB WORKFLOWS X2

__title__ = 'disdick'
__author__ = 'cop-discord/Rapptz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-present Rapptz'
__version__ = '2.4.0'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)
__slots__ = ('you','are','a','faggot')

import loguru
from typing import NamedTuple, Literal

from .client import *
from .expiringdictionary import *
from .appinfo import *
from .user import *
from .emoji import *
from .partial_emoji import *
from .activity import *
from .channel import *
from .guild import *
from .flags import *
from .member import *
from .message import *
from .asset import *
from .errors import *
from .permissions import *
from .role import *
from .file import *
from .colour import *
from .integrations import *
from .invite import *
from .template import *
from .welcome_screen import *
from .soundboard import *
from .widget import *
from .object import *
from .reaction import *
from . import (
    utils as utils,
    regex as regex,
    opus as opus,
    abc as abc,
    ui as ui,
    app_commands as app_commands,
)
from .enums import *
from .embeds import *
from .mentions import *
from .shard import *
from .player import *
from .webhook import *
from .voice_client import *
from .audit_logs import *
from .raw_models import *
from .team import *
from .sticker import *
from .stage_instance import *
from .scheduled_event import *
from .interactions import *
from .components import *
from .threads import *
from .automod import *
from .pool import *
from .globals import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=2, minor=3, micro=1, releaselevel='alpha', serial=0)


del NamedTuple, Literal, VersionInfo
