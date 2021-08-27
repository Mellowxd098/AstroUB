import random
import asyncio
from astro import CMD_HELP
from astro.utils import admin_cmd

STRING = ["HEADS", "TAILS"]

@astro.on(admin_cmd(pattern="flipcoin ?(.*)"))
async def coin(ast):
      await ast.edit("Coin On Flip👀")
      await asyncio.sleep(1)
      await ast.edit("🪙")
      await asyncio.sleep(1)
      await ast.edit("Ohhhhh......\nAnswer is")
      await asyncio.sleep(1)
      await ast.edit(random.choice(STRING))
    
CMD_HELP.update({"coin": ".flipcoin\nUse - Get Random Heads Or Tails"
  
})
# © Astro-UB
