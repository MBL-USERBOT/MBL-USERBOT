from telethon import events
import asyncio
import os
import sys
from telethon import events, functions, __version__
from userbot.utils import mbl_cmd


@borg.on(mbl_cmd(pattern="ftxt"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.edit(pay)
