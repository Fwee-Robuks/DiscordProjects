from colorama import init, Fore, Back, Style
import requests
import os
import time
import json
import getpass
from threading import Thread

username = getpass.getuser()
init()
os.system("title Discord Nuker")

# Functions

def send_message(webhook, message, index):
    payload = {'content': message}
    json_payload = json.dumps(payload)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook, data=json_payload, headers=headers)
    if response.status_code == 204:
        print(Fore.GREEN + f"[NUKE]: Sent Message Without Problems! Account {index}")
    else:
        print(Fore.RED + f'[RATELIMIT]: Failed to send message! Account {index}. Response status code: {response.status_code}')
    time.sleep(5) 
       

def send_messages(message, webhooks):
    threads = []
    for i, webhook in enumerate(webhooks):
        thread = Thread(target=send_message, args=(webhook, message, i+1))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# Loading Phase

print(Fore.GREEN + "[CONSOLE]: Discord Nuker Has Loaded!")
time.sleep(.2)
print(Fore.GREEN + "[CONSOLE]: Welcome, ", username,"!")
time.sleep(.2)
print(Fore.BLUE + "[CONSOLE]: Command Prompt Loaded")
webhooks = []
for i in range(4):
    webhookforbot = input(f"Please insert the bot's webhook URL {i+1}: ")
    webhooks.append(webhookforbot)
os.system("cls")
print(Fore.BLUE + "LIST OF COMMANDS")
print(Fore.GREEN + "[1]: Delete 1 Or More Webhooks.")
print(Fore.GREEN + "[2]: Send A Message Through The Webhooks.")
print(Fore.GREEN + "[3] Spam All 4 Webhooks.")
print(Fore.GREEN + "[4] Send Messages From A .txt File.")
code_exe = input("Input Command >>>")


# Exit loading phase and onto commands

if code_exe == "1":
    webhook_url = input("Please insert the webhook URL to delete or type 'all' to delete all of them: ")
    if webhook_url.lower() == 'all':
        for webhook in webhooks:
            response = requests.delete(webhook)
            if response.status_code == 204:
                print("Webhook deleted successfully.")
            else:
                print("Error deleting webhook. Status code:", response.status_code)
    else:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print("Webhook deleted successfully.")
        else:
            print("Error deleting webhook. Status code:", response.status_code)

elif code_exe == "2":
    message = input("Input Message >>>")
    send_messages(message, webhooks)

elif code_exe == "3":
    num_messages = int(input("Input Number of Messages >>>"))
    message = input("Input Message >>>")
    for i in range(num_messages):
        send_messages(message, webhooks)

else:
    print("Invalid option. Please choose 1, 2, 3 or 4")