# 好耶酱 Bot

由 @eatradish 所做的 Telegram Bot，基于 python-telegram-bot 框架而做，支持群标题修改，卖萌等。 

## VPS 上的 Systemctl 配置文件

这里我借助了 Systemd 使 Bot 作为守护进程运行


```
# mkdir /var/python
# cp $LOCAL/bot.py /var/python
$ cat /usr/lib/system/bot.service
[Service]
WorkingDirectory=/var/python
ExecStart=/usr/bin/python3 bot.py
User=eatradish
restart=always

# systemctl enable bot
# systemctl start bot
```

