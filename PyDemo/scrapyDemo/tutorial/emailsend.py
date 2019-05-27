# encoding: utf-8

"""
File: emailsend.py
Author: Rock Johnson
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr, parseaddr

def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode('utf-8'), addr))

from_addr = 'spiderSender@163.com'
to_addr = '836867547@qq.com'

msg = MIMEText('<h3>请扫描下方二维码登录</h3>\n<img src="https://static.zhipin.com/v2/web/geek/images/logo.png">', 'html', 'utf-8')
msg['From'] = format_addr('爬虫登录 <%s>' % from_addr)
msg['To'] = to_addr
msg['Subject'] = Header('爬虫登录二维码', 'utf-8')

mailer = smtplib.SMTP('smtp.qq.com')
mailer.set_debuglevel(1)
mailer.login(to_addr, 'kxpswqagpirlbcdd')
# mailer.login(from_addr, 'k836867547sqm')
mailer.sendmail(to_addr, to_addr, msg.as_string())
mailer.quit()