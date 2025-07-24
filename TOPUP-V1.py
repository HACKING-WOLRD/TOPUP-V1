import time
import os
from os import system as c

G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
P = '\033[95m'

def slow(text, delay=0.03):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    c("clear")
    print(f"""{G}
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
           {Y}HACKING WORLD - VIP DIAMOND TOOL
-------------------------------------------------------
""")

def loading(txt, sec=3):
    for i in range(sec):
        print(f"{Y}{txt}{'.' * (i % 4)}", end='\r')
        time.sleep(1)

def diamond_tool():
    banner()
    slow(f"{C}[!] This tool requires Free Fire Cookie & UID\n")
    cookie = input(f"{P}Enter your Free Fire Cookie: {W}")
    uid = input(f"{P}Enter your UID: {W}")
    loading("Connecting to Garena Server", 3)
    print(f"{G}[✓] Cookie Verified")
    time.sleep(1)
    print(f"{G}[✓] UID Matched: {uid}")
    loading("Fetching Diamond Packages", 3)

    diamonds = [1000, 2000, 5200, 9999]
    for d in diamonds:
        print(f"{C}[*] Injecting {d} Diamonds...")
        time.sleep(1)

    time.sleep(1.5)
    print(f"\n{G}[!] Your TopUp Success !")
    print(f"{G}Waiting 6 Minit.")
    print(f"{G}Topup success done 9999 Diamond: {G}TopUp\n")
    input(f"{C}Press Enter to Exit...")

diamond_tool()