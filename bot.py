from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import requests
import subprocess
#logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

b = []
d = dict()
# 添加群标题
def tadd(bot, update):
    d = {'chat_id':'-1001139528938', 'title':'摸鱼'}
    if update.message.chat.id != -1001139528938:
        return
    # 这里用于群组判断，如果不是在这个群组内改名，则 returm 终止方法。（为了不让在其他地方乱改群名
    name = 'eatradishhaotebot'
    if update.message.text[6:23] == name:
        str1 = update.message.text[:5]
        str2 = ''
        str3 = update.message.text[23:]
        update.message.text = str1 + str2 + str3
    # 用于与无关内容分类，比如 /tadd@eatradishhaotebot 智障 01 则把 ‘@eatradishhaotebot’ 字符串替换掉    
    b.append(update.message.text[6:])
    tadd2 = b[-1]
    tadd = "摸鱼"
    s = None
    # 如果用户只输入了一个命令，并没有输入要添加的标题，则让 Bot 发送用法并终止此方法
    if tadd2 == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /tadd 内容")
        return
    # 使用 requests 方法能够支持对字符串的转义，详情看文档
    if len(update.message.chat.title) > 2:
        s = update.message.chat.title[4:]
        d['title'] = tadd + " - " + tadd2 + " - " + s
        requests.get('https://api.telegram.org/bot+TOKEN+/setChatTitle', data = d)
    else:
        d['title'] = tadd + " - " + tadd2
        print(d['title'])
        requests.get('https://api.telegram.org/bot+TOKEN+/setChatTitle', data = d)
    # 这里主要是两种情况的处理，a.首次添加标题时 b.再次 (>2) 添加标题时
def main():
    TOKEN = 'TOKEN'

    # 详情看 python-telegram-bot 的 echobot 事例


        # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)
    #tadd(updater)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    #print(update.message.text)
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("whois", whois))
    #dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bmi", bmi))
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, tadd))
    dp.add_handler(CommandHandler("tadd", tadd))
    dp.add_handler(CommandHandler("tclear", tclear))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("tlen", tlen))
    dp.add_handler(MessageHandler(Filters.text, miaow))
    dp.add_handler(MessageHandler(Filters.text, gum))
    #dp.add_handler(MessageHandler(Filters.text, qaq))
    dp.add_handler(CommandHandler("tcat", tcat))
    #dp.add_handler(MessageHandler(Filters.text, qaq))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    
# 设置群标题为默认值，这里我用了 subrocess.call 方法调用了 curl, curl 访问了 API 的 URL 地址进行改变
# 你也可以用 request, 像上面那样，这里我偷懒了而已。
def tclear(bot, update):
    if update.message.chat.id != -1001139528938:
        return
    tadd = "摸鱼"
    subprocess.call(["curl", "https://api.telegram.org/bot+API+/setChatTitle?chat_id=-1001139528938&title=" + tadd])
# whois 功能，这里我调用了外部 os 命令 whois，然后用 os.popen 接受 whois 这个命令返回的字符串，再让 bot 发送出去
def whois(bot, update):
    name = 'eatradishhaotebot'
    # 当用户输入不输入接受的参数，只输入 '/whois' 这个命令的时候，机器人发送用法，之后终止这个方法
    if update.message.text == '/whois' or update.message.text == '/whois@' + name:
        bot.sendMessage(chat_id = update.message.chat_id, text = '用法: /whois + 域名')
        return
    # 无关内容 '@eatradishhaotebot' 分离
    if update.message.text[7:24] == name:
        str1 = update.message.text[:6]
        str2 = ''
        str3 = update.message.text[24:]
        update.message.text = str1 + str2 + str3
    print(update.message.text)
    # 提取 '/whois' 之后的字符串，既用户想查询的域名
    txt = update.message.text[7:]
    # 调用外部命令，发送
    a = os.popen("whois " + txt).read()
    print(txt)
    bot.sendMessage(chat_id = update.message.chat_id, text = a)
# 测试模块，用于调试 bot
def test(bot, update):

    bot.sendMessage(chat_id = update.message.chat_id, text = "_(:3」∠)_")
    a = update.message.text
    print(a)
