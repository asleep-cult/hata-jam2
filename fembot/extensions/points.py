import itertools
from dateutil import relativedelta
from hata import discord
from datetime import datetime
from .. import constants


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
    cursor = await fembot.db.execute(
        sql,
        (user_id, constants.DAILY_INCREMENT, now)
    )
    await fembot.db.commit()
    return cursor


async def increment_catboy(user_id, amount):
    sql = \
        'UPDATE catboys SET ' \
        'catboy_points = catboy_points + ?, ' \
        'last_claimed = ? WHERE user_id = ?'
    now = datetime.now().isoformat()
    cursor = await fembot.db.execute(
        sql,
        (amount, now, user_id)
    )
    await fembot.db.commit()
    return cursor


async def decrement_catboy(user_id, amount):
    sql = \
        'UPDATE catboys SET ' \
        'catboy_points = catboy_points - ? ' \
        'WHERE user_id = ?'
    cursor = await fembot.db.execute(
        sql,
        (amount, user_id)
    )
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
        points = constants.DAILY_INCREMENT
    else:
        time = datetime.fromisoformat(catboy[2])
        window = time + constants.DAILY_WINDOW
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
        await increment_catboy(event.user.id, constants.DAILY_INCREMENT)
        points = catboy[1] + constants.DAILY_INCREMENT

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

    while True:
        catboy = await cursor.fetchone()

        if catboy is None:
            break

        user = discord.User.precreate(catboy[0])
        description.append(
            f'**{user:f}**\n**Points**: {catboy[1]}'
        )

    embed.description = '\n'.join(
        f'#{i}: {v}' for i, v in enumerate(reversed(description), start=1)
    )

    return embed


@fembot.client.interactions(guild=constants.DUNGEON)
async def gift(
    client,
    event,
    user: ('user', 'The user you want to gift to'),
    amount: ('int', 'The amount you want to gift')
):
    """
    Give a user some of your catboy points
    """
    if amount < 0:
        return discord.Embed(
            'Nop.',
            'Stop trying to break me cutie',
            constants.RED
        )

    author_catboy = await get_catboy(event.user.id)

    if author_catboy is None:
        await create_catboy(event.user.id)
        author_catboy = (event.user.id, constants.DAILY_INCREMENT)

    if author_catboy[1] < amount:
        return discord.Embed(
            'Nop.',
            'You don\'t have enough points for that :(',
            constants.RED
        )

    user_catboy = await get_catboy(user.id)

    if user_catboy is None:
        await create_catboy(user.id)
        user_catboy = (user.id, constants.DAILY_INCREMENT)

    await increment_catboy(user.id, amount)
    await decrement_catboy(event.user.id, amount)

    return discord.Embed(
        f'{event.user:f} gifted {user:f} {amount} catboy points',
        f'**{event.user:f}** {author_catboy[1]} -> {author_catboy[1] - amount}\n'
        f'**{user:f}** {user_catboy[1]} -> {user_catboy[1] + amount}'
    )
