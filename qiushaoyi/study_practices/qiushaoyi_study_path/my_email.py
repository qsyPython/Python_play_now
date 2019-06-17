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
    （发邮件 遵循SMTP 需输入地址、口令配置SMTP服务器）       分割线   (收邮件 遵循IMAP或POP3 需输入地址口令配置POP3或IMAP服务器)
'''
'''
==========================practice 1: 发送 邮件文本和链接 ==========================
Python对SMTP支持有smtplib和email两个模块。
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
# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import parseaddr,formataddr
# import smtplib
#
# def _format_addr(s):
#     name,addr = parseaddr(s)
#     header = Header(name,'utf-8').encode()
#     return formataddr((header,addr))
# #发送文本内容
# from_addr = input('From:')
# password = input('Password:')# 该password为设置的第3方登陆授权码
# to_addr1 = input('To:')
# to_addr2 = input('To:')
#
#
# # 发送的内容：
# # 1、文本
# # msg = MIMEText('爱你么么哒... ','plain','utf-8')
#
# # 2、链接
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
# msg['From'] = _format_addr('Python 爱好者<%s>'%from_addr)
# msg['To'] = _format_addr('管理员<%s>,<%s>'%(to_addr1,to_addr2))
# msg['Subject'] = Header('来自qsy的问候...','utf-8').encode()
# smtp_server = input('SMTP server:') # 一般为：smtp.邮箱@后的内容.com
#
# try:
#     server = smtplib.SMTP(smtp_server,25)# SMTP协议默认端口是25
#     server.set_debuglevel(1)
#     server.starttls()
#     server.login(from_addr,password)
#     server.sendmail(from_addr,[to_addr1],msg.as_string())
#     server.quit()
#     print("发送成功")
# except smtplib.SMTPException as e:
#     print('失败了%s',e)
#     # 问题：网易系列554 DT: SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。
#     # 请检查是否有用户发送病毒或者垃圾邮件


'''
==========================practice 2: email：发送 附件==========================
使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。
要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。Gmail端口是587。
具体的服务器和端口：
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server.starttls()
'''

# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import parseaddr,formataddr
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# import smtplib
#
# def _format_addr(s):
#     name,addr = parseaddr(s)
#     header = Header(name,'utf-8').encode()
#     return formataddr((header,addr))
# #发送文本内容
# from_addr = input('From:')
# password = input('Password:')# 该password为设置的第3方登陆授权码
# to_addr1 = input('To:')
# to_addr2 = input('To:')
#
# # msg = MIMEMultipart('')
# # 若是3、发送附件：支持HTML和Plain格式,解决对方无法查看html问题,增加可选机制
# msg = MIMEMultipart('alternative')
# msg['From'] = _format_addr('Python 爱好者<%s>'%from_addr)
# msg['To'] = _format_addr('管理员<%s>,<%s>'%(to_addr1,to_addr2))
# msg['Subject'] = Header('来自qsy的问候...','utf-8').encode()
#
# # 1、发送附件+纯文本
# # msg.attach(MIMEText('send with file...','plain','utf-8'))
#
# # 2、发送附件+html、直接发送图片到正文：若有多个图片，给它们依次编号，然后引用不同的cid:x即可
# # msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
# #     '<p><img src="cid:0"></p>' +
# #     '</body></html>', 'html', 'utf-8'))
#
# # 3、发送附件：支持HTML和Plain格式,解决对方无法查看html问题
#
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
#
# with open('/Users/mac/Desktop/WechatIMG39.jpeg','rb') as f:
#     mime = MIMEBase('image','jpeg',filename='WechatIMG39.jpeg')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.jpeg')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)
#
# smtp_server = input('SMTP server:') # 一般为：smtp.邮箱@后的内容.com
# try:
#     server = smtplib.SMTP(smtp_server,25)# SMTP协议默认端口是25，连接的是明文传输，发送邮件的整个过程可能会被窃听
#     server.set_debuglevel(1)
#     server.starttls()
#     server.login(from_addr,password)
#     server.sendmail(from_addr,[to_addr1],msg.as_string())
#     server.quit()
#     print("发送成功")
# except smtplib.SMTPException as e:
#     print('失败了%s',e)
#     # 问题：网易系列554 DT: SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。
#     # 请检查是否有用户发送病毒或者垃圾邮件



'''
==========================practice 3: email：接收 邮件==========================
第一步：用poplib把邮件的原始文本下载到本地；
第二部：用email解析原始文本，还原为邮件对象,展示出来

126邮箱：
POP3服务器 pop.126.com	 110
IMAP服务器 imap.126.com	 143

'''
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = input('Email:')
password = input('Password:')
pop3_server = input('POP3 server:')

# 邮件的Subject或者Email中包含的名字都是经过编码后的str，
# 要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 文本邮件的内容也是str，还需要检测编码，
# 否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
#Message对象本身可能是一个MIMEMultipart对象,即包含嵌套的其他MIMEBase对象
# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# 连接到POP3服务器:
server = poplib.POP3(pop3_server,110)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

# 服务器进行身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages当前返回的数量和空间: %s. Size: %s' % server.stat())

# list()返回所有邮件的编号:
resp,mails,octets = server.list()
print('返回所有邮件的编号:',mails)

# 获取最新一封邮件, 注意索引号从 1 开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# 逐行获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 解析出邮件为Message对象:
msg = Parser().parsestr(msg_content)

print_info('获取到新发邮件的内容：',msg)
# 关闭连接:
server.quit()





