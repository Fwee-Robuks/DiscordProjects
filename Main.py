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
webhookforbot = input("Please insert the bots webhook url >>>")
code_exe = input(">>>")
if code_exe == "1":
    webhookdelete = input("Input Discord Webhook >>>")
    webhook_url = webhookdelete
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("Webhook deleted successfully.")
else:
    print("Error deleting webhook. Status code:", response.status_code)

if code_exe == "2":
    webhook_url = webhookforbot
    print(Fore.BLUE + "[CONSOLE]: Welcome to embed builder!")
    title = input("Webhook Title >>>")
    desc = input("Webhook Description >>>")

embed = {
    "title": title,
    "description": desc,
    "color": 16711680
}

# Define the payload data (including the embed)
data = {
    "username": "Embed built with Discord Fucker <3",
    "avatar_url": "https://imgur.com/7tv3Wjs",
    "embeds": [embed]
}

# Send a POST request to the webhook URL with the payload data
response = requests.post(webhook_url, json=data)

# Check the response status code
if response.status_code == 200:
    print("Message sent successfully.")
else:
    print("Error sending message. Status code:", response.status_code)

