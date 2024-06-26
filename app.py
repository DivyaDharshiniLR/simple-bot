from flask import Flask
from flask import request
from flask import Response
import requests
 
TOKEN = "6657751973:AAFsqGHxrqN3UIPg8AZVDcoWEghQwaVbEjs"
app = Flask(__name__)
 
def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)
        if txt == "hi":
            tel_send_message(chat_id,"helloo its doreamon")
        elif txt == "how are you":
            tel_send_message(chat_id,"fine and wht bt u")
            
        else:
         tel_send_message(chat_id," sounds good")
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__== '__main__':
   app.run(debug=True)