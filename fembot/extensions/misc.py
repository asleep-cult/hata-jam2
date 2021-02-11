import os
import random
from hata import discord
from .. import constants


GAYNESS_LEVELS = {
    constants.FEMBOT.id: 99999999999,
    constants.SLEEP.id: 99999999999
}


@fembot.client.interactions(guild=constants.DUNGEON)
async def kiss(
    client,
    event,
    user: ('user', 'The person you want to kiss')
):
    """
    Kiss someone you big gay
    """
    embed = discord.Embed(
        title=':rainbow_flag: This is so gay... I love it :rainbow_flag:',
        description=f'{event.user:f} kisses {user:f}',
        color=constants.RED
    )
    embed.add_image(random.choice(constants.KISS_IMAGES))
    return embed


@fembot.client.interactions(guild=constants.DUNGEON)
async def catboy(client, event):
    """
    Send's an image of a cute catboy
    """
    embed = discord.Embed(
        title='Here\'s a cute catboy',
        color=constants.GREEN
    )
    embed.add_image(random.choice(constants.CAT_BOYS))
    return embed


@fembot.client.interactions(guild=constants.DUNGEON)
async def gayness(
    client,
    event,
    user: ('user', 'The user whose gayness to show')
):
    """
    Show\'s a user\'s hayness level
    """
    embed = discord.Embed()
    level = GAYNESS_LEVELS.get(user.id)

    if level is None:
        embed.title = \
            'Hmm I don\'t remember them ' \
            'so i\'ve decided to do a re-evaluation'
        level = int(os.urandom(1)[0] * 0.39)
        GAYNESS_LEVELS[user.id] = level
    else:
        embed.title = 'OwO'

    if level > 69:
        embed.description = \
            ':unicorn: :rainbow_flag: ' \
            'They seem a little gay to me ' \
            ':unicorn: :rainbow_flag:\n'
        embed.color = constants.GREEN
    else:
        embed.description = \
            'I hate them entirely, heterosexuality is a sin... ' \
            'but I still support them :man_shrugging:\n'
        embed.color = constants.RED

    embed.description += \
        f':rainbow_flag: Gayness Level: **{level}**% :rainbow_flag:'
    embed.add_author(user.avatar_url, user.full_name)
    embed.add_thumbnail(fembot.client.avatar_url)

    return embed
