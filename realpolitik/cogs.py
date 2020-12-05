import logging
from typing import Dict

import diplomacy
import discord

from discord.ext import commands

from config import NAME, DESCRIPTION, VERSION

LOGGER = logging.getLogger()


class Info(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def about(self, context: commands.context.Context, *, member: discord.Member = None):
        """
        The about command returns a short description of the bot.
        This message replies in a DM to the author.

        :type context: commands.context.Context
        :param context: The command context.
        :type member: discord.Member
        :param member: The user who invoked the command.
        """
        reply = f"{NAME} v{VERSION}\n{DESCRIPTION}"
        await context.author.send(reply)


class Matchmaking(commands.Cog):

    def __init__(self, bot: commands.Bot, match_make_channel_name: str = "matchmaking"):
        self.bot: commands.Bot = bot
        self.game_number: int = 0
        self.match_make_channel_name = match_make_channel_name
        self.lobbies: Dict[int, diplomacy.Game] = {}

    @commands.command()
    async def create(self, context: commands.context.Context, *, member: discord.Member = None):
        """
        The create command will create a new diplomacy game.

        :type context: commands.context.Context
        :param context: The command context.
        :type member: discord.Member
        :param member: The user who invoked the command.
        """
        if isinstance(context.channel, discord.DMChannel) or context.channel.name != self.match_make_channel_name:
            reply = f"The `{self.bot.command_prefix}{context.command}` command can only be used in the " \
                    f"{self.match_make_channel_name} channel."
            try:
                await context.message.delete()
            except discord.HTTPException as e:
                pass
            finally:
                await context.author.send(reply)
                return

        n = self.game_number
        self.game_number += 1

        game_name = f"{context.author}_{n}"
        reason = f"User {context.author} instantiated a new game."

        game = diplomacy.Game(game_id=game_name)
        self.lobbies[n] = game

        category = await context.guild.create_category(name=game_name, reason=reason)
        await context.guild.create_text_channel(name=game.game_id, category=category, reason=reason)
        await context.guild.create_voice_channel(name="public", category=category, reason=reason)

    @commands.command()
    async def join(self, context: commands.context.Context, *, member: discord.Member = None):
        """
        The join command will add the user to an existing diplomacy game.

        :type context: commands.context.Context
        :param context: The command context.
        :type member: discord.Member
        :param member: The user who invoked the command.
        """
        pass

    @commands.command()
    async def resign(self, context: commands.context.Context, *, member: discord.Member = None):
        """
        The resign command will remove the user from their current game; this counts as defeat.

        :type context: commands.context.Context
        :param context: The command context.
        :type member: discord.Member
        :param member: The user who invoked the command.
        """
        pass
