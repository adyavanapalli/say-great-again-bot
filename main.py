"""main.py"""

import os

from saygreatagainbot import Bot

if __name__ == "__main__":
    bot = Bot(os.environ.get("SAY_GREAT_AGAIN_BOT_TOKEN"))
    bot.start()
