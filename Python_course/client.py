import socket
import time


class ClientError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Client:
    def __init__(self, address, port, timeout=None):
        self.address = address
        self.port = port
        self.timeout = timeout

    def get(self, key):
        pass

    def put(self, key, value, timestamp=None):
        if not timestamp:
            timestamp = str(int(time.time()))
