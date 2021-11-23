import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]

# 填入glados账号对应cookie
cookie1 = os.environ["COOKIE1"] # 2226840339@qq.com
cookie2 = os.environ["COOKIE2"] # 20171376006@nuist.edu.cn
cookie3 = os.environ["COOKIE3"] # 2315230220@qq.com
cookie4 = os.environ["COOKIE4"] # 1713863719@qq.com
cookie5 = os.environ["COOKIE5"] # 3494620766@qq.com



def start():    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    #state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"
    payload={
        'token': 'glados_network'
    }
    checkin1 = requests.post(url,headers={'cookie': cookie1 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state1 =  requests.get(url2,headers={'cookie': cookie1 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    checkin2 = requests.post(url,headers={'cookie': cookie2 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state2 =  requests.get(url2,headers={'cookie': cookie2 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    checkin3 = requests.post(url,headers={'cookie': cookie3 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state3 =  requests.get(url2,headers={'cookie': cookie3 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    checkin4 = requests.post(url,headers={'cookie': cookie4 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state4 =  requests.get(url2,headers={'cookie': cookie4 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    checkin5 = requests.post(url,headers={'cookie': cookie5 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state5 =  requests.get(url2,headers={'cookie': cookie5 ,'referer': referer,'origin':origin,'user-agent':useragent})
    

    if 'message' in checkin1.text:
        mess = checkin1.json()['message']
        time = state1.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text='+mess+'，222账号剩余'+time+'天')
    else:
        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text=222的cookie过期！请更新COOKIE1')
    #--------------------------------------------------------------------------------------------------------#  
    if 'message' in checkin2.text:
        mess = checkin2.json()['message']
        time = state2.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text='+mess+'，nuist账号剩余'+time+'天')
    else:
        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text=nuist邮箱的cookie过期！请更新COOKIE2')
     #--------------------------------------------------------------------------------------------------------#   
     if 'message' in checkin3.text:
        mess = checkin3.json()['message']
        time = state3.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text='+mess+'，231账号剩余'+time+'天')
    else:
        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text=231邮箱的cookie过期！请更新COOKIE3')
     #--------------------------------------------------------------------------------------------------------#   
     if 'message' in checkin4.text:
        mess = checkin4.json()['message']
        time = state4.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text='+mess+'，171账号剩余'+time+'天')
    else:
        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text=171邮箱的cookie过期！请更新COOKIE4')
     #--------------------------------------------------------------------------------------------------------#  
     if 'message' in checkin5.text:
        mess = checkin5.json()['message']
        time = state5.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text='+mess+'，349账号剩余'+time+'天')
    else:
        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text=349邮箱的cookie过期！请更新COOKIE5')


def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
