import os
from hata import discord
from hata.ext.extension_loader import EXTENSION_LOADER
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from .constants import SETUP

PREFIXES = ['f!', 'femboy!']

fembot = discord.Client(SETUP['TOKEN'], intents=32767)
setup_ext_commands(fembot, PREFIXES)
setup_ext_slash(fembot)

EXTENSION_LOADER.add_default_variables(fembot=fembot)

for name in os.listdir('fembot/extensions'):
    if name.endswith('.py'):
        EXTENSION_LOADER.add(f'fembot.extensions.{name[:-3]}')

EXTENSION_LOADER.load_all()
