from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect(('localhost', 8888))

clientSocket.send("hahah".encode("utf-8"))
recvData = clientSocket.recv(1024)
print("recvData:%s"%recvData.decode("utf-8"))

clientSocket.close()