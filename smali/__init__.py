import os
import sys

from .smali_file import SmaliFile

if sys.hexversion < 0x03080000:
    raise Exception('python 3.8 or newer required')

__all__ = [
    SmaliFile
]