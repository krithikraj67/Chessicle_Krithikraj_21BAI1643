import socket
from _thread import *
import dill as pickle
from board import Board

"""

Server codes to get info:
700: Get board

"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for connection...")

bo = Board()
token = ["A", "B"]
num = 0


def threaded_client(conn):
    global bo, num
    conn.send(str.encode(token[num % 2]))
    num += 1

    while True:
        try:
            data = conn.recv(2048)
            if not data:
                break
            reply = pickle.loads(data)
            if reply == 700:
                conn.send(pickle.dumps(bo))
            else:
                bo = reply
                conn.sendall(data)
        except:
            print(e)
            break

    print("Connection closed")
    conn.close()
    num -= 1


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))
