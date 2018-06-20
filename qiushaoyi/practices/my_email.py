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
email负责构造邮件，smtplib负责发送邮件。

问题123：
1. 一开始取名email.py，跟库名冲突
from email.mime.text import MIMEText
2. 
“  File "/usr/local/lib/python2.7/smtplib.py", line 614, in login
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (550, '\xd3\xc3\xbb\xa7\xce\xde\xc8\xa8\xb5\xc7\xc2\xbd')”
发信邮箱的SMTP服务需要打开
3.
“File "/usr/local/lib/python2.7/smtplib.py", line 738, in sendmail
    raise SMTPDataError(code, resp)
smtplib.SMTPDataError: (554, 'DT:SPM smtp5, jtKowAAnL9uJ_UJW9CsUDQ--.62928S2 1447230858 http://mail.163.com/help/help_spam_16.htm?ip=42.120.174.7&hostid=smtp5&time=1447230858')
”
被系统拒信，内容一定要长！

个人邮箱和：
# qsy118614@126.com
# qsy118614@163.com
# 1129331905@qq.com
# smtp.126.com 端口多是25
# smtp.163.com
# smtp.qq.com


'''
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    header = Header(name,'utf-8').encode()
    return formataddr((header,addr))
#发送文本内容
from_addr = input('From:')
password = input('Password:')# 该password为设置的第3方登陆授权码
to_addr1 = input('To:')
to_addr2 = input('To:')


# 发送的内容：文本、链接、附件
msg = MIMEText('爱你么么哒... ','plain','utf-8')
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>'%from_addr)
msg['To'] = _format_addr('管理员 <%s>,<%s>'%(to_addr1,to_addr2))
msg['Subject'] = Header('来自qsy的问候……','utf-8').encode()
smtp_server = input('SMTP server:') # 一般为：smtp.邮箱@后的内容.com
try:
    server = smtplib.SMTP(smtp_server,25)# SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.starttls()
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr1],msg.as_string())
    server.quit()
    print("发送成功")
except smtplib.SMTPException as e:
    print('失败了%s',e)
    # 问题：网易系列554 DT: SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。
    # 请检查是否有用户发送病毒或者垃圾邮件








