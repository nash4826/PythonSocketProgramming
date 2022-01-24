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

from socket import *
import threading
import time

client = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
client.connect(('127.0.0.1', 8080))  # 생성한 소켓을 통해 로컬호스트 :8080에 접속

print('클라이언트 연결 완료!')

while True:
    recvData = client.recv(1024)
    print('상대방: ', recvData.decode('utf-8'))

    sendData = input('입력: ')
    client.send(sendData.encode('utf-8'))

# Note!
# Server,Client 중 한쪽이 입력을 해야 다른 한쪽이 입력할 수 있는 코드이다.
# 동시 채팅 불가!
# 이 문제를 해결하기 위해서는 멀티 Thread를 이용해야한다.

# Thread란
# 어떠한 프로그램 내에서, 특히 프로세스 내에서 실행되는 흐름의 단위를 말한다.
# 일반적으로 한 프로그램은 하나의 스레드를 가지고 있지만, 프로그램 환경에 따라 둘 이상의 스레드를 동시에 실행할 수 있다.
# 이러한 실행 방식을 멀티스레드(multithread)라고 한다.
# ===============================================================================
