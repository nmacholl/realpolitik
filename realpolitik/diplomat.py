import discord
import logging

from realpolitik.command import parse_command, CommandContext
from realpolitik.handlers import DM_COMMAND_HANDLER, CHANNEL_COMMAND_HANDLER


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
            f"Created {__class__.__name__} with token {token[0:3]}{'*'*56}"
        )

    def run(self):
        self.logger.info(f"Starting {__class__.__name__}")
        self.client.run(self.token, bot=True)

    def __register_events__(self):
        @self.client.event
        async def on_message(message: discord.Message):
            if message.author == self.client.user:
                return

            if not message.content.startswith("!"):
                return

            self.logger.info(
                f'Processing command from user {message.author}: "{message.content}"'
            )
            command, args = parse_command(message.content)

            context = CommandContext(
                client=self.client, message=message, arguments=args
            )

            if isinstance(message.channel, discord.DMChannel):
                if command in DM_COMMAND_HANDLER:
                    logging.debug(
                        f'Handling private message command: {command} {", ".join(args)}'
                    )
                    await DM_COMMAND_HANDLER[command](context)
                    return

            if isinstance(message.channel, discord.TextChannel):
                if command in CHANNEL_COMMAND_HANDLER:
                    logging.debug(
                        f'Handling channel command: {command} {", ".join(args)}'
                    )
                    await CHANNEL_COMMAND_HANDLER[command](context)
                    return

            logging.info(f"Dropping unknown command: {command}")
