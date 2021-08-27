import asyncio

from astro import CMD_HELP
from astro.utils import admin_cmd


@astro.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "shadi":

        await event.edit(input_str)

        animation_chars = [
            "`HEHE U NAUGHTY BOY NEED GIRLFRIEND`",
            "`OK BRO BHAI KE LIYE KUCH BHI`",
            "`GO TO ASTRO SPAM BRUH THERE U WILL GET ADORABLE GIRLBUT DONT MESS WITH THEM BRUH `"
            "`DONT ABUSE AND FIRST DEPLOY ASTRO USERBOT THEN ONLY GO TO THIS GROUP🙂\nNOW TAKE THIS LINK AND ENJOY NOOB ; https://t.me/Astro_Spam .🙂",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


CMD_HELP.update({"SHADI": ".SHADI\nUse - Animation Plugin."})
