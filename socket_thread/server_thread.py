#   Server                     Client

# making socket              making socket
#     ↓                          ↓
#    bind                        ↓
#     ↓                          ↓
#   listen                       ↓
#     ↓                          ↓
#   accept ←←←←←←←←←←←←←←←←←←← connect
#     ↓                          ↓
# send & recv ←-----------→ send & recv
#     ↓                          ↓
# socketclose                socketclose

# multithread 적용
# (import threading,time 와 send,receive 함수 제작)

from socket import *
import threading
import time


def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8080

server = socket(AF_INET, SOCK_STREAM)
server.bind(('', port))
server.listen(1)

print('Port: %d connect standbying....' % port)

connectionSock, addr = server.accept()

print(str(addr), '에서 접속되었습니다.')

# threading.Thread(target=함수, args=(함수인자,))
sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    # sleep를 불러오는 이유는
    # while문으로 인한 프로세스와 쓰레드가 무한 동작으로 인한 부하 방지
    # 요즘 컴퓨터가 좋아서 과부하까지는 오지 않을듯 싶으나,
    # 노트북 쿨러가 미친듯이 돌거나, 배터리가 쭉쭉 닳을 듯 싶어
    # sleep 메서드를 호출하여 1초씩 쉬게
    pass
