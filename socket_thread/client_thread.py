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
# (import threading,time 와 send,receive 함수 제작 )

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

client = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
client.connect(('127.0.0.1', port))  # 생성한 소켓을 통해 로컬호스트 :8080에 접속

print('클라이언트 연결 완료!')

sender = threading.Thread(target=send, args=(client,))
receiver = threading.Thread(target=receive, args=(client,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
