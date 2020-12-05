import diplomacy
import discord

from realpolitik.command import command_handler, CommandContext
from definitions import NAME, DESCRIPTION, VERSION


@command_handler
async def about(context: CommandContext):
    """
    The about command returns a small message describing the bot and where to get more information about it.
    This message replies in a DM to the author.
    :param context: The command context.
    :return:
    """
    reply = f"{NAME} v{VERSION}\n{DESCRIPTION}\nTry !help for a list of commands."
    await context.message.author.send(reply)


@command_handler
async def cmd_help(context: CommandContext):
    """
    The about command returns a

    :param context: The command context.
    :return:
    """
    reply = (
        f"Direct message commands: {', '.join(DM_COMMAND_HANDLER.keys())}\n"
        f"Text channel commands: {', '.join(CHANNEL_COMMAND_HANDLER)}"
    )
    await context.message.author.send(reply)

DM_COMMAND_HANDLER = {
    "ABOUT": about,
    "HELP": cmd_help,
}

"""
The following commands are channel commands
"""


@command_handler
def create(context: CommandContext):
    pass


@command_handler
def join(context: CommandContext):
    pass


@command_handler
def resign(context: CommandContext):
    pass


CHANNEL_COMMAND_HANDLER = {
    "CREATE": create,
    "JOIN": join,
    "RESIGN": resign,
}
