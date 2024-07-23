import requests

rasa_url = 'http://localhost:5005/webhooks/rest/webhook'

def rasa(message):
	response =  requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": "default", "message": message})
	response = response.json()
	print("RASA RESPONSE :-",response,"\n")
	return response[0]['text']
