'''
电子邮件：
邮件用户代理：电子邮件软件 即MUA
先到
邮件传输代理：Email服务提供商 即邮件MTA(有很多，会经历几个MTA)
再到
邮件投递代理：邮件投递的最终目的 即MDA
最后到
邮件用户代理：电子邮件软件 即MUA

总过程：
发件人 -> MUA -> MTA -> MTA -> 若干个MTA----------> MDA <- MUA <- 收件人
    （发邮件 遵循SMTP 输入地址、口令配置SMTP服务器）       分割线   (收邮件 遵循IMAP或POP3，输入地址口令配置POP3或IMAP服务器)
'''
'''
==========================practice 1: ==========================
Python对SMTP支持有smtplib和email两个模块
email负责构造邮件，smtplib负责发送邮件
'''
from email.mime.text import MIMEText
import smtplib

#发送文本内容
msg = MIMEText('hello,send by Python... ','plain','utf-8')
from_addr = input('From:')
password = input('Password:')
to_addr1 = input('To:')
to_addr2 = input('To:')
smtp_server = input('SMTP server:')

server = smtplib.SMTP(smtp_server,25)# SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr1,to_addr2],msg.as_string())
server.quit()











