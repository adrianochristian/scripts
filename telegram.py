import env
import requests as re

def send_message(message):
    try:
        token = env.BOT_TOKEN
        chat_id = env.CORNER_GROUP_ID
        re.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}")
    except Exception as e:
        print(f"An error occurred while trying to send the message: {e}")
        return None
    
def bot_updates():
    try:
        token = env.BOT_TOKEN
        response = re.get(f"https://api.telegram.org/bot{token}/getUpdates")
        return response.json()
    except Exception as e:
        print(f"An error occurred while trying to get the bot updates: {e}")
        return None
