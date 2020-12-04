import discord
import logging

from realpolitik.command import (
    DM_COMMAND_HANDLER,
    parse_command,
    CHANNEL_COMMAND_HANDLER,
)


class Diplomat:
    def __init__(self, token: str):
        self.logger = logging.getLogger()

        self.client = discord.Client()
        self.__register_events__()

        if not isinstance(token, str):
            raise TypeError(
                f"A string token is required when constructing {__class__.__name__}"
            )

        self.token = token
        self.logger.info(
            f'Created {__class__.__name__} with token {token[0:14]}{"*"*45}'
        )

    def __enter__(self):
        self.client.run(self.token, bot=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def __register_events__(self):
        @self.client.event
        async def on_message(message: discord.Message):
            if message.author == self.client.user:
                return

            if not message.content.startswith("!"):
                return

            self.logger.debug(
                f'Processing command from user {message.author}: "{message.content}"'
            )
            command, args = parse_command(message.content)

            if isinstance(message.channel, discord.DMChannel):
                if command in DM_COMMAND_HANDLER:
                    logging.debug(
                        f'Handling private message command: {command} {", ".join(args)}'
                    )
                    result = DM_COMMAND_HANDLER[command](*args)
                    await message.channel.send(result)
                    return

            if isinstance(message.channel, discord.TextChannel):
                if command in CHANNEL_COMMAND_HANDLER:
                    logging.debug(
                        f'Handling channel command: {command} {", ".join(args)}'
                    )
                    result = CHANNEL_COMMAND_HANDLER[command](*args)
                    await message.channel.send(result)
                    return

            logging.debug(f"Dropping unknown command: {command}")
