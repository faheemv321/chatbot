from flask import Flask
from flask import render_template,jsonify,request



from final import translate
from final import translate_rev


url = "127.127.127.0"
url_port = 9000

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/",methods=["POST"])
def translate_string():
  user_message = request.form["message"]
  lang_type = request.form["type"]

  
  print("USER MESSAGE:- ",user_message)

  if(lang_type == "hi-en"):
    print("TO_TYPE : ",lang_type)
    result = translate(user_message)
  elif(lang_type == "en-hi"):
    print("TO_TYPE : ",lang_type)
    result = translate_rev(user_message)  

  print("RETURNED MESSAGE:- ",result)

  return jsonify({"message":result})


if __name__ == "__main__":
  app.run(host=url,port=url_port)
