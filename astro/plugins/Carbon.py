import os
from time import sleep
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from astro import CHROME_DRIVER, GOOGLE_CHROME_BIN
from astro.utils import register

CARBONLANG = "auto"

LANG = "en"


@register(outgoing=True, pattern="^.carbon")
async def carbon_api(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        """ A Wrapper for carbon.now.sh """

        await e.edit("`Processing..`")

        CARBON = "https://carbon.now.sh/?l={lang}&code={code}"

        global CARBONLANG

        textx = await e.get_reply_message()

        pcode = e.text

        if pcode[8:]:

            pcode = str(pcode[8:])

        elif textx:

            pcode = str(textx.message)  # Importing message to module

        code = quote_plus(pcode)  # Converting to urlencoded

        await e.edit("`Creating your Carbon...\n25%`")

        url = CARBON.format(code=code, lang=CARBONLANG)

        chrome_options = Options()

        chrome_options.add_argument("--headless")

        chrome_options.binary_location = GOOGLE_CHROME_BIN

        chrome_options.add_argument("--window-size=1920x1080")

        chrome_options.add_argument("--disable-dev-shm-usage")

        chrome_options.add_argument("--no-sandbox")

        chrome_options.add_argument("--disable-gpu")

        prefs = {"download.default_directory": "./"}

        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)

        driver.get(url)

        await e.edit("`Just Done.......\n50%`")

        download_path = "./"

        driver.command_executor._commands["send_command"] = (
            "POST",
            "/session/$sessionId/chromium/send_command",
        )

        params = {
            "cmd": "Page.setDownloadBehavior",
            "params": {"behavior": "allow", "downloadPath": download_path},
        }

        driver.execute("send_command", params)

        driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()

        # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()

        # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()

        await e.edit("`Finishing Touches..\n75%`")

        # Waiting for downloading

        sleep(2.5)

        await e.edit("`Done Dana Done...\n100%`")

        file = "./carbon.png"

        await e.edit("`Uploading..`")

        await e.client.send_file(
            e.chat_id,
            file,
            caption="<< Here's your carbon, \n Carbonised by [Black Lightning](https://www.github.com/hellboi-atul/hellboi-atul)>> ",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )

        os.remove("./Astro.png")

        driver.quit()

        # Removing carbon.png after uploading

        await e.delete()  # Deleting msg