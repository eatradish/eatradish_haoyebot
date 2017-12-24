import requests
import json
import os
import random
import re
import express
import shlex
import urllib.parse
import Netease
import wikipedia

moeFish_url = 'https://api.telegram.org/botTOKEN/setChatTitle'
moeFish_dict = {'chat_id':'-1001125312504', 'title':'摸鱼'}

def tadd(msg, title_info):
    if title_info == moeFish_dict['title']:
        moeFish_dict['title'] = moeFish_dict['title'] + ' - ' + msg
    else:
        moeFish_dict['title'] = moeFish_dict['title'] + ' - ' + msg + ' - ' + title_info[4:]
    requests.get(url = moeFish_url, data = moeFish_dict)

def tclear():
    requests.get(url = moeFish_url, data = moeFish_dict)

def bmi(lst):
    if len(lst) != 2:
        return "Syntax: /bmi <Weight in kilogram>kg {<Height in meter>m | <Height in centimeter>cm}"
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
        return "Syntax: /bmi <Weight in kilogram>kg {<Height in meter>m |  <Height in centimeter>cm}"

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
    if re.search(r'[qpbd]+[wau]+[qpbd]', msg) != None:
        s = re.findall(r'[A-Za-z]', msg)
        s = "".join(s)
        f = open('words_dictionary.json', 'r')
        d = json.load(f)
        f.close()
        if s in d.keys():
            return
        else:
            lst = list(msg)
            for i in range(len(lst)):
                if lst[i] in dic.keys():
                    lst[i] = dic[lst[i]]
            lst = list(filter(lambda x: x in dic.keys() or x in run, lst))
            while lst[0] in run:
                lst = lst[1:]
            while lst[-1] in run:
                lst = lst[:-1]
            return "".join(lst)
    elif msg == "ping":
        return "pong"
    elif "music.163.com/song" in msg:
        r = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
        url_list = r.findall(msg)
        lst = list(filter(lambda x: 'music.163.com/song' in x, [i[0] for i in url_list]))
        s = "".join(lst)
        temp = urllib.parse.urlsplit(s)
        mid_list = temp.path.split('/')
        mid = []
        for i in mid_list:
            try:
                int(i)
                mid.append(i)
            except:
                pass
        if len(mid) == 0:
            try:
                mid.append(temp.query.replace("id=", ""))
            except:
                pass
        url = 'http://music.163.com/api/song/detail?ids=[' + mid[0] + ']'
        req = requests.get(url)
        j = json.loads(req.text)
        msgs = []
        msgs.append(j['songs'][0]['name'])
        msgs.append(j['songs'][0]['album']['name'])
        artists = [a['name'] for a in [b for b in j['songs'][0]['artists']]]
        msgs.append(", ".join(artists))
        photo = j['songs'][0]['album']['blurPicUrl']
        msgs.append("--")
        ids = [mid[0]]
        try:
            msgs.append('320K: ' + Netease.songs_detail_new_api(ids)[0]['url'])
        except:
            pass
        finally:
            msg = "\n".join(msgs)
            return {'msgs': msg, 'photo': photo}
    else:
        return

def whois(msg):
    return os.popen("whois " + msg).read()

def kuaidi(msg):
    if type(msg) is not int:
        msg = int(msg)
    return express.tracking(msg)

def pixiv():
    url = 'https://public-api.secure.pixiv.net/v1/ranking/all?image_sizes=px_128x128%2Cpx_480mw%2Clarge&include_stats=true&page=1&profile_image_sizes=px_170x170%2Cpx_50x50&mode=daily&include_sanity_level=true&per_page=50'
    headers = {"Host": "public-api.secure.pixiv.net", "Authorization": "Bearer WHDWCGnwWA2C8PRfQSdXJxjXp0G6ULRaRkkd6t5B6h8", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "zh-cn", "Connection": "keep-alive", "Proxy-ConnectAion": "keep-alive", "User-Agent": "PixivIOSApp/5.6.0", "Referer": "http://spapi.pixiv.net/"}
    r = requests.get(url, headers = headers)
    j = json.loads(r.text)
    num = random.randint(0, 49)
    photo_url = j['response'][0]['works'][num]['work']['image_urls']['large']
    pixiv_url = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id={}'.format(urllib.parse.urlsplit(photo_url).path.split('/')[-1].replace('_p0.jpg', '').replace('_p0.png', ''))
    return {'photo': photo_url, 'pixiv': pixiv_url}

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

def guess():
    d = None
    with open('google-10000-english-usa.json', 'r') as f:
        d = json.load(f)
    return '你现在适宜 ' + random.choice(list(d.items()))[0] + ',  不适宜 ' + random.choice(list(d.items()))[0]

def decided(lst):
    if len(list(set(lst))) == 1:
        return '不' + lst[0]
    else:
        return lst[random.randint(0, len(lst) - 1)]

def wikipedia_summary(msg, lang = 'en'):
    try:
        if lang == 'en':
            wikipedia.set_lang('en')
        else:
            wikipedia.set_lang(lang)
        url = wikipedia.page(msg).url
        msg = wikipedia.summary(msg)
        fliter = []
        for i in msg:
            if i != '\n':
                fliter.append(i)
            else:
                break
        msg = "".join(fliter)
        return msg + '\n' + url
    except:
        return "Not Found Page or LANG"


