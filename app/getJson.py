import requests
import json
URL='https://wakatime.com/share/@2fce9297-5ba7-422a-aa89-cbaacd4b2508/78e3bc08-4b8a-4833-ba6f-53daeafd4a7f.json'
headers = {"content-type": "application/json"}
g=requests.get(URL,headers=headers)
data=g.json()

def getWorkTime():
    compress=[]
    for l in data['data']:
        compress.append(l['range']['date']+' '+l['grand_total']['digital'])
    return compress