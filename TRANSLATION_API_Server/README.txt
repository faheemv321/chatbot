 
You can install the modules specified in the translation_env.yml file manually using pip

OR

If using conda set up the environment using :-   conda create -f translation_env.yml

To start the Flask Server:- python trans_api_server.py


This API accepts as POST request 
The fields for this api as json are:-
{"type":"lang","message":"Message to chatbot"}

where "type" field in this project can be :- "en-hi" OR "hi-en"


Refer the Translation section in the docs for more information
