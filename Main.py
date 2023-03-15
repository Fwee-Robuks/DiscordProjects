import json
import requests

# Discord webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1085439407512891423/KQILUDIPVggOdMGVuXl5BmMj4j7Yer-nk-W3FrsXBiHuEMBgZyM_mHixIFLuj-0VHKrZ"

def send_discord_message(title, user):
    # Create the message payload
    message = {
        "username": "Plex Bot",
        "avatar_url": "https://i.imgur.com/g3ZvNSm.png",
        "embeds": [
            {
                "title": f"{user} is now watching {title}",
                "color": 6570404
            }
        ]
    }
    
    # Send the message to the Discord webhook
    response = requests.post(discord_webhook_url, json=message)
    
    # Check the response status code
    if response.status_code == 204:
        print("Discord message sent successfully")
    else:
        print(f"Error sending Discord message: {response.text}")

def handle_webhook(payload):
    # Extract the relevant data from the webhook payload
    event = payload['event']
    user = payload['Account']['title']
    
    # Check if the event is a "media.play" event for a movie
    if event['type'] == "media.play" and event['Metadata']['type'] == "movie":
        title = event['Metadata']['title']
        send_discord_message(title, user)

# Listen for incoming Plex webhooks
while True:
    try:
        # Wait for incoming webhook data
        payload = json.loads(input())
        handle_webhook(payload)
    except:
        pass
