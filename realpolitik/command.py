import discord
import logging

from dataclasses import dataclass, field
from typing import List, Tuple

LOGGER = logging.getLogger()


@dataclass
class CommandContext:

    client: discord.Client
    message: discord.Message
    arguments: List[str] = field(default_factory=list)


def command_handler(func):
    async def wrapper(context: CommandContext):
        await func(context)
        LOGGER.info(f"Processed command from user {context.message.author}: {func.__name__.upper()}")
    return wrapper


def parse_command(raw_message: str) -> Tuple[str, List[str]]:
    message_split = raw_message.split()

    command = message_split[0].upper()[1:]
    args = message_split[1:]

    return command, args
