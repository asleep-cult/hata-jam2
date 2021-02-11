from dateutil import relativedelta
from hata import discord
from datetime import datetime, timedelta
from .. import constants


DAILY_WINDOW = timedelta(days=1)
DAILY_INCREMENT = 100


async def get_catboy(user_id):
    sql = 'SELECT * FROM catboys WHERE user_id = ?'
    cursor = await fembot.db.execute(sql, (user_id,))
    catboy = await cursor.fetchone()
    return catboy


async def create_catboy(user_id):
    sql = \
        'INSERT INTO catboys (user_id, catboy_points, last_claimed) ' \
        'VALUES (?, ?, ?)'
    now = datetime.now().isoformat()
    cursor = await fembot.db.execute(sql, (user_id, DAILY_INCREMENT, now))
    await fembot.db.commit()
    return cursor


async def increment_catboy(user_id):
    sql = \
        'UPDATE catboys SET ' \
        f'catboy_points = catboy_points + {DAILY_INCREMENT}, ' \
        'last_claimed = ? WHERE user_id = ?'
    now = datetime.now().isoformat()
    cursor = await fembot.db.execute(sql, (now, user_id))
    await fembot.db.commit()
    return cursor


@fembot.client.interactions(guild=constants.DUNGEON)
async def daily(client, event):
    """
    Claim daily catboy points
    """
    catboy = await get_catboy(event.user.id)

    if catboy is None:
        await create_catboy(event.user.id)
        points = DAILY_INCREMENT
    else:
        time = datetime.fromisoformat(catboy[2])
        window = time + DAILY_WINDOW
        now = datetime.now()

        if window > now:
            remaining = relativedelta.relativedelta(
                seconds=(window - now).total_seconds()
            )
            hours = int(remaining.hours)
            minutes = int(remaining.minutes)
            seconds = int(remaining.seconds)

            time = []
            if hours:
                time.append(f'{hours} hours')
            if minutes:
                time.append(f'{minutes} minutes')
            if seconds:
                time.append(f'{seconds} seconds')

            time = ', '.join(time[:-1]) + f' and {time[-1]}'

            return discord.Embed(
                'Nop, you can\'t do that.',
                f'Try again in {time}',
                constants.RED
            )
        await increment_catboy(event.user.id)
        points = catboy[1] + DAILY_INCREMENT

    return discord.Embed(
        'Noice.',
        f'Good job my catboy... you now have {points} points',
        constants.GREEN
    )


@fembot.client.interactions(guild=constants.DUNGEON)
async def points(
    client,
    event,
    user: ('user', 'The user whose points to show') = None
):
    """
    Shows a users catboy points
    """
    user = user or event.user
    catboy = await get_catboy(user.id)

    embed = discord.Embed()
    if catboy is not None:
        embed.description = f'**Catboy Points**: {catboy[1]}'
        embed.color = constants.GREEN
    else:
        embed.title = 'Nop. Sorry'
        embed.description = 'That user isn\'t in my database of cuties'
        embed.color = constants.RED

    embed.add_author(icon_url=user.avatar_url, name=user.full_name)
    return embed


@fembot.client.interactions(guild=constants.DUNGEON)
async def leaderboard(client, event):
    """
    Shows the catboy leaderboard
    """
    sql = 'SELECT * FROM catboys ORDER BY catboy_points LIMIT 10'
    cursor = await fembot.db.execute(sql)

    embed = discord.Embed(title='OwO', color=constants.GREEN)
    description = []

    for i in range(cursor.arraysize):
        catboy = await cursor.fetchone()
        user = discord.User.precreate(catboy[0])
        description.append(
            f'#{i + 1}: **{user:f}**\n**Points**: {catboy[1]}'
        )

    embed.description = '\n'.join(description)

    return embed
