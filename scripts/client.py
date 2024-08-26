import socket
import dill as pickle


class Network:
    def __init__(self, host="localhost", port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.board = pickle.loads(self.connect())

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048)

    def send(self, data):
        try:
            board = pickle.dumps(data)
            self.client.send(board)
            reply = pickle.loads(self.client.recv(2048))
            return reply
        except socket.error as e:
            return str(e)


client = Network()
