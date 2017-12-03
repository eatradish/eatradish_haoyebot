#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,sys,time,requests,os

api_addr="https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/channel/data/asyncqury"
ua='User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

header={
    'Cookie':'BAIDUID=',
    'User-Agent':ua
}
def mstimestamp():
    return int(round(time.time() * 1000))

def tracking(number,retry=0):
    try:
        payload = {
            'cb': '',
            'appid': 4001,
            'nu': number,
            'vcode' : '',
            'token' : '',
            '_' : mstimestamp()
            }
        raw_json = requests.get(api_addr,params=payload,headers=header)
        track=json.loads(raw_json.text)
        if(retry>=5):
            return "查询失败!错误:-5"
        elif(track['status']=='0'):
            lst = []
            for i in range(len(track['data']['info']['context']) - 1):
                timeArray = time.localtime(int(track['data']['info']['context'][i]['time']))
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                lst.append(otherStyleTime + ', ' + track['data']['info']['context'][i]['desc'])
            return '\n'.join(lst)
        elif(track['status']=='-5'):
            if(len(raw_json.cookies)>=1):
                header['Cookie']="BAIDUID=%s"%(raw_json.cookies['BAIDUID'])
            return tracking(number,retry+1)
        else:
            return track['msg']
    except ValueError:
        return "查询接口爆炸"

