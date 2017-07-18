rom telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import json
from subprocess import call
#logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

b = []
def tadd(bot, update):
    # 更改标题功能，-1001139528938 是群组 ID
    if update.message.chat.id != -1001139528938: # 防止 Bot 在其他地方更改群名
        return
    name = 'eatradishhaotebot'

    if update.message.text[6:23] == name: # 使 Boy 与其他无关内容分开
        str1 = update.message.text[:5]
        str2 = ''
        str3 = update.message.text[23:]
        update.message.text = str1 + str2 + str3
    b.append(update.message.text[6:])
    print(b)
    tadd2 = b[-1]
    tadd = "摸鱼"
    s = None
    if tadd2 == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /tadd 内容")
        return
    if len(update.message.chat.title) > 2:
        s = update.message.chat.title[4:]
        call(["curl", "https://api.telegram.org/bot + token +/setChatTitle?chat_id=-1001139528938&title=" + tadd + "%20-%20" + tadd2 + "%20-%20" + s])
    else:
        call(["curl", "https://api.telegram.org/bot + token + /setChatTitle?chat_id=-1001139528938&title=" + tadd + "%20-%20" + tadd2])
    #urllib.parse.quote_plus("https://api.telegram.org/bot433014046:AAHD1X1SDlkcdVpxZpvFK0BpEJiwOI5vY8o/setChatTitle?chat_id=-1001139528938&title"+ tadd + "%20-%20" + tadd2)
def main():
    TOKEN = 'token'
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("tadd", tadd))
    dp.add_handler(CommandHandler("tclear", tclear))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("tlen", tlen))
    dp.add_handler(MessageHandler(Filters.text, miaow))
    dp.add_handler(MessageHandler(Filters.text, gum))
    dp.add_handler(CommandHandler("tcat", tcat))
    updater.start_polling()
    updater.idle()
def tclear(bot, update): # 清理群标题
    if update.message.chat.id != -1001139528938:
        return
    tadd = "摸鱼"
    call(["curl", "https://api.telegram.org/bot + token  + /setChatTitle?chat_id=-1001139528938&title=" + tadd])

def test(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "_(:3」∠)_")
    a = update.message
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
    if update.message.from_user['username'] == 'xxx':
        update.message.reply_text("这个人的味道好奇怪的 QAQ")

def miaow(bot, update):
    baka_in = 'qpbd'
    baka_out = 'pqdb'
    baka = ''
    if len(update.message.text) > 3:
        return
    for i in range(len(baka_in)):
        if baka_in[i] in update.message.text:
            baka = baka + baka_out[i]
    bot.sendMessage(chat_id = update.message.chat_id, text = baka)

if __name__ == '__main__':
    main()
