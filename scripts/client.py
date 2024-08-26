import socket
import dill as pickle


class Network:
    def __init__(self, host="localhost", port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.turn = self.connect()
        self.board = self.send(700)

    def connect(self):
        try:
            self.client.connect(self.addr)
            # print(f"Connecting to {self.host} : {self.port}")
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            board = pickle.dumps(data)
            self.client.send(board)
            reply = pickle.loads(self.client.recv(2048))
            return reply
        except socket.error as e:
            return str(e)
