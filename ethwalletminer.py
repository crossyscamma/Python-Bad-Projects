import random, time, string, colorama, os, sys, socket, re, json, urllib.request
from colorama import Fore
from getpass import getpass
colorama.init()

def reg():
    os.system("cls")
    username = input("> Username: ")
    password = getpass(prompt="> Password: ")
    if(username == "Admin" and password == "password"):
        print(f"{Fore.GREEN}> Login successful !")
        print(f"{Fore.WHITE}")
        main()
    else:
        print(f"{Fore.RED}> Username or password is incorrect !{Fore.WHITE}")
        print("")
        input("> Press ENTER to try again...")
        os.system("cls")
        reg()

def main():
    print(f"{Fore.BLUE}$$$$$$$$\ $$$$$$$$\ $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  ")
    time.sleep(0.2)
    print("$$  _____|\__$$  __|$$ |  $$ |      $$$\    $$$ |\_$$  _|$$$\  $$ |$$  _____|$$  __$$\ ")
    time.sleep(0.2)
    print("$$ |         $$ |   $$ |  $$ |      $$$$\  $$$$ |  $$ |  $$$$\ $$ |$$ |      $$ |  $$ |")
    time.sleep(0.2)
    print("$$$$$\       $$ |   $$$$$$$$ |      $$\$$\$$ $$ |  $$ |  $$ $$\$$ |$$$$$\    $$$$$$$  |")
    time.sleep(0.2)
    print("$$  __|      $$ |   $$  __$$ |      $$ \$$$  $$ |  $$ |  $$ \$$$$ |$$  __|   $$  __$$< ")
    time.sleep(0.2)
    print("$$ |         $$ |   $$ |  $$ |      $$ |\$  /$$ |  $$ |  $$ |\$$$ |$$ |      $$ |  $$ |")
    time.sleep(0.2)
    print("$$$$$$$$\    $$ |   $$ |  $$ |      $$ | \_/ $$ |$$$$$$\ $$ | \$$ |$$$$$$$$\ $$ |  $$ |")
    time.sleep(0.2)
    print("\________|   \__|   \__|  \__|      \__|     \__|\______|\__|  \__|\________|\__|  \__|")
    time.sleep(0.2)
    print(f"{Fore.WHITE} \n")
    adress = input("> Enter your ETH address: ")
    print(f"{Fore.GREEN}> ETH address is connected !")
    time.sleep(1)
    loading()
    print("")
    print(f"{Fore.WHITE}Starting...")
    print("")
    time.sleep(2)
    characters = string.ascii_lowercase + string.digits
    pokus = 0
    for x in range(random.randrange(120000)):
        print(f"{Fore.RED}> %s | 0.00000 ETH |" % "".join(random.sample(characters, 32)))
    time.sleep(0.5)
    print(f"{Fore.GREEN}> %s | 0.24085 ETH |" % "".join(random.sample(characters, 32)))
    time.sleep(0.5)
    print(f"{Fore.WHITE}> Attempting to transfer to your wallet")
    time.sleep(2)
    print(f"{Fore.GREEN}> Transfer successful !")
    time.sleep(0.2)
    print("> You earned 0.24085 ETH !")
    input("")

def loading():
    res = 1
    print("")
    while res < 10:
        sys.stdout.write(f"{Fore.WHITE}\rLoading |")
        time.sleep(0.1)
        sys.stdout.write("\rLoading /")
        time.sleep(0.1)
        sys.stdout.write("\rLoading -")
        time.sleep(0.1)
        sys.stdout.write("\rLoading \\")
        time.sleep(0.1)
        res += 1
    print(f"{Fore.GREEN}\rLoading Done !")
reg()