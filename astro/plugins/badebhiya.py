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

    if input_str == "ro_mut_bhai":

        await event.edit(input_str)

        animation_chars = [
            "`BRUH DONT CRY SHE DONT DESERVED U U DESERVED BETTER THAN THAT`",
            "`JUST LEARN SOME ROMANCE TIPS FROM OUR BIG BRO `",
            "`CONTACT LOVERBOY SIR - @LbjiBot`",
            "`HE WILL TEACH U HOW TO ROMANCE AND ALSO WILL HELP U OVERCOME`",
            "`FORGET THAT NIBBI BRUH`",
          
            for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])

            
          CMD_HELP.update({"breakup": ".breakup\nUse - Animation Plugin."})
