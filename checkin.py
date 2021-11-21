import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]

# 填入glados账号对应cookie
#cookie1 = os.environ["COOKIE1"] # @qq.com
cookie2 = os.environ["COOKIE2"] # @nuist.edu.cn


def start():    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    #state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados_network'
    }
    #checkin1 = requests.post(url,headers={'cookie': cookie1 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    #state1 =  requests.get(url2,headers={'cookie': cookie1 ,'referer': referer,'origin':origin,'user-agent':useragent})
    
    checkin2 = requests.post(url,headers={'cookie': cookie2 ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state2 =  requests.get(url2,headers={'cookie': cookie2 ,'referer': referer,'origin':origin,'user-agent':useragent})    
    

    #if 'message' in checkin1.text:
    #    mess = checkin1.json()['message']
    #    time = state1.json()['data']['leftDays']
    #    time = time.split('.')[0]
    #    print(time)
    #    if sever == 'on':
    #        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left @qq.com')
    #else:
    #    requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text=QQ邮箱的cookie过期！请更新COOKIE1')
        
    if 'message' in checkin2.text:
        mess = checkin2.json()['message']
        time = state2.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left @nuist.edu.cn')
    else:
        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?text=nuist邮箱的cookie过期！请更新COOKIE2')


def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
