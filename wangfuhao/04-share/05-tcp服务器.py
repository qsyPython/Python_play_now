from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("", 8888))

serverSocket.listen(5)

print("-----1-------")
#clientSocket 表示这个新的客户端
#clientInfo 表示这个新的客户端的ip以及port
clientSocket,clientInfo = serverSocket.accept() #f返回值是一个元组

print("-----2-------")
recvData = clientSocket.recv(1024)
print("%s:%s"%(str(clientInfo), recvData.decode("utf-8")))

clientSocket.close()
serverSocket.close()