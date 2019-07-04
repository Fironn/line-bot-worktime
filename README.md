# line-bot-worktime
send the working time from wakatime on line

# 使い方

```
git clone https://github.com/Fironn/line-bot-worktime.git
```

```
cd line-bot-worktime
cd app
```

```
pip3 install iso8601
pip3 install linebot
pip3 install requests
```

## LINE Developper設定をする
参考 :  <https://qiita.com/Takagenki/items/b2a67422e7226a16e2b1>


取得したAPIキーで `token.json` と `app.json` をつくる

token.json
```
{
    "Id":"YOUR_LINE_APP_ID",
    "Access-Secret":"YOUR_LINE_ACCESS_SECRET",
    "Access-Token":"YOUE_LINE_API_TOKEN"
}
```

app.json
```
{
    "Api-Key":"YOUR_WAKATIME_API_KEY"
}
```

```
python3 sendLine.py
```


# Credit

supported by wakatime

[<img src="app/Logo + Text Horizontal.png">](https://wakatime.com/)