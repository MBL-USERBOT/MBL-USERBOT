from telethon import events
import asyncio
import os
import sys
from uniborg.util import mbl_cmd

@borg.on(mbl_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("Test Successfull. Boss !")      
