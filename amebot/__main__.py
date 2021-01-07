from amebot import ALIVE_PIC
from amebot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from amebot.utils import load_module
from amebot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Pach
import asyncio
import telethon.utils

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Work Done with no errors")
        print("Starting Amebot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    
import glob
pach = 'amebot/plugins/*.py'
files = glob.glob(pach)
for name in files:
    with open(name) as f:
        pach1 = Pach(f.name)
        shortname = pach1.stem
        load_module(shortname.replace(".py", ""))
        
if ALIVE_PIC is not None:
    print("""╔═══╗─────╔╗────╔╗
             ║╔═╗║─────║║───╔╝╚╗
             ║║─║╠╗╔╦══╣╚═╦═╩╗╔╝
             ║╚═╝║╚╝║║═╣╔╗║╔╗║║
             ║╔═╗║║║║║═╣╚╝║╚╝║╚╗
             ╚╝─╚╩╩╩╩══╩══╩══╩═╝""")
import amebot._core
print("Bot is ready for helping u try it wiyh `.alive` or `.help`!!")
print("Join `@Amebotsupport` we are always there to help you !!")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
