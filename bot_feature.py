import requests
import json
import os
import random

def tadd(msg, title_info):
    url = 'https://api.telegram.org/botTOKEN/setChatTitle'
    d = {'chat_id':'-1001125312504', 'title':'摸鱼'}
    if len(title_info) == d['title']:
        d['title'] = d['title'] + '-' + msg
    else:
        d['title'] = d['title'] + ' - ' + msg + ' - ' + title_info[4:]
    requests.get(url, data = d)

def tclear():
    d = {'chat_id':'-1001125312504', 'title':'摸鱼'}
    url = 'https://api.telegram.org/botTOKEN/setChatTitle'
    requests.get(url, data = d)

def bmi(lst):
    if len(lst) != 2:
        return "用法: /bmi kg/cm or kg/m"
    kg = ''
    cm = ''
    m = ''
    for i in lst:
        if 'kg' in i:
            kg = i
        if 'c' in i:
            cm = i
        if 'm' in i and 'c' not in i:
            m = i
    if kg == '':
        return "用法: /bmi kg/cm or kg/m"
    kg = float(kg.replace('kg', ''))
    if m != '':
        m = float(m.replace('m', ''))
        bmi = '{:.1f}'.format(kg / (m ** 2))
    if m == '':
        cm = float(cm.replace('cm', ''))
        bmi = '{:.1f}'.format(kg / ((cm / 100) ** 2))
    return bmi

def miaow(msg):
    dic = {'q': 'p', 'p': 'q', 'd': 'b', 'b': 'd'}
    run = ['a', 'w', 'u']
    lst = list(msg)
    num = 0
    for i in range(len(lst)):
        if lst[i] in dic.keys():
            lst[i] = dic[lst[i]]
    lst = list(filter(lambda x: x in dic.keys() or x in run, lst))
    while num < len(lst) - 1:
        if lst[num] in dic.keys() and lst[num + 1] not in run:
            lst.pop(num)
        else:
            num += 1
    return "".join(lst)

def whois(msg):
    return os.popen("whois " + msg).read()

def kuaidi(msg):
    comCode_url = 'https://www.kuaidi100.com/autonumber/autoComNum?text=' + msg
    headers = {'Origin': "https://www.kuaidi100.com", 'Accept-Encoding': "gzip, deflate, br", 'Accept-Language': "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2,zh-TW;q=0.2,uz;q=0.2,vi;q=0.2", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    try:
        c_r = requests.post(comCode_url, headers = headers)
        c_r = json.loads(c_r.text)
        comCode = c_r['auto'][0]['comCode']
        get_url = 'https://www.kuaidi100.com/query?type=' + comCode + '&postid=' + msg + '&id=1&valicode=&temp=0.21830105590577142'
        g_r = requests.post(get_url, headers = headers)
        g_r = json.loads(g_r.text)
        msgs = []
        for i in g_r['data']:
            msgs.append('%(time)s %(context)s' % i)
            pass
        msg = '\n'.join(msgs)
    except:
        msg = '输入错误或订单号不存在'
    return msg

def pixiv():
    url = 'https://public-api.secure.pixiv.net/v1/ranking/all?image_sizes=px_128x128%2Cpx_480mw%2Clarge&include_stats=true&page=1&profile_image_sizes=px_170x170%2Cpx_50x50&mode=daily&include_sanity_level=true&per_page=50'
    headers = {"Host": "public-api.secure.pixiv.net", "Authorization": "Bearer WHDWCGnwWA2C8PRfQSdXJxjXp0G6ULRaRkkd6t5B6h8", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "zh-cn", "Connection": "keep-alive", "Proxy-ConnectAion": "keep-alive", "User-Agent": "PixivIOSApp/5.6.0"}
    r = requests.get(url, headers = headers)
    j = json.loads(r.text)
    num = 0
    num = int(random.random() * 100)
    while num > 49:
        num = int(random.random() * 100)
    msg = j['response'][0]['works'][num]['work']['image_urls']['large']
    return msg

def couplet(msg):
    url = 'https://ai-backend.binwang.me:5001/chat/couplet/' + msg
    r = requests.get(url)
    return json.loads(r.text)['output']

def cur(lst):
    from_tkc = lst[0]
    to_tkc = lst[1]
    amount = float(lst[2])
    headers = {'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja;q=0.6,zh-TW;q=0.5,uz;q=0.4,vi;q=0.3', 'Connection': 'keep-alive', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'http://www.cngold.org/fx/huansuan.html'}
    r = requests.get("https://api.jijinhao.com/plus/convert.htm?from_tkc=" + from_tkc + '&to_tkc=' + to_tkc + '&amount=' + repr(amount), headers = headers)
    try:
        result = r.text
        msg = result.replace("var result = ", "")
        msg = msg.replace("'", "")
        return msg
    except:
        return



