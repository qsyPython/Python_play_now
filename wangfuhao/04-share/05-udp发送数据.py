print("------------------udp发数据------------------")
from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

#使用udp发送的数据，在每一次的是都需要写上接收方的ip和port
#注意:在python3中 需要.encode("utf-8")  也可以跟gb2312编码 具体什么编码,要看接收方使用什么编码,需要一致
#接受到的数据也是utf-8编码过的,接受的时候也需要解码
udpSocket.sendto("haha".encode("utf-8"), ("", 8080))
udpSocket.sendto("haha1".encode("utf-8"), ("", 8080))