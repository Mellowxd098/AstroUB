from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("Welcome There✨")
print("")

APP_ID = int(input("Enter API ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    ast = client.send_message("me", f"`{client.session.save()}`")
    ast.reply(
        "The Above is the your `STRING_SESSION` FOR your **AstroUB**\nFor any kind of Help Join ~ @Astro_HelpChat")
    print("")
    print("Below is the STRING_SESSION. You can also find it in your Telegram Saved Messages.")
    print("")
    print("")
    print(client.session.save())
