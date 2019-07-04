import datetime
import requests
import json

today= datetime.date.today()
dayDel=datetime.timedelta(days=14)
startDay=today-dayDel
endDay=today
data={}

URL='https://wakatime.com/api/v1/users/current/summaries'
headers = {"content-type": "application/json"}

def getData(key,day):
    global data,dayDel,startDay
    if len(day)>0:
        dayDel=datetime.timedelta(days=day)
        startDay=today-dayDel
    if len(key)>0 :
        params = {'api_key':key,'end':endDay,'start':startDay}
        g=requests.get(URL,headers=headers,params=params)
        data=g.json()
    else:
        print('Please set the api key.')

def getLangBySummary():
    res=[]
    i=0
    for s in data['data']:
        nextDay=datetime.timedelta(days=i)
        for l in s['categories']:
            res.append(str(startDay+nextDay)+' '+l['digital'])
        for l in s['languages']:
            res.append(l['name']+' '+str(l['percent']))
        i+=1
    return res
        
def getProjectBySummary():
    res=[]
    i=0
    for s in data['data']:
        nextDay=datetime.timedelta(days=i)
        for l in s['categories']:
            res.append(str(startDay+nextDay)+' '+l['digital'])
        for l in s['projects']:
            res.append(l['name']+' '+l['digital'])
        i+=1
    return res

def setStartDate(date):
    global startDate
    startDate=date

def setEndDate(date):
    global endDate
    endDate=date