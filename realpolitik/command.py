import diplomacy

from typing import List, Tuple
from definitions import NAME, DESCRIPTION, VERSION


def parse_command(raw_message: str) -> Tuple[str, List[str]]:
    message_split = raw_message.split()

    command = message_split[0].lower()[1:]
    args = message_split[1:]

    return command, args


def about(*args) -> str:
    return f"{NAME} v{VERSION}\n{DESCRIPTION}\nTry !help for a list of commands."


def cmd_help(*args) -> str:
    return (
        f"Direct message commands: {', '.join(DM_COMMAND_HANDLER.keys())}\n"
        f"Text channel commands: {', '.join(CHANNEL_COMMAND_HANDLER)}"
    )


def game(*args) -> str:
    pass


def join(*args) -> str:
    pass


def resign(*args) -> str:
    pass


DM_COMMAND_HANDLER = {
    "about": about,
    "help": cmd_help,
}

CHANNEL_COMMAND_HANDLER = {
    "game": game,
    "join": join,
    "resign": resign,
}
