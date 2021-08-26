from astro import astro 
l = """
───▄▀▀▀▀▀───▄█▀▀▀█▄
──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██
──▐▒▒▒▒▒▒▒▒███▌▀▐███
───▌▒▓▒▒▒▒▓▒██▌▀▐██
───▌▓▐▀▀▀▀▌▓─▀▀▀▀▀
"""

@astro.on(admin_cmd(pattern="lion ?(.*)"))
async def lion(astro):
      await astro.edit(l)