from userbot.utils import mbl_cmd

@borg.on(mbl_cmd(pattern=r"hhi ?(.*)"))
async def hhi(event):
    giveVar = event.text
    cat = giveVar[5:6]
    if not cat:
        cat = "🌺"
    ct = giveVar[7:8]
    if not ct:
        ct = "✨"
    await event.edit(
        f"{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{cat}{cat}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n☁☁☁☁☁☁☁☁"
    )
