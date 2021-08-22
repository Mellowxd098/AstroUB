
import asyncio
import math
import os

import heroku3
import requests

from astro.helps.heroku_helper import HerokuHelper
from astro.utils import admin_cmd, edit_or_reply, sudo_cmd

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@astro.on(admin_cmd(pattern="(logs|log)"))
@astro.on(sudo_cmd(pattern="(logs|log)", allow_sudo=True))
async def giblog(event):
    herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME, Config.HEROKU_API_KEY)
    logz = herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logz)
    await astro.send_file(
        event.chat_id, "logs.txt", caption=f"**Logs Of {Config.HEROKU_APP_NAME}**"
    )


@astro.on(admin_cmd(pattern="(rerun|restarts)"))
@astro.on(sudo_cmd(pattern="(restart|restarts)", allow_sudo=True))
async def restart_me(event):
    herokuHelper = HerokuHelper(Config.HEROKU_APP_NAME, Config.HEROKU_API_KEY)
    await event.edit("`App is Restarting. This is May Take Upto 10Min.`")
    herokuHelper.restart()


@astro.on(admin_cmd(pattern="usage$"))
@astro.on(sudo_cmd(pattern="usage$", allow_sudo=True))
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    await edit_or_reply(dyno, "`Trying To Fetch Dyno Usage....`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await edit_or_reply(
            dyno, "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await edit_or_reply(
        dyno,
        "**Dyno Usage Data**:\n\n"
        f"✗ **APP NAME =>** `{Config.HEROKU_APP_NAME}` \n"
        f"✗ **Usage in Hours And Minutes =>** `{AppHours}h`  `{AppMinutes}m`"
        f"✗ **Usage Percentage =>** [`{AppPercentage} %`]\n"
        "\n\n"
        "✗ **Dyno Remaining This Months 📆:**\n"
        f"✗ `{hours}`**h**  `{minutes}`**m** \n"
        f"✗ **Percentage :-** [`{percentage}`**%**]",
    )


@astro.on(
    admin_cmd(pattern="(set|get|del) Config(?: |$)(.*)(?: |$)([\s\S]*)", outgoing=True)
)
@astro.on(
    sudo_cmd(pattern="(set|get|del) Config(?: |$)(.*)(?: |$)([\s\S]*)", allow_sudo=True)
)
async def Configiable(Config):
    """
    Manage most of ConfigConfigs setting, set new Config, get current Config,
    or delete Config...
    """
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_or_reply(
            Config, "`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**"
        )
    exe = Config.pattern_match.group(1)
    heroku_Config = app.config()
    if exe == "get":
        await edit_or_reply(Config, "`Getting information...`")
        await asyncio.sleep(1.5)
        try:
            Configiable = Config.pattern_match.group(2).split()[0]
            if Configiable in heroku_Config:
                return await edit_or_reply(
                    Config,
                    "**ConfigConfigs**:" f"\n\n`{Configiable} = {heroku_Config[Configiable]}`\n",
                )
            else:
                return await edit_or_reply(
                    Config, "**ConfigConfigs**:" f"\n\n`Error:\n-> {Configiable} don't exists`"
                )
        except IndexError:
            configs = prettyjson(heroku_Config.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await Config.client.send_file(
                        Config.chat_id,
                        "configs.json",
                        reply_to=Config.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await edit_or_reply(
                        Config,
                        "`[HEROKU]` ConfigConfigs:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================",
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        await edit_or_reply(Config, "`Setting information...`")
        Configiable = Config.pattern_match.group(2)
        if not Configiable:
            return await edit_or_reply(Config, ">`.set Config <ConfigConfigs-name> <value>`")
        value = Config.pattern_match.group(3)
        if not value:
            Configiable = Configiable.split()[0]
            try:
                value = Config.pattern_match.group(2).split()[1]
            except IndexError:
                return await edit_or_reply(Config, ">`.set Config <ConfigConfigs-name> <value>`")
        await asyncio.sleep(1.5)
        if Configiable in heroku_Config:
            await edit_or_reply(
                Config, f"**{Configiable}**  `successfully changed to`  ->  **{value}**"
            )
        else:
            await edit_or_reply(
                Config, f"**{Configiable}**  `successfully added with value`  ->  **{value}**"
            )
        heroku_Config[Configiable] = value
    elif exe == "del":
        await edit_or_reply(Config, "`Getting information to deleting Configiable...`")
        try:
            Configiable = Config.pattern_match.group(2).split()[0]
        except IndexError:
            return await edit_or_reply(
                Config, "`Please specify ConfigConfigs you want to delete`"
            )
        await asyncio.sleep(1.5)
        if Configiable in heroku_Config:
            await edit_or_reply(Config, f"**{Configiable}**  `successfully deleted`")
            del heroku_Config[Configiable]
        else:
            return await edit_or_reply(Config, f"**{Configiable}**  `is not exists`")


@astro.on(admin_cmd(pattern="shp ?(.*)"))
async def lel(event):
    cpass, npass = event.pattern_match.group(1).split(" ", 1)
    await event.edit("`Changing You Pass`")
    accountm = Heroku.account()
    accountm.change_password(cpass, npass)
    await event.edit(f"`Done !, Changed You Pass to {npass}")


@astro.on(admin_cmd(pattern="acolb (.*)"))
async def sf(event):
    hmm = event.pattern_match.group(1)
    app = Heroku.app(Config.HEROKU_APP_NAME)
    collaborator = app.add_collaborator(user_id_or_email=hmm, silent=0)
    await event.edit("`Sent Invitation To Accept Your Collab`")


@astro.on(admin_cmd(pattern="tfa (.*)"))
async def l(event):
    hmm = event.pattern_match.group(1)
    app = Heroku.app(Config.HEROKU_APP_NAME)
    transfer = app.create_transfer(recipient_id_or_name=hmm)


@astro.on(admin_cmd(pattern="kd (.*)"))
async def killdyno(event):
    app = Heroku.app(Config.HEROKU_APP_NAME)
    await event.edit("`Dyno Is Off. Manually Turn it On Later`")
    app.kill_dyno("python3 Astrorun.py")


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""

    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0