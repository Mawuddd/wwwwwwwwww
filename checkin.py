import requests,json,os

# 推送开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写pushplus的sckey,不开启推送则不用填
sckey = os.environ["SCKEY"]

# 填入glados账号对应cookie
cookie1 = os.environ["COOKIE1"] # 20211201028@nuist.edu.cn
cookie2 = os.environ["COOKIE2"] # 2021nuister@gmail.com
cookie3 = os.environ["COOKIE3"] # 2226840339@qq.com




def start():    
    url= "https://glados.one/api/user/checkin"
    url2= "https://glados.one/api/user/status"
    referer = 'https://glados.one/console/checkin'
    origin = "https://glados.one"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    payload={
        'token': 'glados.network'
    }
    checkin1 = requests.post(url,headers={'cookie': cookie1 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state1 =  requests.get(url2,headers={'cookie': cookie1 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    checkin2 = requests.post(url,headers={'cookie': cookie2 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state2 =  requests.get(url2,headers={'cookie': cookie2 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    checkin3 = requests.post(url,headers={'cookie': cookie3 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state3 =  requests.get(url2,headers={'cookie': cookie3 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    

    time1 = state1.json()['data']['leftDays']
    time1 = time1.split('.')[0]
    email1 = state1.json()['data']['email']
    if 'message' in checkin1.text:
        mess = checkin1.json()['message']
        if sever == 'on':
            requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title='+mess+'&content='+email1+' 剩余'+time1+'天')
    else:
        requests.get('http://www.pushplus.plus/send?token=' + sckey + '&content='+email1+'更新cookie')
    #--------------------------------------------------------------------------------------------------------# 
    time2 = state2.json()['data']['leftDays']
    time2 = time2.split('.')[0]
    email2 = state2.json()['data']['email']
    if 'message' in checkin2.text:
        mess = checkin2.json()['message']
        if sever == 'on':
            requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title='+mess+'&content='+email2+' 剩余'+time2+'天')
    else:
        requests.get('http://www.pushplus.plus/send?token=' + sckey + '&content='+email2+'更新cookie')
     #--------------------------------------------------------------------------------------------------------#   
    time3 = state3.json()['data']['leftDays']
    time3 = time3.split('.')[0]
    email3 = state3.json()['data']['email']
    if 'message' in checkin3.text:
        mess = checkin3.json()['message']
        if sever == 'on':
            requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title='+mess+'&content='+email3+' 剩余'+time3+'天')
    else:
        requests.get('http://www.pushplus.plus/send?token=' + sckey + '&content='+email3+'更新cookie')
     #--------------------------------------------------------------------------------------------------------#   


def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
