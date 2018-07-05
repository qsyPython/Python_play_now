print("------------------udp收数据------------------")
from socket import *

def main():
    udpSocket1 = socket(AF_INET, SOCK_DGRAM)

    udpSocket1.bind(("", 8080))#绑定的目的：为了让接收方有一个明确的地址

    while True:
        recvData = udpSocket1.recvfrom(1024) #recvData是一个元组,有发送方的IP地址和端口信息以及内容
        content,destInfo = recvData  #这句话相当于解包content保存发送方的内容,destInfo保存发送方的信息
        print(content.decode("utf-8")) #接受到数据的时候,需要指定解析数据的编码

if __name__ == '__main__':
    main()