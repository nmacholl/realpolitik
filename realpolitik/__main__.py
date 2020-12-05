import logging
import os
import sys

from realpolitik import Diplomat
from datetime import datetime
from definitions import LOG_DIR, NAME, VERSION

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

fmt = logging.Formatter("%(asctime)s %(levelname)s:%(message)s ")

std = logging.StreamHandler(sys.stderr)
std.setLevel(logging.ERROR)
std.setFormatter(fmt)
LOGGER.addHandler(std)

try:
    os.makedirs(LOG_DIR, exist_ok=True)
    file = logging.FileHandler(
        filename=f"{LOG_DIR}{os.sep}{datetime.now().strftime('%Y%m%d')}.log", mode="a+"
    )
    file.setLevel(logging.DEBUG)
    file.setFormatter(fmt)
    LOGGER.addHandler(file)
except PermissionError as e:
    std.setLevel(logging.INFO)

LOGGER.info(f"{NAME} v{VERSION} is starting")

if len(sys.argv) > 1:
    try:
        diplomat = Diplomat(token=sys.argv[1])
        diplomat.run()
    except Exception as e:
        LOGGER.exception(e)
        exit(1)
else:
    print("A discord bot token is required.")
    exit(1)
