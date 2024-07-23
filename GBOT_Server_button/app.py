# Ref: https://github.com/bhavaniravi/rasa-site-bot
"""
user_message -> User input
trans_response -> Stores the output of the Translation API
trans_msg -> Stores the translated message
response -> Stores the response of the Chatbot



"""
from flask import Flask
from flask import render_template,jsonify,request
import requests
# from models import *
from Tapi import translate_api
from rasapi import rasa

url = "127.0.127.0"
url_port = 8080
app = Flask(__name__)
app.secret_key = '12345'



# 
"""
API CALLER (Tapi)
trans_api_url = ???    Delete ??? to set new url
rasa_api_url = ???     Delete ??? to set new url
def translate_api(message,lang,translate_api_url = "http://127.127.127.0:9000"):
	trans_response = requests.post(translate_api_url,data={"text":message})
	trans_response = trans_response.json() 
	print("API RESPONSE : ",trans_response)
	trans_msg = trans_response["message"]
	print("API Message : ",trans_msg)
	return trans_msg


def rasa_nlu(message,rasa_nlu_url = "http://localhost:5000/parse"):
	response = requests.get(rasa_nlu_url,params={"q":message})
	print(response)
	response = response.json()
	print(response)
	return response
"""



@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/chat',methods=["POST"])
def chat():
	msg = request.form["text"]
	lang = int(request.form["lang"])
	print("USER MESSAGE : ",msg)
	print("lang = ",lang)
	#Translation API Call FUNCTION -> translate_api(message,translate_api_url)   default : "http://127.127.127.0:9000"
	if(lang == 0):
		msg = translate_api(msg,"hi-en")
	
	#print("TRANSLATED MESSAGE : ",trans_msg)

	# RASA NLU API   Call  FUNCTION -> rasa_nlu(message,rasa_nlu_url)   default : "http://localhost:5000/parse"
	response = rasa(msg)
	
	#print("ENG RESPONSE : ",response)
	if(lang == 0):
		response = translate_api(response,"en-hi")
	
	#print("TRANSLATED RESPONSE : ",trans_response)
	
	return jsonify({"status":"success","response":response})
   


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(host=url,port=url_port)
