# Made by Epsilon#4200 on discord and tweaked by ChatGPT

from colorama import init, Fore, Back, Style
import requests
import os
import time
import json
import getpass

username = getpass.getuser()
init()
os.system("title Discord Fucker V1 (Yay more functions)")

# Loading Phase

print(Fore.GREEN + "[CONSOLE]: Discord Fucker Has Loaded!")
time.sleep(.2)
print(Fore.GREEN + "[CONSOLE]: Welcome, ", username,"!")
time.sleep(.2)
print(Fore.BLUE + "[CONSOLE]: Command Prompt Loaded")
webhookforbot = input("Please insert the bot's webhook URL >>>")
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
elif code_exe == "2":
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
elif code_exe == "3":
    webhook_url = webhookforbot
    for i in range(5):
        message = f'This is message {i+1}'
        payload = {'content': message}
        json_payload = json.dumps(payload)
        response = requests.post(webhook_url, data=json_payload, headers={'Content-Type': 'application/json'})
        if response.status_code == 204:
            print(f'Message {i+1} sent successfully')
            time.sleep(1)
        else:
            print(f'Failed to send message {i+1}. Response status code: {response.status_code}')
            time.sleep(1)
else:
    print("Invalid option. Please choose 1, 2 or 3")
    time.sleep(2)
