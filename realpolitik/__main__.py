import argparse
import asyncio
import inspect

import config
import logging
import os
import sys

from discord.ext.commands import Bot

from realpolitik import cogs

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter(config.LOG_FMT)


def is_file(path: str):
    if os.path.isfile(path):
        return path
    raise ValueError(f"{path} is not a path to a file.")


def is_token(token: str):
    if isinstance(token, str) and len(token) == 59:
        return token
    raise ValueError(f"Discord token is invalid.")


async def main():
    parser = argparse.ArgumentParser(
        prog=f"python3 -m {config.NAME}", description=config.DESCRIPTION
    )
    parser.add_argument("token", metavar="T", type=is_token, help="The discord bot token.")
    parser.add_argument("--version", action="version", version=config.VERSION)
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Enables verbose logging to stdout.",
    )
    parser.add_argument(
        "--log_file",
        type=is_file,
        default=config.LOG_FILE_NAME,
        help="A file path to log to. This overrides the configuration log file path.",
    )

    args = parser.parse_args()

    # Configure stderr output
    stderr = logging.StreamHandler(sys.stderr)
    stderr.setLevel(logging.ERROR)
    stderr.setFormatter(log_format)
    logger.addHandler(stderr)

    try:
        os.makedirs(os.path.dirname(args.log_file), exist_ok=True)
        file = logging.FileHandler(filename=args.log_file, mode="a+")
        file.setLevel(logging.DEBUG)
        file.setFormatter(log_format)
        logger.addHandler(file)
    except PermissionError as e:
        args.verbose = True
        logger.exception(e)
        logger.error(f"Could not create log file; verbose mode has been set")

    if args.verbose:
        stdout = logging.StreamHandler(sys.stdout)
        stdout.setLevel(logging.INFO)
        stdout.setFormatter(log_format)
        logger.addHandler(stdout)

    logger.info(f"{config.NAME} v{config.VERSION} is starting")

    bot = Bot(command_prefix="!", description=config.DESCRIPTION)

    for name, cog in inspect.getmembers(cogs, inspect.isclass):
        try:
            bot.add_cog(cog(bot=bot))
            logger.info(f"Added cog {name}")
        except Exception as e:
            logger.exception(e)
            logger.error(f"Failed to add cog {name}")

    task = asyncio.create_task(bot.start(args.token))
    while not bot.is_closed():
        await asyncio.sleep(1, task.get_loop())
        logger.info("Heartbeat")


asyncio.run(main())
