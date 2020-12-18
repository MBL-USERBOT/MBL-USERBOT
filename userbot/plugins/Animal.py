
import asyncio
import os
from userbot.utils import mbl_cmd

M = ("┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n" 
     "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
     "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
     "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
     "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n" 
     "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
     "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
     "▕┈╰▏╰╯╰━━━━╯┈┈▏\n")

@mbl.on(mbl_cmd(pattern=r"spong"))
async def kek(mellow):
  await mellow.edit(M)
 
  D = ("╭━┳━╭━╭━╮╮\n"
       "┃┈┈┈┣▅╋▅┫┃\n"
       "┃┈┃┈╰━╰━━━━━━╮\n"
       "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
       "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
       "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
       "╲┃┈┈┈┈╭━┳━━━━╯\n"
       "╲┣━━━━━━┫\n")
       
@mbl.on(mbl_cmd(pattern=r"dog"))
async def dog(dog):
  await dog.edit(D)
  P = ("┈┏━╮╭━┓┈╭━━━━╮\n"
       "┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
       "┈╰┓▋▋┏╯╯╰━━━━╯\n"
       "╭━┻╮╲┗━━━━╮╭╮┈\n"
       "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
       "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
       "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
       "┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")
       
  S = ("▔▔╲╱▔▔▔╲╱▔▔\n"
     "┈╲＿╱╰╮┈╭╯╲＿╱\n"
      "┈┈┈▏▉╮┈╭▉▕\n"
      "┈┈╱╲╰╰┊╯╯╱╲\n"
      "┈╱╰▕╰╰┳╯╯▏╯╲\n"
      "▕╰╰╰╲╰┻╯╱╯╯╯▏\n"
      "▕╰╰╰╰▔▔▔╯╯╯╯▏\n"
      "▕╰╰╰╰╰╮╭╯╯╯╯▏\n"
      "┈╲╭╮┈╰╮╭╯╭╮╱\n"
      "┈┈┫┣╭━━━╮┫┃\n"
      "┈┈┃┃┃┈┈┈┃┃┃\n"
      "┈┈┗┛┛┈┈┈┗┗┛\n")      
      
  
F =(" ╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈\n"
     "▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈\n"
     "▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈\n")
    
E =("┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈\n")
    
H = ("┈┈┈╭━━━━━╮┈┈┈┈┈\n"
     "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
     "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
     "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
      "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
       "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
       "┈┈┈┃┊┃╰━━┫┈HOMER\n"
       "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈\n")
      
    
  
@mbl.on(mbl_cmd(pattern=r"fox"))
async def fox(fox):
  await fox.edit(F)
  
@mbl.on(mbl_cmd(pattern=r"elephant"))
async def elephant(elephant):
  await elephant.edit(E)

  
@mbl.on(mbl_cmd(pattern=r"homer"))
async def homer(homer):
  await homer.edit(H)

@mbl.on(mbl_cmd(pattern=r"pig"))
async def pig(pig):
  await pig.edit(P)
  
@mbl.on(mbl_cmd(pattern=r"sheep"))
async def sheep(sheep):
  await sheep.edit(S)
