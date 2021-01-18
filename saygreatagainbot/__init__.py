"""Contains the `Bot` class."""

import os
import random
import re

from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from typing import List


class Bot:
    """Contains methods for initializing and starting this bot."""

    RESPONSES: List[str] = [
        "Say 'great' again. Say 'great' again, I dare you, I double dare you motherfucker, say great one more Goddamn time!"
    ]

    IMAGES: List[str] = os.listdir("images")

    PATTERN: re.Pattern = re.compile(r"^g+r+e+a+t+[\.!]*$", re.IGNORECASE)

    def __init__(self, token: str) -> None:
        """Constructor."""

        self.token = token

    def great_callback(
        self,
        update: Update,
        context: CallbackContext,
    ) -> None:
        """A callback method to run when a `great` message is received."""

        reply_method = random.choice([self.reply_with_message, self.reply_with_image])
        reply_method(update, context)

    def reply_with_image(self, update: Update, context: CallbackContext):
        """Replies to a `great` message with an image."""

        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(f"images/{random.choice(self.IMAGES)}", mode="rb"),
            reply_to_message_id=update.message.message_id,
        )

    def reply_with_message(self, update: Update, context: CallbackContext):
        """Replies to a `great` message with a message."""

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            reply_to_message_id=update.message.message_id,
            text=random.choice(self.RESPONSES),
        )

    def start(self) -> None:
        """Starts the bot."""

        updater = Updater(self.token)
        dispatcher = updater.dispatcher

        handler = MessageHandler(Filters.regex(self.PATTERN), self.great_callback)
        dispatcher.add_handler(handler)

        updater.start_polling()
        updater.idle()
