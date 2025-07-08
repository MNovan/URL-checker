import os, re, time, random, threading, requests, easygui
from colorama import Fore
from bs4 import BeautifulSoup

# Credit to Mnovan
# Github: https://github.com/MNovan


# Credit to Pycenter by billythegoat356
# Github: https://github.com/billythegoat356/pycenter/
# License: https://github.com/billythegoat356/pycenter/blob/main/LICENSE

def center(var: str, space: int = None):  # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns- len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
    
    return "\n".join((" " * int(space)) + var for var in var.splitlines())

class URL:

    def __init__(self):
        if os.name == "posix":
            print("WARNING: This program is designed to run on Windows only.")
            quit(1)
        self.proxies = []
        self.combos = []
        self.dead = 0
        self.alive = 0
        self.error = 0
        self.cpm = 0
        self.retries = 0
        self.hr = 0
        self.lock = threading.Lock()

    def ui(self):
        os.system("cls && title [URL CHECKER] - Made by Novan")
        text = """
            
                                                                 
		888b      88                                                     
		8888b     88                                                     
		88 `8b    88                                                     
		88  `8b   88   ,adPPYba,   8b       d8  ,adPPYYba,  8b,dPPYba,   
		88   `8b  88  a8"     "8a  `8b     d8'  ""     `Y8  88P'   `"8a  
		88    `8b 88  8b       d8   `8b   d8'   ,adPPPPP88  88       88  
		88     `8888  "8a,   ,a8"    `8b,d8'    88,    ,88  88       88  
		88      `888   `"YbbdP"'       "8"      `"8bbdP"Y8  88       88  
		                                                                 
                                                                              
        """
        faded = ""
        red = 40
        for line in text.splitlines():
            faded += f"\033[38;2;{red};0;220m{line}\033[0m\n"
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        print(center(faded))
        print(center(f"{Fore.LIGHTYELLOW_EX}\ngithub.com/MNovan\n{Fore.RESET}"))

    def mainui(self):
        while True:
            os.system("cls")
            print(center(f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RESET}"))
            print(center(f"{Fore.RESET}{Fore.LIGHTWHITE_EX}URL CHECKER By. Novan{Fore.RESET}"))
            print(center(f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RESET}"))
            print((f"       {Fore.RESET}Checked                >>  {Fore.LIGHTGREEN_EX}{self.dead + self.alive}/{int(len(self.combos))}{Fore.RESET}"))
            print((f"       {Fore.RESET}Alive                  >>  {Fore.LIGHTGREEN_EX}{self.alive}{Fore.RESET}"))
            print((f"       {Fore.RESET}Dead                   >>  {Fore.LIGHTRED_EX}{self.dead}{Fore.RESET}"))
            print((f"       {Fore.RESET}Retries                >>  {Fore.LIGHTYELLOW_EX}{self.retries}{Fore.RESET}"))
            print(center(f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RESET}"))
            print(center(f"{Fore.RESET}{Fore.LIGHTWHITE_EX}Stats{Fore.RESET}"))
            print(center(f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RESET}"))
            print((f"\n         {Fore.RESET}Alive Rate (HR)      >>  {Fore.LIGHTBLUE_EX}% {self.hr}{Fore.RESET}"))
            time.sleep(0.9)

    def cpmCounter(self):
        while True:
            old = self.alive
            time.sleep(4)
            new = self.alive
            self.cpm = (new - old) * 15
    
    def hrcounter(self):
        while True:
            a = self.alive
            b = self.dead
            self.hr = (a - b) * 0.1

    def updateTitle(self):
        while True:
            elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start))
            os.system(
                f"title [URL CHECKER] - Alive: {self.alive} ^| Dead: {self.dead} ^| Retries: {self.retries} ^| CPM: {self.cpm} ^| Threads: {threading.active_count() - 3} ^| Time elapsed: {elapsed}"
            )
            time.sleep(0.4)


    def getProxies(self):
        try:
            print(f"[{Fore.LIGHTBLUE_EX}>{Fore.RESET}] Path to proxy file> ")
            path = easygui.fileopenbox(
                default="*.txt",
                filetypes=["*.txt"],
                title="URL CHECKER - Select proxy",
                multiple=False,
            )
            try:
                open(path, "r", encoding="utf-8")
            except:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed to open proxyfile")
                os.system("pause >nul")
                quit()

            try:
                choice = int(
                    input(
                        f"[{Fore.LIGHTBLUE_EX}?{Fore.RESET}] Proxy type [{Fore.LIGHTBLUE_EX}0{Fore.RESET}]HTTP/[{Fore.LIGHTBLUE_EX}1{Fore.RESET}]SOCKS4/[{Fore.LIGHTBLUE_EX}2{Fore.RESET}]SOCKS5> "
                    )
                )
            except:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Value must be an integer")
                os.system("pause >nul")
                quit()

            if choice in [0, 1, 2]:
                if choice == 0:
                    proxytype = "http"
                elif choice == 1:
                    proxytype = "socks4"
                elif choice == 2:
                    proxytype = "socks5"
                else:
                    print(
                        f"[{Fore.RED}!{Fore.RESET}] Please enter a valid choice such as 0, 1 or 2!"
                    )
                    os.system("pause >nul")
                    quit()

            with open(path, "r", encoding="utf-8") as f:
                for l in f:
                    proxy = l.strip().split(":")
                    if len(proxy) >= 2:
                        self.proxies.append(
                            {proxytype: f"{proxytype}://{proxy[0]}:{proxy[1]}"}
                        )
        except Exception as e:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {e}")
            os.system("pause >nul")
            quit()

    def getCombos(self):
        try:
            print(f"[{Fore.LIGHTBLUE_EX}>{Fore.LIGHTWHITE_EX}] Path to Url File> ")
            path = easygui.fileopenbox(
                default="*.txt",
                filetypes=["*.txt"],
                title="URL CHECKER - Select combos",
                multiple=False,
            )
            with open(path, "r", encoding="utf-8") as f:
                for l in f:
                    self.combos.append(l.replace("\n", ""))
        except Exception as e:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed to open Url File")
            os.system("pause >nul")
            quit()

    def checker(self, url):
        try:
            req = requests.head(
                url,
                proxies= random.choice(self.proxies),
                timeout= 10,
                allow_redirects= False,
            )
            if req.status_code == 200:
                self.alive += 1
                with open("alive.txt", "a", encoding="utf-8") as fp:
                	fp.writelines([f"{url}\n"])
                self.lock.release()
            else:
                self.lock.acquire()
                self.dead += 1
                self.lock.release()

        except requests.exceptions.RequestException:
            self.lock.acquire()
            self.retries += 1
            self.lock.release()
        except Exception as e:
            self.lock.acquire()
            self.retries += 1
            self.lock.release()

    def worker(self, combos, thread_id):
        while self.check[thread_id] < len(combos):
            combination = combos[self.check[thread_id]].strip()
            self.checker(combination)
            self.check[thread_id] += 1

    def main(self):
        self.ui()
        self.getProxies()
        self.getCombos()
        try:
            self.threadcount = int(
                input(f"[{Fore.LIGHTBLUE_EX}>{Fore.RESET}] Threads> ")
            )
        except ValueError:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Value must be an integer")
            os.system("pause >nul")
            quit()

        self.start = time.time()
        threading.Thread(target=self.cpmCounter, daemon=True).start()
        threading.Thread(target=self.updateTitle, daemon=True).start()
        threading.Thread(target=self.mainui, daemon=True).start()
        threading.Thread(target=self.hrcounter, daemon=True).start()

        threads = []
        self.check = [0 for i in range(self.threadcount)]
        for i in range(self.threadcount):
            sliced_combo = self.combos[
                int(len(self.combos) / self.threadcount * i) : int(
                    len(self.combos) / self.threadcount * (i + 1)
                )
            ]
            t = threading.Thread(
                target=self.worker,
                args=( 
                    sliced_combo,
                    i,
                ),
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f"[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Task completed")
        os.system("pause>nul")


if __name__ == "__main__":
    URL().main()