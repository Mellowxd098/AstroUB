# CREDIT TO LIGHT YAGAMI
import asyncio
from astro import astro, CMD_HELP

@astro.on(admin_cmd(pattern=f"breakup", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("BRUH DONT CRY SHE DONT DESERVED U\n")
    await asyncio.sleep(2)
    await event.edit("U DESERVED BETTER THAN THAT NIBBI\n")
    await asyncio.sleep(2)
    await event.edit("JUST LEARN SOME ROMANCE TIPS FROM OUR BIG BRO\n")
    await asyncio.sleep(2)
    await event.edit("HE WILL TEACH U HOW TO ROMANCE\n")
    await asyncio.sleep(2)
    await event.edit("CONTACT LOVERBOY SIR\n")
    await asyncio.sleep(2)
    await event.edit("FORGET THAT NIBBI BRUH\n")
    await asyncio.sleep(2)
    await event.edit("CONTACT LOVERBOY SIR` - @Astro_Spam\n")
    await asyncio.sleep(1)
  

CMD_HELP.update({"breakup": ".breakup\nUse - Animation Plugin."})
