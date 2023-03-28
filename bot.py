import os 
import logging 
import logging.config
from pyrogram import Client 

logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR) 

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5287314321:AAFNRWNo-hGRHibmBKFSFgxPyw9B3oSTQo0")

API_ID = int(os.environ.get("API_ID", "13132442"))

API_HASH = os.environ.get("API_HASH", "54484b8b13b1c2357b6087b196510e21")

FORCE_SUB = os.environ.get("FORCE_SUB", "PhoenixBotz")           

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username 
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)
            self.invitelink = link
         except Exception as e:
            logging.warning(e) 
            logging.warning("Make Sure Bot admin in force sub channel") 
            self.force_channel = None
       logging.info(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
        
    async def stop(self, *args):
      await super().stop()
      logging.info("Bot Stopped")
        
bot = Bot()
bot.run()
