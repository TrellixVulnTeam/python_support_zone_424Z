from . import *
import asyncio
import random
from telethon import events
from PYTHONBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PYTHON"
from userbot.Config import Config
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG
# Thanks to PYTHON BRO.. 
# animation Idea by @Legendl_Mr_Hacker (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 5
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/cab7a726ba2b03b19059f.jpg"
file2="https://telegra.ph/file/fb22904a6aa14a9e09e47.jpg"
file3="https://telegra.ph/file/6b1929b5e93c38a03fb8c.jpg"
file4="https://telegra.ph/file/83570ffd11ebd2dbe2bf3.jpg"
file5="https://telegra.ph/file/bf2c1a5ed662878104c0c.jpg"""" =======================CONSTANTS====================== """
pm_caption = "     **🔥『PYTHONẞø†』🔥**\n\n"
pm_caption += f"**{CUSTOM_ALIVE_TEXT}**\n\n"
pm_caption += "༆༄🎀🌹Åbôût Mê \n\n"
pm_caption += "💫💫**✞︎t͛ẞ̸ SaTyaẞø†**💫💫 >>》 V•1\n"
pm_caption += "😇😇**Dark-LegendPro**😇😇   >>》 [Owner](https://t.me/Its_LegendBoy)\n"
pm_caption += f"🔰🔰**Mâßtêř**🔰🔰  >>》 {python_mention}\n"
pm_caption += "❣❣ *SaTyaẞø✞︎**❣❣ >>》 [𝕲𝖗ουρ](https://t.me/Python_Userbot_Support_Pro)\n\n"
pm_caption += "🎊🎊 **Řepô**🎊🎊  >>》 [𝕽єρο](https://github.com/SATYA-OP/SATYABOT)\n\n"
pm_caption += "[....▄███▄███▄\n....█████████\n.......▀██❣🌹💫😇💫🌹❣███▀\n...............▀█▀\n](https://t.me/Its_Legendboy)\n\n"
@borg.on(admin_cmd(pattern=r"abot"))
@bot.on(sudo_cmd(pattern="python$", allow_sudo=True))
async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("about").add_command(
    "abot", None , "BEST alive command"
).add_type(
    "Official"
).add()
