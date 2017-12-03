from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, JobQueue
import bot_feature
from telegram import ParseMode
from pprint import *
import logging
import shlex
#logging.basicConfig(level=logging.DEBUG,
#format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = 'TOKEN'

def args_to_list(msg):
    return shlex.split(msg)

def msg_to_arg(msg):
    msg = replace_rub_str(msg)
    msg = replace_command_str(msg)
    return msg

def replace_rub_str(msg):
    lst = msg.split()
    if '@eatradishhaotebot' in lst[0]:
        lst[0] = lst[0].replace('@eatradishhaotebot', '')
        return ' '.join(lst)
    else:
        return msg

def replace_command_str(msg):
    lst = msg.split()
    if '/' in lst[0]:
        lst.remove(lst[0])
    return ' '.join(lst)

def tadd(bot, update):
    msg = msg_to_arg(update.message.text)
    print(msg)
    if update.message.chat.id != -1001125312504:
        return
    if msg == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /tadd 内容")
        return
    else:
        bot_feature.tadd(msg, update.message.chat.title)

def tcat(bot, update):
    if update.message.chat.id != -1001125312504:
        return
    bot.sendMessage(chat_id = update.message.chat_id, text = update.message.chat.title)

def tclear(bot, update):
    if update.message.chat.id != -1001125312504:
        return
    else:
        bot_feature.tclear()

def test(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "_(:3」∠)_")
    pprint(update.message)

def tlen(bot, update):
    if update.message.chat.id != -1001125312504:
        return
    bot.sendMessage(chat_id = update.message.chat_id, text = "喵，当前群标题长度是 " + repr(len(update.message.chat.title)))

def miaow(bot, update):
    msg = bot_feature.miaow(update.message.text)
    if msg != None:
        bot.sendMessage(chat_id = update.message.chat_id, text = msg)

def bmi(bot, update):
    msg = msg_to_arg(update.message.text)
    lst = args_to_list(msg)
    if msg == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = 'Syntax: ```/bmi <Weight in kilogram>kg {<Height in meter>m | <Height in centimeter>cm}```', parse_mode = ParseMode.MARKDOWN)
        return
    result = bot_feature.bmi(lst)
    update.message.reply_text(result)

def kuaidi(bot, update):
    msg = msg_to_arg(update.message.text)
    if msg == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /kuaidi + 运单号")
        return
    msg = int(msg)
    msg = bot_feature.kuaidi(msg)
    update.message.reply_text(msg)

def pixiv(bot, update):
    msg = bot_feature.pixiv()
    bot.sendMessage(chat_id = update.message.chat_id, text = msg)

def couplet(bot, update):
    msg = msg_to_arg(update.message.text)
    if msg == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /couplet + 被对联")
        return
    msg = bot_feature.couplet(msg)
    update.message.reply_text(msg)

def cur(bot, update):
    msg = msg_to_arg(update.message.text)
    lst = args_to_list(msg)
    if msg == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /cur + 被转换货币 转换货币 转换数目")
    msg = bot_feature.cur(lst)
    bot.sendMessage(chat_id = update.message.chat_id, text = msg)

def whois(bot, update):
    msg = msg_to_arg(update.message.text)
    if msg == '':
        bot.sendMessage(chat_id = update.message.chat_id, text = "用法: /whois + 域名")
    msg = bot_feature.whois(msg)
    bot.sendMessage(chat_id = update.message.chat_id, text = msg)

def guess(bot, update):
    msg = bot_feature.guess()
    update.message.reply_text(msg)

def decided(bot, update):
    msg = msg_to_arg(update.message.text)
    lst = args_to_list(msg)
    print(lst)
    if len(lst) == 0 or len(lst) == 1:
        msg = '用法: /decided [选项 1][选项 2][选项 3]...'
    else:
        msg = bot_feature.decided(lst)
    update.message.reply_text(msg)

if __name__ == '__main__':
    updater = Updater(TOKEN)
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
    dp.add_handler(CommandHandler("kuaidi", kuaidi))
    dp.add_handler(MessageHandler(Filters.text, miaow))
    #dp.add_handler(MessageHandler(Filters.text, moe))
    #dp.add_handler(MessageHandler(Filters.text, gum))
    #dp.add_handler(MessageHandler(Filters.text, qaq))
    dp.add_handler(CommandHandler("tcat", tcat))
    dp.add_handler(CommandHandler("pixiv", pixiv))
    dp.add_handler(CommandHandler("couplet", couplet))
    dp.add_handler(CommandHandler("cur", cur))
    dp.add_handler(CommandHandler("guess", guess))
    dp.add_handler(CommandHandler("decided", decided))
    #dp.add_handler(MessageHandler(Filters.text, qaq))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

