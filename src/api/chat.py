import os
import openai
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
from pymongo import DESCENDING, ASCENDING
from pprint import pprint
from bson import json_util


uri = os.environ.get("MONGO_CONNECTION")

# Create a new client and connect to the server
client = None
if uri:
    client = MongoClient(uri, server_api=ServerApi('1'))
    print('Mongo Client Established!')

openai.api_key = os.getenv("OPENAI_API_KEY")

def save_message(sender, recipient, message):
    current_datetime = datetime.now()
    try:
        db = client["jaspa"]
        collection = db["chats"]

        result = collection.insert_one({'sender': sender, 'recipient': recipient, 'message': message, "timestamp": current_datetime })

        return result
    except Exception as e:
        print(e)
        return None


def summarize_conversation(sender):
    pass

def identify_intent(sender, message, configuration):

    options = "0. General discussion, 1. Plan a date, 2. Plan a meal. 3. Write a song. 4. Write a poem 5. Write a compliment"
    try:

        result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": f"{configuration['jaspa_description']}"},
                {"role": "system", "content": f"You categorize messages into the following options: {options}."},
                {"role": "system", "content": f"{configuration['john_description']}"},
                {"role": "system", "content": f"{configuration['riley_description']}"},
                {"role": "system", "content": f"You are speaking with {sender}, and they sent you the following message. \"{message}\""},
                {"role": "system", "content": f"Which category does that message most closely relate?"},
            ]
        )

        # Load in previous chat context
        # Identify purpose of chat
        # Respond in most fitting manner

        #return result
        return result['choices'][0]['message']['content']

    except Exception as e:
        print(e)
        return None
    

def fetch_configuration():
    try:

        db = client["jaspa"]
        collection = db["configuration"]

        query = {"name": "configuration"}

        result = collection.find_one(query)

        return result
    except Exception as e:
        print(e)
        return None
    
def fetch_conversation_context(user):
    # Fetch Last 10 messages
    # Provide 1 paragraph Summary of 10 before that
    try:
        db = client["jaspa"]
        collection = db["chats"]

        query = {"$or": [{"sender": user}, {"recipient": user}]}
        projection = {"_id": 0, "sender": 1, "recipient": 1, "message": 1, "timestamp": 1}

        result = collection.find(query, projection).sort("timestamp", DESCENDING).limit(10)

        return result
    except Exception as e:
        print(e)
        return None

def clear_chats():
    # Fetch Last 10 messages
    # Provide 1 paragraph Summary of 10 before that
    try:
        db = client["jaspa"]
        collection = db["chats"]

        result = collection.delete_many({})
        print('Chat cleared')
        return result
    except Exception as e:
        print(e)
        return None


def handle_message(sender="Riley", message="Hello, how are you doing today?"):

    configuration = fetch_configuration()

    conversation_context = fetch_conversation_context(user=sender)

    messages = [
            {"role": "system", "content": f"{configuration['jaspa_description']}"},
            {"role": "system", "content": f"{configuration['jaspa_background']}"},
            {"role": "system", "content": f"{configuration['john_description']}"},
            {"role": "system", "content": f"{configuration['john_background']}"},
            {"role": "system", "content": f"{configuration['riley_description']}"},
            {"role": "system", "content": f"{configuration['riley_background']}"},
        ]
    messages_to_add = []
    for chat in conversation_context:
        chat_role = "user" if chat['sender'] == sender else "assistant"
        messages_to_add.append({"role": chat_role ,"content": chat['message']})

    messages_to_add.reverse()
    messages.extend(messages_to_add)
    messages.append({"role": "system", "content": f"You are currently speaking with {sender}."},)
    messages.append({"role": "user", "content": message})

    #pprint(messages)
    
    result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    save_message(sender=sender, recipient='Jaspa', message=message)

    message_text = result['choices'][0]['message']['content']
    save_message(sender='Jaspa', recipient=sender, message=message_text)

    # Load in previous chat context
    # Identify purpose of chat
    # Respond in most fitting manner
    #return result
    if (message_text):
        return json_util.dumps({'message': message_text, 'sender': 'Jaspa', 'recipient': sender})
    else:
        return None


def notify_user():
    pass
    
def plan_date():

    # Fetch profile information
    # 
    pass

def plan_meal():
    pass

def serenade_user():

    # Load Jaspa profile and user profile

    # Generate a song about the user given any special instructions
    pass

def write_poetry():
    # Load Jaspa profile and user profile

    # Generate a song about the user given any special instructions
    pass

def adjust_configuration():
    pass


if __name__ == "__main__":
    clear_chats()
