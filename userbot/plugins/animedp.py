#Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script
#Usage .animedp Im Not Responsible For Any Ban caused By This

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import mbl_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [
  "pokemon-serena-wallpaper",
  "hd-pokemon-iphone-wallpapers",
  "pokemon-wallpaper-pikachu",
  "doraemon-3d-wallpaper-2018",
  "pokemon-serena-wallpaper",
  "anime-girls-wallpapers"
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
    
@borg.on(mbl_cmd(pattern="animedp ?(.*)"))
async def main(event):
    await event.edit("**Started Anime Profile Pic\n\n Check Your Dp**")    
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(900) #Edit This To Your Required need

