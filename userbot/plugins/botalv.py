from userbot import *
from PYTHONBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PYTHON"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

python = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={python})"


PM_IMG = "https://telegra.ph/file/00399ad38373f61c5a2ff.jpg"
pm_caption ="**SaTYAẞø✞︎ 𝙸𝚜 𝙾𝚗𝚕𝚒𝚗𝚎**\n\n"

pm_caption += f"**┏━━︎♠️✞t͛ẞ̸ SaTyaẞø✞︎♠️━━┓**\n"
pm_caption += f"**┣🔥 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛    : {mention}**\n"
pm_caption += f"**┣🔥 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 : `{version.__version__}`**\n"
pm_caption += f"**┣🔥 SATYABOT : {PYTHONversion}**\n"
pm_caption += f"**┣🔥 𝚂𝚞𝚍𝚘     : `{sudou}`**\n"
pm_caption += f"**┣🔥 𝙾𝚠𝚗𝚎𝚛     : [Legend-Lx](https://t.me/Its_LegendBoy)**\n"
pm_caption += f"**┗━━━━━[♠️𝙶𝚛𝚘𝚞𝚙♠️](https://t.me/Python_Userbot_Support_Pro)━━━━━━━━┛**\n"

pm_caption += "    [☠️яєρο☠️](https://github.com/SATYA-OP/SATYABOT) 🔹 [📜ℓιϲєиѕє📜](https://github.com/SATYA-OP/SATYABOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="pybot$"))
@bot.on(sudo_cmd(pattern="pybot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("botalv").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'bot', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Are u alive?'
).add()
