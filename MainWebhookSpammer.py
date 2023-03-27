from colorama import init, Fore, Back, Style
import requests
import os
import time
import json
import getpass
from threading import Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

username = getpass.getuser()
init()
os.system("title Discord Nuker")

# Functions

def send_message_from_queue(queue, webhook):
    while True:
        message = queue.get()
        if message is None:
            break
        send_message(webhook, message)
        queue.task_done()

def spam_webhooks(message, webhooks, num_messages):
    queue = Queue()
    for _ in range(num_messages):
        queue.put(message)
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        for webhook in webhooks:
            executor.submit(send_message_from_queue, queue, webhook)
    
    queue.join()
    for _ in range(len(webhooks)):
        queue.put(None)
    queue.join()

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
    spam_webhooks(message, webhooks, num_messages)

else:
    print("Invalid option. Please choose 1, 2 or 3")
