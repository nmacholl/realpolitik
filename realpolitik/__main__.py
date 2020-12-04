import logging
import os
import sys

from realpolitik import Diplomat
from datetime import datetime
from definitions import LOG_DIR, NAME, VERSION

LOGGER = logging.getLogger(name=__name__)
log_config = {
    "datefmt": "%H:%M:%S",
    "format": "%(asctime)s %(levelname)s:%(message)s ",
    "level": logging.INFO,
}

try:
    os.makedirs(LOG_DIR, exist_ok=True)
    log_config[
        "filename"
    ] = f"{LOG_DIR}{os.sep}{NAME.lower()}.{datetime.now().strftime('%Y%m%d')}.log"
except PermissionError:
    # We do not have permissions for the log directory.
    log_config["stream"] = sys.stderr
    log_config["level"] = logging.ERROR
finally:
    logging.basicConfig(**log_config)

LOGGER.info(f"{NAME} v{VERSION} is starting")

token = "Nzg0MjAxMDI1NDI2ODE3MDY0.X8l2Hg.8FIhiU5BBfkc4g6uDM29KN-IogI"
with Diplomat(token=token) as r:
    pass
