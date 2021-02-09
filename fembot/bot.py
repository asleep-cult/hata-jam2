import os
from hata import discord
from hata.ext.extension_loader import EXTENSION_LOADER
from hata.ext.slash import setup_ext_slash
from .database import sql
from .constants import SETUP


class Fembot:
    def __init__(self):
        self.client = discord.Client(SETUP['TOKEN'])
        discord.KOKORO.create_task(self.create_db())
        setup_ext_slash(self.client)

    async def create_db(self):
        self.db_conn = await sql.connect('fembot/database/database.db')
        await self.db_conn.execute(
            'CREATE TABLE IF NOT EXISTS catboys ('
            'user_id INTEGER, catboy_points INTEGER'
            'last_claimed TEXT'
            ')'
        )

fembot = Fembot()

EXTENSION_LOADER.add_default_variables(fembot=fembot.client)

for name in os.listdir('fembot/extensions'):
    if name.endswith('.py'):
        EXTENSION_LOADER.add(f'fembot.extensions.{name[:-3]}')

EXTENSION_LOADER.load_all()
