import json
from hata import discord

SLEEP = discord.User.precreate(385575610006765579)
FEMBOT = discord.User.precreate(800526029969555456)
DUNGEON = discord.Guild.precreate(388267636661682178)
TESTING = discord.Guild.precreate(729426764652347486)

GREEN = 0x34eb6b
RED = 0xeb4034

KISS_IMAGES = (
    'https://media1.tenor.com/images/bb91ac9f2169548bbae300ecd21f4e77/tenor.gif?itemid=19762150',
    'https://media1.tenor.com/images/fa4ec9dd7ba5b3559700edf7b1ac2522/tenor.gif?itemid=9124289',
    'https://media1.tenor.com/images/3dae6c0f04315b273587d8c23311bcc4/tenor.gif?itemid=10078290',
    'https://media1.tenor.com/images/37fef4ddbf25ca7321deb9723c31cbc1/tenor.gif?itemid=18871882',
    'https://media1.tenor.com/images/19dbe8dd384166af181d06b9fb02e028/tenor.gif?itemid=5982180',
    'https://media1.tenor.com/images/4ad93cee6ac511788ed54a993a8c0eb5/tenor.gif?itemid=7358012',
    'https://media1.tenor.com/images/ec216114884c59a90b1de75e3e6750b4/tenor.gif?itemid=6047650',
    'https://media1.tenor.com/images/d2ea8149b5afe52592a4efa449f25cf5/tenor.gif?itemid=9003999',
    'https://media1.tenor.com/images/efd95d7439962fb9369f227cac3d51b2/tenor.gif?itemid=18385206',
    'https://media1.tenor.com/images/be62e1f84ae18a71ece942f774d61267/tenor.gif?itemid=19330879',
    'https://media1.tenor.com/images/13c163a5e5988ba216378b34751fce65/tenor.gif?itemid=6056284',
    'https://media1.tenor.com/images/2d195925d2b671205a47d398b4e1395a/tenor.gif?itemid=18954799'
)

CAT_BOYS = (
    'https://media1.tenor.com/images/e82ea2acdaff05417b2b28daf95aa966/tenor.gif?itemid=19423064',
    'https://media1.tenor.com/images/f6cd310cff3a86b64a548bed86575468/tenor.gif?itemid=14321810',
    'https://media1.tenor.com/images/3d05c293d0df5f165c6c0e891e9a0457/tenor.gif?itemid=20199733',
    'https://media1.tenor.com/images/96a458e8575b4dd1118aea645f9cb1cb/tenor.gif?itemid=16181878',
    'https://media1.tenor.com/images/542339c921a93e717373784c59935bb5/tenor.gif?itemid=19202127',
)

with open('fembot/setup.json') as fp:
    SETUP = json.load(fp)
