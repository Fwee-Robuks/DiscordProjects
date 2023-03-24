from colorama import init, Fore, Back, Style
import requests
import os
import time
import json
import getpass
username = getpass.getuser()
init()
os.system("title Discord Fucker V1")

print(Fore.GREEN + "[CONSOLE]: Discord Fucker Has Loaded!")
time.sleep(.2)
print(Fore.GREEN + "[CONSOLE]: Welcome, ", username,"!")
time.sleep(.2)
print(Fore.BLUE + "[CONSOLE]: Command Prompt Loaded")
webhookforbot = input("Please insert the bots webhook url >>>")
code_exe = input(">>>")
if code_exe == "1":
    webhook_url = webhookforbot
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("Webhook deleted successfully.")
        time.sleep(2)
else:
    print("Error deleting webhook. Status code:", response.status_code)
    time.sleep(2)

if code_exe == "2":
    name = input("New Discord Webhook Name >>>")
    new_name = name
    payload = {'name': new_name}
    json_payload = json.dumps(payload)
    response = requests.patch(webhook_url, data=json_payload, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print(f'Webhook name updated to "{new_name}"')
        time.sleep(2)
else:
    print(f'Failed to update webhook name. Response status code: {response.status_code}')
    time.sleep(2)

    
