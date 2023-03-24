from colorama import init, Fore, Back, Style
import requests
import os
import time
import getpass
username = getpass.getuser()
init()

print(Fore.GREEN + "[CONSOLE]: Discord Fucker Has Loaded!")
time.sleep(.2)
print(Fore.GREEN + "[CONSOLE]: Welcome, ", username,"!")
time.sleep(.2)
print(Fore.BLUE + "[CONSOLE]: Command Prompt Loaded")
code_exe = input(">>>")
if code_exe == "deletewebhook":
    webhookdelete = input("Input Discord Webhook >>>")
    webhook_url = webhookdelete
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("Webhook deleted successfully.")
else:
    print("Error deleting webhook. Status code:", response.status_code)
    

