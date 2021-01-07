"""Contains the `Bot` class."""

import random
import re

from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater


class Bot:
    """Contains methods for initializing and starting this bot."""

    RESPONSES = [
        "Say 'great' again. Say 'great' again, I dare you, I double dare you motherfucker, say great one more Goddamn time!"
    ]

    PATTERN = re.compile(r"^g+r+e+a+t+[\.!]*$", re.IGNORECASE)

    def __init__(self, token):
        """Constructor."""

        self.token = token

    def great_callback(self, update, context):
        """A callback method to run when a `great` message is received."""

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=random.choice(self.RESPONSES),
        )

    def start(self):
        """Starts the bot."""

        updater = Updater(self.token)
        dispatcher = updater.dispatcher

        handler = MessageHandler(Filters.regex(self.PATTERN), self.great_callback)
        dispatcher.add_handler(handler)

        updater.start_polling()
