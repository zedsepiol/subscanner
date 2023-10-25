from colorama import Fore
import argparse
from typing import NamedTuple, Literal
from domain import *
from web.scripts.convert_txt import *
from web.fetcher import *

__title__ = "subscanner"
__author__ = "zedsepiol"
__version__ = "1.0.0"
__license__ = "MIT"
__url__ = "https://github.com/zedsepiol/subscanner"


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=1, minor=0, micro=0, releaselevel='beta', serial=0)

del NamedTuple, Literal, VersionInfo
