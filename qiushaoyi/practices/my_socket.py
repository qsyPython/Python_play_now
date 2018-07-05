'''
网络编程：
2个进程间的通信交互！
如何实现交互？通过大家都认可的一套协议，最重要的两个协议是TCP和IP协议。

1、IP（IPv4：32位证书按8位分组得到的字符串 和IPv6：128位整数按8位分组得到的字符串）：是每个计算机的身份证，每个计算机可以有多个IP，IP地址对应的实际上是计算机的网络接口，通常是网卡！
IP协议：负责把分割成小块的数据，以IP包的形式从一台计算机通过网络发送到另一台计算机。
通过IP（获取到某计算机地址）无法实现最终的准确通信，还需要端口：来区分当前哪些应用进程，每个网络程序都向操作系统申请唯一的端口号。
一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。
所以，实现交互要做到2点：获取到IP地址、端口号和制定好对应的协议。这种实现方式叫一个Socket！

2、TCP协议则是建立在IP协议之上的，只是增加了IP包重发。
TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议（HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端）、发送邮件的SMTP协议等。

3、打开了一个网络链接：Socket又称'套接字'
应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。
一个Socket表示“打开了一个网络链接”！！！

4、啥叫服务器、啥叫客户端？
如创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。
如我用mac访问新浪，我的mac就是客户端，浏览器会主动向新浪的服务器发起连接

'''

'''
==========================practice 1: 在客户端 打开了一个网络链socket:例如访问新浪==========================
'''
# import socket
#
# #AF_INET指定使用IPv4协议,AF_INET6为IPv6;SOCK_STREAM面向流的TCP协议
# #创建一个socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 不同的服务有对应的标准端口号，如80端口是Web服务的标准端口，SMTP服务是25端口，FTP服务是21端口。
# # 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
# #客户端发起连接
# s.connect(('www.sina.com.cn', 80))
# #发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# #接收数据:包括HTTP头和网页内容
# buffer =[]
# while True:
#     d = s.recv(1024)#每次max接收1k字节
#     if d:
#         buffer.append(d)
#     else:
#         break
#
# data = b''.join(buffer)
# # 关闭连接:
# s.close()
#
# #处理接收的数据:HTTP头和网页的内容
# header, html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('sina.html','wb')as f:
#     f.write(html)


'''
==========================practice 2: 服务器编程Servce.py=========================
服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
服务器是1对多的关系！所以，
每个socket连接都需要1个新的进程或者新的线程来处理，否则，服务器1次就只能服务1个客户端了。
服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。
服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket！！！
客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。
'''

# import socket,threading,time,signal
#
# #创建socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# #绑定地址和监听端口：127.0.0.1是本机地址。
# # 如果绑定到本机地址，客户端必须同时在本机运行才能连接: 外部的计算机无法连接进来。
# host = socket.gethostname()
# port = 9999
# s.bind((host,port))
#
# # 监听端口
# s.listen(5)
# print('Waiting for client connection...')
#
# # 接收来自客户端的连接：sock为socket信息，addr为客户端的地址和端口
# def tcplink(sock,addr):
#     print('Accept new client connection from %s:%s...'%(sock,addr))
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8')=='exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
#
# # 永久循环来接受来自客户端的连接：每建立新连接都会执行！
# while True:
#     # 接受一个新连接
#     sock,addr = s.accept()
#     # 等待客户端connecting后，才会执行下面的code
#     print('每次客户端发生连接时，都会执行1遍')
#     # 创建新线程来处理TCP连接
#     t = threading.Thread(target=tcplink,args=(sock,addr))
#     t.start()
# # 要测试该程序，需要有客户端程序配套，进行连接,见practice3

'''
==========================practice 3: 配合 服务器编程 的client.py=========================
1、u/U:表示unicode字符串 如 u'我肋骨去hhh333'，对字符串进行unicode编码
2、r/R:非转义的原始字符串 如 r'我肋个去\nhhh\r是\t333',该字符串中\n\r\t均不再表示特殊的字符的含义，字符串写的啥就是啥！
3、b :表示 bytes       如  b'\xe4\xb8\xad\xe6333aaa'，表示字节，bytes每个字符都只占用一个字节。
为经过编码为bytes的字符串，通过str.encode('utf-8')方法可选择对应的编码（'ascii'）/('utf-8')/('gbk')方式
解码，就需要用decode()方法：
'''
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1',9999))
# rev_data = s.recv(1024).decode('utf-8')
# print('接收的数据：',rev_data)
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# # 发送数据:
# s.send(b'exit')
# s.close()



'''
==========================practice 4: UDP协议使用:server.py=========================
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包
但是，能不能到达就不知道了，优点很明显：就是快，虽然不一定靠谱！
服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
'''

# import socket
#
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host = socket.gethostname()
# port = 9999
# s.bind((host,port))
# print('Bind UDP on 9999...')
# while True:
#     data,addr = s.recvfrom(1024)
#     print('Received from client %s:%s.' % addr)
#     s.sendto(b'Hello,%s!'%data,addr)


'''
==========================practice 5: UDP协议使用 client.py=========================
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包
但是，能不能到达就不知道了，优点很明显：就是快，虽然不一定靠谱！
投资：努力、眼光、销售渠道、势

'''
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.sendto(data, ('127.0.0.1', 9999))
#     # 接收数据:
#     print(s.recv(1024).decode('utf-8'))
# s.close()


# 编码解码走一波
tt1 = '我就改了沮丧看了jjj'
tt2 = b'\xd3\xc3\xbb\xa7\xce\xde\xc8\xa8\xb5\xc7\xc2\xbd'
print(tt1.encode('utf-8',errors='ignore'),tt2.decode('gbk',errors='ignore'))













