#coding:utf-8
import requests
import json
headers = {"Content-Type": "application/json"} 

def gettoken():
    data={'corpid':'your corpid','corpsecret':'your corpsecret'}
    tokenurl="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    r=requests.get(tokenurl,params=data)
    #print r.content          #str  for json
    token = json.loads(r.content)
    token = token['access_token']
    return token

def sendmsg():

    token=gettoken() 
    texturl='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % token 
    #print texturl
    text={
       "touser":"@all",
       "msgtype": "text",
       "agentid": 2,
       "text": {
           "content": "just a test"
       },
       "safe":"0"
    }

    r = requests.post(texturl, headers=headers, json=text)
    print r.status_code
    print r.content
    return r.content

print sendmsg()
