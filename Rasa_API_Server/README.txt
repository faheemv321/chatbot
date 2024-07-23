To set up the Rasa environment:-  

pip install rasa

For Rasa X :- pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

Start the Rasa Local Server:- rasa run -m models --enable-api --cors “*” --debug (Debug Mode) 

This API accepts as POST request 
The fields for this api as json are:-
{"sender":"any_name","message":"Message to chatbot"}

The url for this api is :- http://localhost:5005/webhooks/rest/webhook
