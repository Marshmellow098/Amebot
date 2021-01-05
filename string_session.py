#!/usr/bin/env python3

# (c) https://t.me/TelethonChat/37677

# This Source Code Form is subject to the terms of the GNU

# General Public License, v.3.0. If a copy of the GPL was not distributed with this

# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.
try :
from telethon.sync import TelegramClient

from telethon.sessions import StringSession 
except BaseException:

    print("Telethon Not Found. Installing Now.")

    import os

    os.system("pip3 install telethon")

    from telethon.sessions import StringSession

    from telethon.sync import TelegramClient 

print("""Please go-to my.telegram.org and get your app id and api hash""")
______     __    __     ______     ______     ______     ______  

/\  __ \   /\ "-./  \   /\  ___\   /\  == \   /\  __ \   /\__  _\ 

\ \  __ \  \ \ \-./\ \  \ \  __\   \ \  __<   \ \ \/\ \  \/_/\ \/ 

 \ \_\ \_\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 

  \/_/\/_/   \/_/  \/_/   \/_____/   \/_____/   \/_____/     \/_/ 

                                                                  





APP_ID = int(input("Enter APP ID here: "))

API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:

    print(client.session.save())
