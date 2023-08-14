from flask import Flask, request, jsonify
from authentication import validate_token, authenticate
app = Flask(__name__)
def hello_world():
    return "<p>Hello, World!"

@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    # Extract JSON data from request
    data = request.get_json()
    #print(data)

    # Compare Auth Data to DB
    # Return error or with authentication token and display name
    authentication_token = authenticate(data)

    if authentication_token:
        return authentication_token
    else:
        return '', 401
    #authenticate({"emoji_password": '😵‍💫🌪🍣🐟', "first_date_password": "06/03/2023", "user_password": "Canada Goose"})

    return jsonify(data)

@app.route('/chat', methods=['POST'])
def chat():
    authorization_header = request.headers.get('Authorization')
    if authorization_header:
        token = authorization_header.split(' ')[1]
        print(authorization_header)
        print(token)
        
        if validate_token(token): 
            return 'Look at us chatting!'
        else:
            return '', 401

    # Extract JSON data from request
    data = request.get_json()

    # Validate user and fetch identify

    # Process Chat

    # Return response


    # Compare Auth Data to DB

    return jsonify(data)



@app.route('/sms', methods=['POST'])
def chat_sms():
    # Extract JSON data from request
    data = request.get_json()

    # Validate user and fetch identify

    # Process Chat

    # Return response


    # Compare Auth Data to DB

    return jsonify(data)


# TODO: SMS HANDLER

# TODO: SERVE REACT