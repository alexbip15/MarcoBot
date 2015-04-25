#!/usr/bin/env python

from src.bot import *
from src.config.twitch_credentials import twitch_credentials
from src.config.config import *

bot = MarcoBot(config, twitch_credentials).run()
