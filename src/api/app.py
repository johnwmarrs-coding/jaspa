from flask import Flask, request, send_from_directory
from authentication import validate_token, authenticate
from chat import handle_message
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='build', static_url_path='/')
CORS(app)


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    

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
    
        
        token = validate_token(token_hash)
        if token:
            return handle_message(sender=token['user'], message=data['message'])
        else:
            return '', 401
    

if __name__ == "__main__":
    from waitress import serve
    port = os.environ.get("PORT")
    serve(app, host="0.0.0.0", port=port)

