"""Emoji
Available Commands:
click gift as soon as fast as possible
.game
build by @Hack12R.."""
from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    input_str = event.pattern_match.group(1)
    if input_str == "game":
        await event.edit(input_str)
        animation_chars = [
       
            "**Welcome To Hardcore Repo Game**",
            "**Click The Gift As Fast As Possible**",
            "**Game Starts in 3**",
            "**Game Starts in 2**",
            "**Game Starts in 1**",    
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆[🎁](https://github.com/Hack12R/HardcoreUserbot/)🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆[🎁](https://github.com/Hack12R/HardcoreUserbot/)🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇[🎁](https://github.com/Hack12R/HardcoreUserbot/)🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆[🎁](https://github.com/Hack12R/HardcoreUserbot/)🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n[🎁](https://github.com/Hack12R/HardcoreUserbot/)🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇[🎁](https://github.com/Hack12R/HardcoreUserbot)\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇",
            "**Game Over**"
 ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 14])
