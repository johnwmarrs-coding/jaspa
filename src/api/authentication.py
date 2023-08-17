
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import hashlib
from datetime import datetime, timedelta
import os
from bson import json_util

uri = os.environ.get("MONGO_CONNECTION")
print(uri)
print("MONGO_CONNECTION" in os.environ.keys())

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def validate_token(token_hash):

    db = client["jaspa"]
    collection = db["tokens"]

    query = {"token": token_hash}

    result = collection.find_one(query)

    if not result:
        print("Invalid Token")
        return None
    else:
        print(result)
        return result




def clear_expired_tokens():


    db = client["jaspa"]
    collection = db["tokens"]

    # Define the current datetime
    current_datetime = datetime.now()

    # Delete documents where the "expiry" field is less than the current datetime
    query = {"expiry": {"$lt": current_datetime}}
    delete_result = collection.delete_many(query)
    print(delete_result.deleted_count, "documents deleted")
    


def generate_token(user, salt):

    db = client["jaspa"]
    collection = db["tokens"]

    token_hash = hashlib.sha256(f"RileyCute{datetime.now().time()}".encode()).hexdigest()

    result = collection.insert_one({"token": token_hash, "user": user, "expiry": datetime.now() + timedelta(hours=1)})
    token_object = collection.find_one({"_id": result.inserted_id})

    return json_util.dumps(token_object)

def authenticate(data):

    # Send a ping to confirm a successful connection
    try:

        db = client["jaspa"]
        collection = db["configuration"]

        query = {"name": "configuration"}

        #result = collection.update_one(query, {"$set": {"emoji_secret": "😵‍💫🌪🍣🐟"}})
        result = collection.find_one(query)

        emoji_passed = data['emoji_password'] == result['emoji_secret']

        date_passed = data['first_date_password'] == result['date_secret']

        john_passed = data['user_password'].lower() == str(result['john_password']).lower()
        riley_passed = data['user_password'].lower() == str(result['riley_password']).lower()



        #print(result['emoji_secret'] ==  '😵‍💫🌪🍣🐟')
        token = None
        if (emoji_passed and date_passed and (john_passed or riley_passed)):
            if (john_passed):
                print('Welcome John!')
                token=generate_token('John', result['salt'])
            elif (riley_passed):
                print('Welcome, Riley')
                token=generate_token('Riley', result['salt'])

        else:
            print("Access Denied!")
            token=None


        clear_expired_tokens()

        return token

    except Exception as e:
        print(e)

#authenticate({"emoji_password": '😵‍💫🌪🍣🐟', "first_date_password": "06/03/2023", "user_password": "Canada Goose"})

