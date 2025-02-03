import requests
import traceback
import time    
import urllib
from time import *
print(2)
TOKEN = "657599339:AAFJutWFo0RuR0DSvx8p3419YDhAqN--cds"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
from flask import Flask,redirect, url_for,request,render_template
from threading import Thread
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'v.json'
app = Flask(__name__)
from flask import Flask, request, jsonify, render_template
import dialogflow
import requests
import json
import pusher

from datetime import *

# initialize Pusher
pusher_client = pusher.Pusher(
    app_id='710715',
    key='b9b672ef1546f479aa6d',
    secret='20b955a98b9e19bf9190',
    cluster='ap2',
    ssl=True)


@app.route('/')
def index():
    return render_template('index.html')


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    
    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        
        return response.query_result.fulfillment_text

def msg(m):
    project_id = 'varshaa-c5649'
    if m.lower().startswith('r.'):
        a=m[2:]
        a=a.split('@')
        rn=a[0]
        s=a[1] if a[1:] else None
        a=cg(s,rn)
        print(a)
        return(a)
    return detect_intent_texts(project_id, "unique", m, 'en')


@app.route('/send_message', methods=['POST'])
def send_message():
    # socketId = request.form['socketId']
    message = request.form['message']
    
    response_text = { "message":  msg(message) }
    print(message,response_text)

                     
    return jsonify(response_text)

# run Flask app
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    return  requests.get(url).json()

def snt(f,a,b=None):
  try:
    Thread(None,f,None,a,b).start()
  except Exception as e:
    print(e);traceback.print_exc()
    return str(e)


domain='sanjuvarshaa'
def restart():
 while True:
  try:
   v=(datetime.utcnow()+timedelta(hours=5,minutes=30))
   if(1 or 5*60<v.hour*60+v.minute<21*60+30):
    requests.head(f"http://{domain}.herokuapp.com",timeout=5)
   sleep(25*60)
  except Exception as e:
   sleep(60)
   print(e);traceback.print_exc()
   continue

snt(restart,())
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url=URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    try:
        r=requests.get(url,timeout=30)
        if r.reason!='OK':print(r.text)
    except Exception as e:
        print(e);traceback.print_exc()
        print(url)

def main():
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)           
            z=updates.get("result")
            if z and len(z) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)
            sleep(0.5)
        except Exception as e:
            print(e);traceback.print_exc()        

from zcg import cg
def echo_all(updates):
    for update in updates["result"]:
        try:
            print(update)
            name=update["message"]["chat"]["first_name"]
            chat = update["message"]["chat"]["id"]
            a = update["message"].get("text")

            #customize here 
            if a=='/start':
                # send_message('N:'+name,537015197)
                a='Welcome '+name
            else:
                
                a=msg(a)
            # 
            send_message(a,chat)
        except Exception as e:
            print(e);traceback.print_exc()
snt(main,())
if __name__ == '__main__':
    app.run(debug=1)
    # send_message(cg('1','15isr055'),37015197)
    # print(cg('1','16isr036'),37015197)