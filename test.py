import requests
import json
import random


# url = "https://kanjiapi.dev/v1/kanji/grade-{}".format(random.randint(1,6))
# r = requests.get(url)
# data_json = json.loads(r.text)
# print(len(data_json))
# print(data_json[1])
# print(r.text)

# url = "https://kanjiapi.dev/v1/kanji/{}".format("身")
# r = requests.get(url)
# data = json.loads(r.text)
# print(data)

# url = "https://kanjiapi.dev/v1/kanji/grade-{}".format(random.randint(1,6))
# r = requests.get(url)
# data_json = json.loads(r.text)
# kanji = data_json[random.randint(0,len(data_json)-1)]
# #REQUEST FOR KANJI DETAIL
# url = "https://kanjiapi.dev/v1/kanji/{}".format(kanji)
# r = requests.get(url)
# data_json = json.loads(r.text) 
# print(data_json)
url = "https://kanjiapi.dev/v1/kanji/{}".format("有")
r = requests.get(url)
data = json.loads(r.text)
print(data)
print(data['meanings'])