from userbot import bot
from sys import argv
import sys
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, PYTHONversion
from pathlib import Path
import asyncio
import glob
import telethon.utils
os.system("pip install -U telethon")

l2= Config.SUDO_COMMAND_HAND_LER
PYTHON_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/75e1eda1498620f0030ea.jpg"
l1 = Config.COMMAND_HAND_LER


LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"PYTHON_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🐍Starting PythonBot🐍")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🔥PythonBot Startup Completed🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()
print("Loading Modules / Plugins")


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))



bot.loop.run_until_complete(module())


print(f""" ╔════❰PYTHOPBOT❱═❍⊱❁۪۪➙𖤍࿐ IS ON!!! PYTHON VERSION :- {PYTHONversion}
TYPE :- " .gpromote @Legendl_Me_Hacker " OR .Alive OR .ping CHECK IF I'M ON!
╔════❰PYTHOPBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - LEGEND-LX
║┣⪼{PYTHON_PIC}
║┣⪼ CREATOR - @Legendl_Mr_Hacker
║┣⪼ TELETHON - 9.2.7JAA
║┣⪼   PYTHON-𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



async def Python_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                Python_PIC,
                caption=f"#START \n\nDeployed PYTHONBOT Successfully\n\n**PYTHONBOT- {PYTHONversion}**\n\nType `{l1}op` or `{l1}alive` to check! \n\nJoin [PythonBot Channel](t.me/Its_LegendBot) for Updates & [PythonBot Chat](t.me/Python_Userbot_Support) for any query regarding PythonBot",
            )
    except Exception as e:
        print(str(e))

# Join PythonBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Its_LegendBot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Python_Userbot_Support"))
    except BaseException:
         pass


bot.loop.create_task(Python_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
