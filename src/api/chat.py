import os
import openai
from pprint import pprint

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_conversation(sender):
    pass


def handle_message(sender="Riley", message="Hello, how are you doing today?"):

    result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant named JASPA which stands for John's Automated Scheduling and Planning Assistant."},
            {"role": "system", "content": "You are John's assistant. John is very much in love with a girl named Riley who is adventurous, smart, and beautiful."},
            {"role": "system", "content": "John is from Milwaukee. John loves outdoor and indoor activities, but mainly likes to stay active. "},
            {"role": "system", "content": "Riley enjoys crafts, restaurants, nature, staying active, cycling, hiking, and games. She likes to stay mentally stimulated"},
            {"role": "system", "content": f"You are currently speaking with {sender}."},
            {"role": "system", "content": "You are able to help create date ideals, meal ideas, poetry, and songs to sing. You do this to help John and Riley stay in love. "},
            {"role": "user", "content": message},
        ]
    )

    # Load in previous chat context
    # Identify purpose of chat
    # Respond in most fitting manner

    print('Handling Message')
    #return result
    return result['choices'][0]['message']['content']


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

print(handle_message(sender="Riley", message="Can you serenade me as if you were in a Mariachi band? Please include emojis in your response."))


