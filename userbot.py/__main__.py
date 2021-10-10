from userbot import bot
from sys import argv
import sys
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module, start_assistant, load_addons
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
            LOGS.info("🐍 Starting PythonBot 🐍")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 PythonBot Startup Completed 🔥")
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

async def assistant():
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

addon = os.environ.get("BOY_OR_GIRL") or False    
if "BOY" in addon:
    addon = addon.replace("BOY", "Boy")            
async def addons():
    if addon == "Boy":
        extra_repo = "https://github.com/LEGEND-LX/PYTHONBOT.py.pkg"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "PythonBot-Addons/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[PYTHON-BOT 9.0.8] - Addons -  ✅Installed✅ - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[PYTHON-BOT 9.0.8] - Addons - ⚠️ERROR⚠️ - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")

bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(assistant())

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


bot.loop.create_task(python_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
