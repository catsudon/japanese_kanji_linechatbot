import requests
from flask import Flask, request, abort
import json
from bs4 import BeautifulSoup
from Project.flex import *
from Project.Config import *
import random

app = Flask(__name__)


@app.route('/kanji', methods = ['POST','GET'])
def kanji():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        if "andom" in message:
            url = "https://kanjiapi.dev/v1/kanji/grade-{}".format(random.randint(1,6))
            r = requests.get(url)
            data_json = json.loads(r.text)
            kanji = data_json[random.randint(0,len(data_json)-1)]
            #REQUEST FOR KANJI DETAIL
            url = "https://kanjiapi.dev/v1/kanji/{}".format(kanji)
            r = requests.get(url)
            data_json = json.loads(r.text)
            meanings = []
            jlpt = data_json["jlpt"]
            for i in range(3):
                try:
                    meanings.append(data_json['meanings'][i])
                except Exception:
                    pass
            kun_readings = []
            for i in range(3):
                try:
                    kun_readings.append(data_json['kun_readings'][i])
                except Exception:
                    pass
            on_readings = []
            for i in range(3):
                try:
                    on_readings.append(data_json['on_readings'][i])
                except Exception:
                    pass

            reply_kanji(Reply_token,kanji,meanings,jlpt,kun_readings,on_readings)    
        try:
            level = int(message[-1])
            passornot = True
        except Exception:
            passornot = False

        if passornot == True:

            if int(message[-1]) <= 6 :
                url = "https://kanjiapi.dev/v1/kanji/grade-{}".format(message[-1])
                r = requests.get(url)
                data_json = json.loads(r.text)
                kanji = data_json[random.randint(0,len(data_json)-1)]
                #REQUEST FOR KANJI DETAIL
                url = "https://kanjiapi.dev/v1/kanji/{}".format(kanji)
                r = requests.get(url)
                data_json = json.loads(r.text) 
                print(data_json)
                meanings = []
                jlpt = data_json["jlpt"]
                for i in range(3):
                    try:
                        meanings.append(data_json['meanings'][i])
                        print(data_json['meanings'][i])
                    except Exception:
                        pass
                kun_readings = []
                for i in range(3):
                    try:
                        kun_readings.append(data_json['kun_readings'][i])
                    except Exception:
                        pass
                on_readings = []
                for i in range(3):
                    try:
                        on_readings.append(data_json['on_readings'][i])
                    except Exception:
                        pass
                reply_kanji(Reply_token,kanji,meanings,jlpt,kun_readings,on_readings)    
            else:
                pass   

        else:
            url = "https://kanjiapi.dev/v1/kanji/{}".format(message)
            try:
                r = requests.get(url)
                kanji = message
                data_json = json.loads(r.text) 
                print(data_json)
                meanings = []
                jlpt = data_json["jlpt"]
                for i in range(3):
                    try:
                        meanings.append(data_json['meanings'][i])
                        print(data_json['meanings'][i])
                    except Exception:
                        pass
                kun_readings = []
                for i in range(3):
                    try:
                        kun_readings.append(data_json['kun_readings'][i])
                    except Exception:
                        pass
                on_readings = []
                for i in range(3):
                    try:
                        on_readings.append(data_json['on_readings'][i])
                    except Exception:
                        pass
                reply_kanji(Reply_token,kanji,meanings,jlpt,kun_readings,on_readings)    



            except Exception:
                error_message_send(Reply_token)

        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)




def reply_kanji(Reply_token,kanji,meanings,jlpt,kun_reading,on_reading):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Channel_access_token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[
        flex(kanji,meanings,jlpt,kun_reading,on_reading)
  ]
}
    
                    

    data = json.dumps(data) ## dump dict >> Json Object
    requests.post(LINE_API, headers=headers, data=data) 
    return 200

def error_message_send(Reply_token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Channel_access_token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[
          {"type":"text",
          "text":"Error"}
  ]
}
    
                    

    data = json.dumps(data) ## dump dict >> Json Object
    requests.post(LINE_API, headers=headers, data=data) 
    return 200
