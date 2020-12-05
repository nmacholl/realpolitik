import os
from datetime import datetime
from typing import Final

"""
The root directory of the project.
"""
ROOT_DIR: Final = os.path.dirname(os.path.abspath(__file__))

"""
The start time of the module.
"""
START_TIME: Final = datetime.now()

"""
The following parameters are for setup.py but can be referenced globally here.
"""
AUTHOR: Final = "Nick Macholl"
AUTHOR_EMAIL: Final = "nickmacholl@gmail.com"
DESCRIPTION: Final = "A diplomacy discord bot."
INSTALL_REQUIRES: Final = ["discord", "diplomacy"]
LICENSE: Final = "GNU AFFERO GENERAL PUBLIC LICENSE v3"
NAME: Final = "realpolitik"
PACKAGES: Final = ["realpolitik"]
URL: Final = "https://github.com/nmacholl/realpolitik/"
VERSION: Final = "0.0.1"

"""
The following parameters are for used in logging configuration
"""
LOG_DIR: Final = f"{ROOT_DIR}{os.sep}logs"
LOG_FILE_NAME: Final = f"{LOG_DIR}{os.sep}{START_TIME.strftime('%Y%m%d')}_{NAME}.log"
LOG_FMT: Final = "%(asctime)s %(levelname)s:%(message)s "

if __name__ == "__main__":
    for item in dir():
        if item == item.upper():
            print(item)
