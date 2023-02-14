import os
import requests
import time

def send_message(webhook_url, message, avatar_url, username):
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "username": username,
        "avatar_url": avatar_url,
        "content": message
    }
    requests.post(webhook_url, headers=headers, json=data)

def delete_webhook(webhook_url, avatar_url, username):
    send_message(webhook_url, "Uh No! You Got Fucked", avatar_url, username)
    os.system(f"curl -X DELETE {webhook_url}")
    print("\n🗑️ Discord Webhook Deleted!")

webhook_url = input("Enter Discord Webhook URL: ")
avatar_url = "https://production.listennotes.com/podcasts/teras-podcast/eps-4-mr-loba-loba-eapfh4LY7As-abDjECBcNyq.1400x1400.jpg"
username = "PeeHooks"

if not webhook_url.startswith("https://discord.com/api/webhooks/"):
    print("\n❌ Invalid Discord Webhook URL")
else:
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            print("\n✨ Options:")
            print(" 1. Send Message to Webhook")
            print(" 2. Delete Webhook")
            print(" 3. Spam Webhook")
            option = input("\nChoose an option (1/2/3): ")
            if option == "1":
                message = input("Enter message to send: ")
                send_message(webhook_url, message, avatar_url, username)
                print("\n✅ Message sent successfully!")
            elif option == "2":
                delete_webhook(webhook_url, avatar_url, username)
            elif option == "3":
                message = input("Enter message to send: ")
                message_q = input("Enter amount of messages to send: ")
                for i in range(int(message_q)):
                    send_message(webhook_url, message, avatar_url, username)
                    time.sleep(0.01)
                print("\n✅ Message sent successfully!")
            else:
                print("\n❌ Wrong Input")
        else:
            print("\n❌ Invalid Discord Webhook URL")
    except requests.exceptions.RequestException as e:
        print("\n❌ An error occurred while trying to connect to the URL")
