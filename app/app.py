import json
import getBySummary
import getByStats

codeUrl="app.json"
f = open(codeUrl, 'r')
codeData = json.load(f)
f.close()

def getWorkTime():
        getByStats.getData(codeData['Api-Key'],'last_30_days')
        res=''
        res+='START : '
        res+=getByStats.getStartTimeByStats()
        res+='\n'
        res+='END : '
        res+=getByStats.getEndTimeByStats()
        res+='\n\n'
        data=getByStats.getTimeByStats()
        res+='TOTAL :  '
        for s in data:
                res+=s
                res+='\n'
        res+='--------------'
        res+='\n'
        data=getByStats.getProjectByStats()
        for s in data:
                res+=s
                res+='\n'
        return res