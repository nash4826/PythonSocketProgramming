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
server = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
server.bind(('', 8080))  # 포트에 바인딩
server.listen(1)  # 접속할 클라이언트 수(1)
connectionSock, addr = server.accept()

print('클라이언트 접속 확인 -> 서버 연결 완료')
while True:
    sendData = input('입력: ')
    # send로 보낼때 utf-8로 인코딩! recive할때는 utf-8로 디코딩 명심!
    connectionSock.send(sendData.encode('utf-8'))

    # 소켓에서 1024byte만큼 가져오곘다. buffer?
    recvData = connectionSock.recv(1024)
    # 데이터를 byte로 수신하기 때문에 문자열로 활용하기 위해서는 decoding을 해야함
    print('상대방: ', recvData.decode('utf-8'))

# Note!
# Server,Client 중 한쪽이 입력을 해야 다른 한쪽이 입력할 수 있는 코드이다.
# 즉, 한쪽이 문자열을 입력 후 enter 키를 누를 때까지 다른 한쪽은 입력하지 못하고 대기중인 상태란 뜻.(반쪽짜리 채팅 프로그램)
# 이 문제를 해결하기 위해서는 멀티 Thread를 이용해야한다.

# Thread란
# 어떠한 프로그램 내에서, 특히 프로세스 내에서 실행되는 흐름의 단위를 말한다.
# 일반적으로 한 프로그램은 하나의 스레드를 가지고 있지만, 프로그램 환경에 따라 둘 이상의 스레드를 동시에 실행할 수 있다.
# 이러한 실행 방식을 멀티스레드(multithread)라고 한다.
# ===============================================================================
# multithread 적용 (import threading,time)
