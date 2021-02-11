from hata import discord
from .. import constants


SAD = (
    'The once was a neko named **{0}**. '
    '**{0}** was **{1}** when it saw the **{2}**, '
    'the **{2}** started **{3}** the neko. The neko tried '
    'to run away from the **{2}** but the **{2}** caught **{0}**. '
    'The neko **{4}** the **{2}** and got away but was '
    'scarred for life.'
)

HAPPY = (
    'There once was a neko named **{0}**. '
    '**{0}** was sad because they hadn\'t '
    'gotten any **{1}** in days. A **{2}** went up '
    'to the neko and asked what was wrong. '
    '**{0}** said that they were fine but the '
    '**{2}** **{3}** **{0}** because they knew something '
    'was wrong. The neko finally told the **{2}** '
    'what was wrong so the **{2}** took **{0}** to **{4}**. '
    'They became best friends forever.'
)


@fembot.client.interactions(guild=constants.DUNGEON)
async def sad_madlib(
    client,
    event,
    name: ('str', 'A name'),
    doing: ('str', 'A verb'),
    creature: ('str', 'A noun'),
    doing_to: ('str', 'A verb'),
    did: ('str', 'A noun')
):
    """
    A sad neko madlib
    """
    return discord.Embed(
        'Sad Madlib',
        SAD.format(
            name, doing, creature, doing_to, did
        ),
        constants.RED
    )


@fembot.client.interactions(guild=constants.DUNGEON)
async def happy_madlib(
    client,
    event,
    name: ('str', 'A name'),
    thing: ('str', 'A noun'),
    creature: ('str', 'A noun'),
    action: ('str', 'A verb'),
    place: ('str', 'A noun')
):
    """
    A happy neko madlib
    """
    return discord.Embed(
        'Happy Madlib',
        HAPPY.format(
            name, thing, creature, action, place
        ),
        constants.GREEN
    )
