# -*- coding: utf-8 -*-

"""
“Commons Clause” License Condition v1.0
Copyright Oli 2019-2020

The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.

Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.

For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.

Software: PartyBot (fortnitepy-bot)

License: Apache 2.0
"""

# System imports.
from typing import Optional, Union

# Third party imports.
from fortnitepy.ext import commands

import fortnitepy
import aiohttp


class ClientCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.dm_only()
    @commands.command(
        description="[Client] Sends and sets the status.",
        help="Sends and sets the status.\n"
             "Example: !status Presence Unknown"
    )
    async def status(self, ctx: fortnitepy.ext.commands.Context, *, content: str) -> None:
        await self.bot.set_presence(content)

        await ctx.send(f'Status set to {content}')
        print(self.bot.message % f'Status set to {content}.')

    @commands.dm_only()
    @commands.command(
        description="[Client] Sets the clients kairos/PartyHub avatar.",
        help="Sets the clients kairos/PartyHub avatar.\n"
             "Example: !avatar stw_soldier_f"
    )
    async def avatar(self, ctx: fortnitepy.ext.commands.Context, kairos_cid: str) -> None:
        kairos_avatar = fortnitepy.Avatar(
            asset=kairos_cid
        )

        self.bot.set_avatar(kairos_avatar)

        await ctx.send(f'Kairos avatar set to {kairos_cid}.')
        print(self.bot.message % f'Kairos avatar set to {kairos_cid}.')

    @commands.dm_only()
    @commands.command(
        aliases=['clear'],
        description="[Client] Clears command prompt/terminal.",
        help="Clears command prompt/terminal.\n"
             "Example: !clean"
    )
    async def clean(self, ctx: fortnitepy.ext.commands.Context) -> None:
        os.system('cls' if 'win' in sys.platform else 'clear')

        print(crayons.cyan(self.bot.message % f'Sono bello come Raulo. '
                           'vegovegovego.'))
        print(crayons.cyan(
            self.bot.message % f'Ciao voi chi siete'))

        await ctx.send('Command prompt/terminal cleared.')
        print(self.bot.message % f'Command prompt/terminal cleared.')

    @commands.dm_only()
    @commands.command(
        description="[Client] Sends and sets the status to away.",
        help="Sends and sets the status to away.\n"
             "Example: !away"
    )
    async def away(self, ctx: fortnitepy.ext.commands.Context) -> None:
        await self.bot.set_presence(
            status=self.bot.status,
            away=fortnitepy.AwayStatus.AWAY
        )

        await ctx.send('Status set to away.')
        print(self.bot.message % f'Status set to away.')

    @commands.dm_only()
    @commands.command(
        aliases=['updates'],
        description="[Client] Sends the most recent commit/s.",
        help="Sends the most recent commit/s.\n"
             "Example: !update"
    )
    async def update(self, ctx: fortnitepy.ext.commands.Context) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method="GET",
                url="https://api.github.com/repos/xMistt/fortnitepy-bot/commits/master"
            ) as request:
                data = await request.json()

        date = fortnitepy.Client.from_iso(data['commit']['committer']['date'])
        pretty_date = f'{date.day}/{date.month}/{date.year} @ {date.hour}:{date.minute}'
        commit_title = data['commit']['message'].split('\n')[0]

        await ctx.send(f"Last commit by {data['committer']['login']} made on {pretty_date}:\n"
                       f"[{data['sha'][0:7]}] {commit_title}")

        print(self.bot.message % f'Sent last commit information.')
