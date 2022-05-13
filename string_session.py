
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
SATYABOT = """
"""
print(SATYABOT)
print("""String Generator. ==> SATYABot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.
╭━━━┳╮╱╱╭┳━━━━┳╮╱╭┳━━━┳━╮╱╭╮
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃┃╱┃┃╭━╮┃┃╰╮┃┃
┃╰━╯┣╮╰╯╭┻╯┃┃╰┫╰━╯┃┃╱┃┃╭╮╰╯┃
┃╭━━╯╰╮╭╯╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╰╮┃┃
┃┃╱╱╱╱┃┃╱╱╱┃┃╱┃┃╱┃┃╰━╯┃┃╱┃┃┃
╰╯╱╱╱╱╰╯╱╱╱╰╯╱╰╯╱╰┻━━━┻╯╱╰━╯
╭━━╮╭━━━┳━━━━╮
┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃╭━╮┃┃╱┃┃╱┃┃
┃╰━╯┃╰━╯┃╱┃┃
╰━━━┻━━━╯╱╰╯""")
APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as SATYABOT:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(SATYABOT.session.save())
    print("")
    print("You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions.")
    omk =SATYABOT.send_message("me", f"`{SATYABOT.session.save()}`")
    omk.reply("The above is the `SATYA_STRING` #POWERFUL [SATYABOT](https://t.me/Python_Userbot_Support)"
		)
