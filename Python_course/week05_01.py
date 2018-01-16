import socket
import time

BUFFERSIZE = 1024

class ClientError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Client:
    def __init__(self, address, port, timeout=None):
        self.address = address
        self.port = port
        self.timeout = timeout

    def get(self, key):
        try:
            with socket.create_connection((self.address, self.port), timeout=self.timeout) as sock:
                sock.sendall(b'get ' + key.encode() + b'\n')
                data = sock.recv(BUFFERSIZE).decode()
        except (socket.timeout, socket.error):
            raise ClientError
        result = {}
        if data.splitlines()[0] != 'ok':
            raise ClientError
        for line in data.splitlines()[1:]:
            if line:
                if not line.split(' ')[0] in result:
                    result[line.split(' ')[0]] = [(int(line.split(' ')[2]), float(line.split(' ')[1]))]
                else:
                    result[line.split(' ')[0]].append((int(line.split(' ')[2]), float(line.split(' ')[1])))
        return result

    def put(self, key, value, timestamp=None):
        if not timestamp:
            timestamp = str(int(time.time()))
        else:
            timestamp = str(int(timestamp))
        try:
            with socket.create_connection((self.address, self.port), timeout=self.timeout) as sock:
                sock.send(b'put ' + key.encode() + b' ' + str(value).encode() + b' ' + timestamp.encode() + b'\n')
                result = sock.recv(BUFFERSIZE).decode()
        except (socket.timeout, socket.error):
            raise ClientError
        if result.splitlines()[0] != 'ok':
            raise ClientError
