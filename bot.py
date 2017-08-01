from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import requests
import subprocess
#logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

b = []
d = dict()
def tadd(bot, update):
    d = {'chat_id':'-1001139528938', 'title':'摸鱼'}
    if update.message.chat.id != -1001139528938:
        return
    name = 'eatradishhaotebot'

    if update.message.text[6:23] == name:
        str1 = update.message.text[:5]
        str2 = ''
        str3 = update.message.text[23:]
        update.message.text = str1 + str2 + str3
    b.append(update.message.text[6:])
    tadd2 = b[-1]
    tadd = "摸鱼"
    s = None
    if tadd2 == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /tadd 内容")
        return
    if len(update.message.chat.title) > 2:
        s = update.message.chat.title[4:]
        d['title'] = tadd + " - " + tadd2 + " - " + s
        requests.get('https://api.telegram.org/bot+TOKEN+/setChatTitle', data = d)
    else:
        d['title'] = tadd + " - " + tadd2
        print(d['title'])
        requests.get('https://api.telegram.org/bot+TOKEN+/setChatTitle', data = d)
def main():
    TOKEN = 'TOKEN'



    #while True:
    #i = 0
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
        #temp = updates[-1].message.text
        #if "/tadd" in updates[-1].message.text:
            #if temp != updates[-1].message.text:
            #bot.send_message(chat_id=updates[-1].message.chat_id, text="I'm a bot, please talk to me!")
                #b.append(updates[-1].message.text[6:])
               #tadd(bot, updatesi, b)
def qaq(bot, update):
    #update.message.reply_text(update.message.text)
    print(update.message)

def tclear(bot, update):
    if update.message.chat.id != -1001139528938:
        return
    tadd = "摸鱼"
    subprocess.call(["curl", "https://api.telegram.org/bot+API+/setChatTitle?chat_id=-1001139528938&title=" + tadd])
def whois(bot, update):
    name = 'eatradishhaotebot'
    if update.message.text == '/whois' or update.message.text == '/whois@' + name:
        bot.sendMessage(chat_id = update.message.chat_id, text = '用法: /whois + 域名')
        return
    if update.message.text[7:24] == name:
        str1 = update.message.text[:6]
        str2 = ''
        str3 = update.message.text[24:]
        update.message.text = str1 + str2 + str3
    print(update.message.text)
    txt = update.message.text[7:]
    a = os.popen("whois " + txt).read()
    print(txt)
    bot.sendMessage(chat_id = update.message.chat_id, text = a)
def test(bot, update):

    bot.sendMessage(chat_id = update.message.chat_id, text = "_(:3」∠)_")
    a = update.message.text
    print(a)

def tlen(bot, update):
    if update.message.chat.id != -1001139528938:
        return
    bot.sendMessage(chat_id = update.message.chat_id, text = "喵，当前群标题长度是 " + repr(len(update.message.chat.title)))
def tcat(bot, update):
    if update.message.chat.id != -1001139528938:
        return
    bot.sendMessage(chat_id = update.message.chat_id, text = update.message.chat.title)
def gum(bot, update):
    if update.message.from_user['username'] == '(不洗澡那个)`:
        update.message.reply_text("这个人的味道好奇怪的 QAQ")
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
def bmi(bot, update):
    if update.message.text == '/bmi' or update.message.text == '/bmi@eatradishhaotebot':
        bot.sendMessage(chat_id = update.message.chat_id, text = '''
        实例:
/bmi 170cm 53.6kg
/bmi 1.70m 53.6kg
可顺序倒换
        ''')
        return
    name = 'eatradishhaotebot'
    if update.message.text[5:21] == name:
        str1 = update.message.text[:4]
        str2 = ''
        str3 = update.message.text[21:]
        update.message.text = str1 + str2 + str3
    a = update.message.text
    a = a[5:]
    temp1 = 0
    temp2 = 0
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
