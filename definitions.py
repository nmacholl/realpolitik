import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = f"{ROOT_DIR}{os.sep}logs"

"""
The following parameters are for setup.py but can be referenced globally here.
"""

NAME = "realpolitik"
VERSION = "0.0.1"
PACKAGES = ["realpolitik"]
URL = ""
LICENSE = ""
AUTHOR = "Nick Macholl"
AUTHOR_EMAIL = "nickmacholl@gmail.com"
DESCRIPTION = "A diplomacy discord bot."
INSTALL_REQUIRES = ["discord", "diplomacy"]
