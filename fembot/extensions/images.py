import random
from hata import discord
from .. import constants

fembot: discord.Client

GAYNESS_LEVELS = {
    385575610006765579: 999999999,
    800526029969555456: 999999999999999999
}

KISS_IMAGES = (
    'https://media1.tenor.com/images/bb91ac9f2169548bbae300ecd21f4e77/tenor.gif?itemid=19762150', # noqa
    'https://media1.tenor.com/images/fa4ec9dd7ba5b3559700edf7b1ac2522/tenor.gif?itemid=9124289', # noqa
    'https://media1.tenor.com/images/3dae6c0f04315b273587d8c23311bcc4/tenor.gif?itemid=10078290', # noqa
    'https://media1.tenor.com/images/37fef4ddbf25ca7321deb9723c31cbc1/tenor.gif?itemid=18871882', # noqa
    'https://media1.tenor.com/images/19dbe8dd384166af181d06b9fb02e028/tenor.gif?itemid=5982180', # noqa
    'https://media1.tenor.com/images/4ad93cee6ac511788ed54a993a8c0eb5/tenor.gif?itemid=7358012', # noqa
    'https://media1.tenor.com/images/ec216114884c59a90b1de75e3e6750b4/tenor.gif?itemid=6047650', # noqa
    'https://media1.tenor.com/images/d2ea8149b5afe52592a4efa449f25cf5/tenor.gif?itemid=9003999', # noqa
    'https://media1.tenor.com/images/efd95d7439962fb9369f227cac3d51b2/tenor.gif?itemid=18385206', # noqa
    'https://media1.tenor.com/images/be62e1f84ae18a71ece942f774d61267/tenor.gif?itemid=19330879', # noqa
    'https://media1.tenor.com/images/13c163a5e5988ba216378b34751fce65/tenor.gif?itemid=6056284', # noqa
    'https://media1.tenor.com/images/2d195925d2b671205a47d398b4e1395a/tenor.gif?itemid=18954799' # noqa
)

CAT_BOYS = (
    'https://media1.tenor.com/images/e82ea2acdaff05417b2b28daf95aa966/tenor.gif?itemid=19423064', # noqa
    'https://media1.tenor.com/images/f6cd310cff3a86b64a548bed86575468/tenor.gif?itemid=14321810', # noqa
    'https://media1.tenor.com/images/3d05c293d0df5f165c6c0e891e9a0457/tenor.gif?itemid=20199733', # noqa
    'https://media1.tenor.com/images/96a458e8575b4dd1118aea645f9cb1cb/tenor.gif?itemid=16181878', # noqa
    'https://media1.tenor.com/images/542339c921a93e717373784c59935bb5/tenor.gif?itemid=19202127', # noqa
)


@fembot.interactions(guild=constants.DUNGEON) # noqa
async def gayness(
    client,
    event,
    user: ('user', 'The User whose gayness to show') # noqa
):
    """
    Show's a User's gayness level
    """
    gay = GAYNESS_LEVELS.get(user.id)
    if gay is None:
        gay = random.randint(0, 100)
        GAYNESS_LEVELS[user.id] = gay
        title = \
            'Hmm I don\'t remember them ' \
            'so i\'ve decided to do a re-evaluation'
    else:
        title = 'OwO'

    if gay < 69:
        color = constants.RED
        description = \
            'I hate them entirely, heterosexuality is a sin... ' \
            'but I still support them :man_shrugging:\n' \
            f':rainbow_flag: Gayness Level: **{gay}**% :rainbow_flag:'
    else:
        color = constants.GREEN
        description = \
            'Looking like a homosexual king to me\n' \
            f':rainbow_flag: Gayness Level: **{gay}**% :rainbow_flag:'

    embed = discord.Embed(title=title, description=description, color=color)
    embed.add_author(user.avatar_url, user.full_name)
    embed.add_thumbnail(fembot.avatar_url) # noqa
    return embed


@fembot.interactions(guild=constants.DUNGEON) # noqa
async def kiss(
    client,
    event,
    user: ('user', 'The person you wan\'t to kiss') # noqa
):
    """
    Kiss someone you big gay
    """
    embed = discord.Embed(
        title=':rainbow_flag: This is so gay... I love it :rainbow_flag:',
        description=f'{event.user:f} kisses {user:f}',
        color=constants.RED
    )
    image = random.choice(KISS_IMAGES)
    embed.add_image(image)
    return embed


@fembot.interactions(guild=constants.DUNGEON) # noqa
async def catboy(client, event):
    """
    Send's an image of a cute catboy
    """
    embed = discord.Embed(
        title='Here\'s a cute catboy',
        color=constants.GREEN
    )
    image = random.choice(CAT_BOYS)
    embed.add_image(image)
    return embed
