import json
from hata import discord

SLEEP = discord.User.precreate(385575610006765579)
DUNGEON = discord.Guild.precreate(388267636661682178)
TESTING = discord.Guild.precreate(729426764652347486)

with open('fembot/setup.json') as fp:
    SETUP = json.load(fp)