# CREDITS TO LIGHT YAGAMI 

import asyncio 

from astro import CMD_HELP

@astro.on(admin_cmd(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    animation_interval = 2
    animation_ttl = range(0, 11)
    
    input_str = event.pattern_match.group(1)
    
    if input_str == "breakup":
      
        await event.edit(shadi)
        animation_chars = [
            "`BRUH DONT CRY SHE DONT DESERVED U\nU DESERVED BETTER THAN shadi",
            "\n`JUST LEARN SOME ROMANCE TIPS FROM OUR BIG BRO `",
            "\n`CONTACT LOVERBOY SIR` - @LbjiBot",
            "\n`HE WILL TEACH U HOW TO ROMANCE AND ALSO WILL HELP U OVERCOME`",
            "\n`FORGET THAT NIBBI BRUH`"
          ]
          for i in animation_ttl:
            await event.edit(animation_chars[i % 11])
            await asyncio.sleep(animation_interval)
            
CMD_HELP.update({"Breakup": ".breakup\nUse - Animation Plugin."})
