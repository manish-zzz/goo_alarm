"""
Goo Cross-Platform Desktop Alarm
~~~~~~~~~~~~~~~~~~~~~

Basic usage:
Either run ./goo.py or use a shell script start_goo.sh and put it in GNOME startup applications of your computer

:copyright: (c) 2023 by Manish R. Ramani
:license: Creative Commons CC BY-NC-ND 4.0 DEED, see LICENSE for more details: https://creativecommons.org/licenses/by-nc-nd/4.0/
"""

from .__version__ import (
    __author__,
    __author_email__,
    __build__,
    __cake__,
    __copyright__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)

from .alarm import Alarm