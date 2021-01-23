"""main.py"""

import os

from saygreatagainbot import Bot

if __name__ == "__main__":
    bot = Bot(os.environ.get("BOT_TOKEN"))
    bot.start()
