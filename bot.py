import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6649234939:AAECrHYBAhNXapW85iFOdzMt5iANOfaqHXM")

API_ID = int(os.environ.get("API_ID", "22286588"))

API_HASH = os.environ.get("API_HASH", "60eba49b796e171d3132f970c158d11c")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
