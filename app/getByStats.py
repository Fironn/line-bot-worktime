import datetime
import requests
import json
import iso8601

data={}

URL='https://wakatime.com/api/v1/users/current/stats/'
headers = {"content-type": "application/json"}

def getData(key,mode):
    global data
    if len(key)>0 :
        params = {'api_key':key}
        g=requests.get(URL+mode,headers=headers,params=params)
        data=g.json()
    else:
        print('Please set the api key.')

def getLangByStats():
    res=[]
    for s in data['data']['languages']:
        res.append(str(s['percent'])+'% \t'+s['text']+' :  '+s['name'])
    return res

def getProjectByStats():
    res=[]
    for s in data['data']['projects']:
        res.append(str(s['percent'])+'% \t'+s['text']+' :  '+s['name'])
    return res

def getTimeByStats():
    res=[]
    for s in data['data']['categories']:
        res.append(s['text'])
    return res

def getStartTimeByStats():
    return str(iso8601.parse_date(data['data']['start']))

def getEndTimeByStats():
    return str(iso8601.parse_date(data['data']['end']))