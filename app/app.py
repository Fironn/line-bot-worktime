#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
print('Content-type: text/html; charset=UTF-8\n')

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import json
import getJson

codeUrl="token.json"
f = open(codeUrl, 'r')

codeData = json.load(f)
f.close()

LINE_CHANNEL_ACCESS_TOKEN = codeData["Access-Token"]
LINE_CHANNEL_SECRET=codeData["Access-Secret"]
user_id=codeData["User-Id"]
api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def main():
    time=getJson.getWorkTime()
    api.push_message(user_id, messages=time)

if __name__ == "__main__":
    main()