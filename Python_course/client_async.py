import asyncio
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
        self.loop = asyncio.get_event_loop()

    async def _data_handler(self, key, loop, value=None):
        reader, writer = await asyncio.open_connection(self.address, self.port, loop=loop)
        if not value:
            await writer.write(b'get ' + key.encode() + b'\n')
            data = await reader.read()
            


    def get(self, key):

        return res


    def put(self, key, value, timestamp=None):
        if not timestamp:
            timestamp = str(int(time.time()))
