# Jaspa
John's Automated Scheduling and Planning Assistant

## Overview
This application is a dedicated chat client designed to help me serenade my girlfriend, make goofy jokes, provide info about myself, and to generate date ideas for us. It is based on Chat-GPT3
and uses prompting to generate interesting responses. 

## The Frontend
The frontend is written in React in conjunction with Material UI as a UI framework. The UI consists of a login page and a chat screen. The frontend sends requests to the backend Flask app to submit chats and receive responses. It then displays the responses to the user as if it was a chat bubble similar to what is found on a phone's message app. In order to run the frontend, you'll need to configure the API endpoint base url and will need to install and run the app following standard react-app practices with NPM / create-react-app.

## The Backend 
The backend is written in Python and Flask. The API is designed to field questions from the user, and then inject prompts and info before rendering the result with ChatGPT3. 
