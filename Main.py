import requests
import json

webhook_url = 'https://discord.com/api/webhooks/1085439407512891423/KQILUDIPVggOdMGVuXl5BmMj4j7Yer-nk-W3FrsXBiHuEMBgZyM_mHixIFLuj-0VHKrZ'

# Define your message content
message = {
    "content": "Hello, world!",
    "embeds": [{
        "title": "Embed Title",
        "description": "Embed Description",
        "color": 16711680, # This sets the color of the embed to red
        "footer": {
            "text": "Embed Footer"
        },
        "fields": [{
            "name": "Field Name",
            "value": "Field Value",
            "inline": False
        }]
    }]
}

# Convert the message dictionary to JSON
payload = json.dumps(message)

# Send the message to the webhook URL
response = requests.post(webhook_url, data=payload, headers={'Content-Type': 'application/json'})

# Check if the message was sent successfully
if response.status_code == 204:
    print('Message sent successfully!')
else:
    print('Error sending message: %s' % response.text)
