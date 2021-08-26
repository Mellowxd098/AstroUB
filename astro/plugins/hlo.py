from astro import bot as astro 
from astro import CMD_HELP

a = """

╔╗─╔╗──╔╗╔╗
║║─║║──║║║║
║╚═╝╠══╣║║║╔══╗
║╔═╗║║═╣║║║║╔╗║
║║─║║║═╣╚╣╚╣╚╝║
╚╝─╚╩══╩═╩═╩══╝
"""

@astro.on(admin_cmd(pattern=r"hello ?(.*)"))
async def hello(astro):
      await astro.edit(a)
      
CMD_HELP.update({"hello": ".hello\nUse - Just a simple Hello"})