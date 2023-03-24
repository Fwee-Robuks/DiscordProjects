from colorama import init, Fore, Back, Style
import requests
import os
import time
import json
import getpass
username = getpass.getuser()
init()
os.system("title Discord Fucker V1")

# Loading Phase

print(Fore.GREEN + "[CONSOLE]: Discord Fucker Has Loaded!")
time.sleep(.2)
print(Fore.GREEN + "[CONSOLE]: Welcome, ", username,"!")
time.sleep(.2)
print(Fore.BLUE + "[CONSOLE]: Command Prompt Loaded")
webhookforbot = input("Please insert the bots webhook url >>>")
code_exe = input(">>>")

# Exit loading phase and onto commands

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
    msgsent = input("Input Message >>>")
    webhook_url = webhookforbot
    message = msgsent
    payload = {'content': message}
    json_payload = json.dumps(payload)
    response = requests.post(webhook_url, data=json_payload, headers={'Content-Type': 'application/json'})
if response.status_code == 204:
    print('Message sent successfully')
    time.sleep(1)
else:
    print(f'Failed to send message. Response status code: {response.status_code}')
    time.sleep(1)
    
