"""main.py"""

import os

from saywhatagainbot import Bot

if __name__ == "__main__":
    bot = Bot(os.environ.get("TOKEN"))
    bot.start()