# 查看群标题长度
def tlen(bot, update):
    if update.message.chat.id != -1001139528938:
        return
    bot.sendMessage(chat_id = update.message.chat_id, text = "喵，当前群标题长度是 " + repr(len(update.message.chat.title)))
# 查看当前群标题
def tcat(bot, update):
    if update.message.chat.id != -1001139528938:
        return
    bot.sendMessage(chat_id = update.message.chat_id, text = update.message.chat.title)
# 某个不洗澡，发消息的时候 bot 就回消息
def gum(bot, update):
    if update.message.from_user['username'] == '(不洗澡那个)`:
        update.message.reply_text("这个人的味道好奇怪的 QAQ")
# qpbd -> pqdb
def miaow(bot, update):
    lst = list(update.message.text)
    baka = ['q', 'p', 'b', 'd']
    if len(lst) == 3 and lst[1] in ['a', 'u', 'w']:
        if lst[0] in baka and lst[2] in baka:
            for i in range(len(lst)):
                if lst[i] == "q":
                    lst[i] = "p"
                elif lst[i] == "p":
                    lst[i] = "q"
                elif lst[i] == "b":
                    lst[i] = "d"
                elif lst[i] == "d":
                    lst[i] = "b"
                else: continue
            s2 = "".join(lst)
            bot.sendMessage(chat_id = update.message.chat_id, text = s2)
# bmi 计算
def bmi(bot, update):
  # 当用户只输入了 '/bmi' 没有输入参数时，机器人发送用法，之后终止方法。
    if update.message.text == '/bmi' or update.message.text == '/bmi@eatradishhaotebot':
        bot.sendMessage(chat_id = update.message.chat_id, text = '''
        实例:
/bmi 170cm 53.6kg
/bmi 1.70m 53.6kg
可顺序倒换
        ''')
        return
     # 分离无关内容 `@eatradishhaotebot'
    name = 'eatradishhaotebot'
    if update.message.text[5:21] == name:
        str1 = update.message.text[:4]
        str2 = ''
        str3 = update.message.text[21:]
        update.message.text = str1 + str2 + str3
    # 接收消息，提取用户输入的除命令之外的字符串
    a = update.message.text
    a = a[5:]
    # temp1, temp2 是下面用于检测字符串的东西
    temp1 = 0
    temp2 = 0
    # 检测用户输入的东西是 kg/cm 还是 kg/m
    if 'kg' and 'cm' in a:
        for i in range(len(a)):
            if a[i] == 'k':
                temp1 = i
            if a[i] == 'c':
                temp2 = i

    if 'c' not in a and 'kg' in a and 'm' in a:
        for i in range(len(a)):
            if a[i] == 'k':
                temp1 = i
            if a[i] == 'm':
                temp2 = i
    # 再次从用户输入的信息中提取字符串，转化为 float 并开始计算它们的值
    # 有两种情况，如果用户输入的是 'w/h' 则正常执行，当用户输入的事 'h/w' 则会出现错误，因此使用 try/except 处理异常
    try:
        num1 = a[:temp1]
        num2 = a[temp1 + 2 : temp2]
        num1 = float(num1)
        num2 = float(num2)
        print(num1, num2)
        if 'c' in a:
            bmi = num1 / ((num2 / 100) ** 2)
        if 'c' not in a:
            bmi = num1 / (num2 ** 2)
        bmi = '{:.1f}'.format(bmi)
        bot.sendMessage(chat_id = update.message.chat_id, text = repr(bmi))

    except:
        num1 = a[:temp2]
        num2 = a[temp2 + 2 : temp1]
        num1 = float(num1)
        num2 = float(num2)
        print(num1, num2)
        if 'c' in a:
            bmi = num2 / ((num1 / 100) ** 2)
        if 'c' not in a:
            bmi = num2 / (num1 ** 2)
        bmi = '{:.1f}'.format(bmi)
        bot.sendMessage(chat_id = update.message.chat_id, text = repr(bmi))

if __name__ == '__main__':
    main()
