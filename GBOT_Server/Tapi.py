# Translate API FUNCTION
import requests
import json

def translate_api(message,lang,translate_api_url = "http://127.127.127.0:9000"):
	trans_response = requests.post(translate_api_url,data={"message":message,"type":lang})
	trans_response = trans_response.json() 

	print("Translation API RESPONSE : ",trans_response)

	trans_msg = trans_response["message"]
	print("Translation API Message : ",trans_msg,"\n")

	return trans_msg