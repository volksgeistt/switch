import asyncio
import aiohttp
import json
from itertools import cycle
import logging
from contextlib import suppress
import pyfiglet
import shutil
from colorama import init, Fore, Style

class Switch:
    def __init__(self):
        self.loadConfig()
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        self.session = None

    def loadConfig(self):
        with open('userAccounts.json') as f:
            config = json.load(f)
            self.accounts = config['accounts']
            self.interval = config.get('interval', 10)

    async def updateAccountSettings(self, user_token, settings):
        url = "https://discord.com/api/v10/users/@me/settings"
        async with self.session.patch(url, headers={'Authorization': user_token}, json=settings) as r:
            if r.status != 200:
                logging.error(f"{Fore.RED}Failed to update settings for token ...{user_token[-8:]} Code: {r.status}")
            else:
                logging.info(f"{Fore.GREEN}Updated settings for token ...{user_token[-8:]}{Fore.RESET}{Fore.YELLOW}: {settings}")

    async def switchAccountSettings(self, user_token, settings_list):
        settingCycle = cycle(settings_list)
        while True:
            settings = next(settingCycle)
            await self.updateAccountSettings(user_token, settings)
            await asyncio.sleep(self.interval)

    async def run(self):
        self.session = aiohttp.ClientSession()
        try:
            tasks = [self.switchAccountSettings(account['userToken'], account['settingsList']) 
                     for account in self.accounts]
            await asyncio.gather(*tasks)
        finally:
            await self.session.close()

    @staticmethod
    def switchWorkLOL():
        init()
        terminalWidth = shutil.get_terminal_size().columns
        asciiArt = pyfiglet.figlet_format("Switch")
        coloredAsciiArt = Fore.MAGENTA + asciiArt + Style.RESET_ALL
        centeredAsciiArt = "\n".join(line.center(terminalWidth) for line in coloredAsciiArt.split("\n"))
        print(centeredAsciiArt)
        authorName = "[ by - volksgeistt ]"
        aboutSwitch = "Switch - An Advance Status Shifter"
        print(aboutSwitch.center(terminalWidth))
        print(authorName.center(terminalWidth))
        print()

if __name__ == "__main__":
    Switch.switchWorkLOL()
    with suppress(KeyboardInterrupt):
        asyncio.run(Switch().run())
