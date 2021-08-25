

"""
Echoes the message via your bot
"""

from astro import CMD_HELP


@astro.on(admin_cmd(pattern=r"echo (.*)"))
@astro.on(sudo_cmd(pattern=r"echo ( .*)", allow_sudo=True))
async def _(event):
    bxt = Config.BOT_USERNAME
    try:
        tex = str(event.text[6:])
        await tgbot.send_message(event.chat_id, tex)
        await event.delete()
    except BaseException:
        await event.client.send_message(event.chat_id, f"Please add @{bxt} here first!")
        await event.delete()


CMD_HELP.update(
    {
        "echo": ".echo <mssg>\nUse - Echoes the message via your bot.ADD YOUR BOT TOO"
    }
)
