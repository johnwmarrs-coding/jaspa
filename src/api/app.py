from flask import Flask, request
from authentication import validate_token, authenticate
from chat import handle_message
from flask_cors import CORS
app = Flask(__name__)
import os
CORS(app)


mock = os.environ.get("MOCK")

def mock_authenticate(success=True):
    if (success):
        return
    else:
        pass


@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    # Extract JSON data from request
    data = request.get_json()

    # Compare Auth Data to DB
    # Return error or with authentication token and display name
    authentication_token = authenticate(data)

    if authentication_token:
        return authentication_token
    else:
        return '', 401

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    authorization_header = request.headers.get('Authorization')
    if authorization_header:
        token_hash = authorization_header.split(' ')[1]
        print(authorization_header)
        
        token = validate_token(token_hash)
        if token:
            return handle_message(sender=token['user'], message=data['message'])
        else:
            return '', 401


# TODO: SERVE REACT