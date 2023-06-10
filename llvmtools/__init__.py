__all__ = []
__version__ = "0.0.1"
__author__ = "Yusuf Rençber"

import os

if os.name != "nt":
    raise OSError("This module does not support the OS you are using.")

from llvmtools.tools import *