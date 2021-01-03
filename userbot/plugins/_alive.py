import os
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, ALIVE_PIC
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MBL USERBOT"

MBL_PIC="https://telegra.ph/file/feb11d33ab59c6b29099a.jpg"

if ALIVE_PIC is None:
    ALIVE_PIC=MBl_PIC

    ALIVE_PIC=ALIVE_PIC

pm_caption = "**Me IZ 🇲🇧🇱 🇺🇸🇪🇷🇧🇴🇹**\n"
pm_caption += f"**My Master** => **{DEFAULTUSER}**\n\n"
pm_caption += f"**{DEFAULTUSER} i am  alive 😁😁😋😋**\n\n"
pm_caption +=f"**JUST CHILL AND DO WHATEVER YOU WANT TO DO WITH ME😉**\n\n"
pm_caption +=f"**Python Version => 3.9.1**\n\n"
pm_caption +=f"**Telethon Version => 1.15.0**\n\n"
pm_caption +=f"**[Support Group](https://t.me/MBL_GANG_SUPORT_GROUP)**\n\n"
pm_caption +=f"**[Channel for Updates](https://t.me/MBL_GANG_USER_BOT)**\n\n"
pm_caption +=f"**[For  joining MBL GANG ](https://t.me/MORAL_MBL_OWNER)**\n\n"
pm_caption += "[REPO IS HERE](https://github.com/MBL-USERBOT/MBL-USERBOT)**\n\n"
pm_caption +=("╔═╦═╦══╦╗─╔══╦══╦═╦╦══╗\n"
              "║║║║║╔╗║║─║╔═╣╔╗║║║║╔═╣\n"
              "║║║║║╔╗║╚╗║╚╗║╠╣║║║║╚╗║\n"
              "╚╩═╩╩══╩═╝╚══╩╝╚╩╩═╩══╝\n")
@borg.on(admin_cmd(pattern=r"mblalive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=ALIVE_PIC,caption=pm_caption)
    await alive.delete()
