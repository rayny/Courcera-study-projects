import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self, data_handler):
        super().__init__()
        self.data_handler = data_handler

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.data_handler(data.decode())
        self.transport.write(resp.encode())


class DataServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.data = {}

    def process_data(self, data):
        params = list(map(lambda x: x.strip(), data.split(' ')))
        result = "ok\n"
        try:
            if params[0] == 'get':
                if params[1] == '*':
                    for key in self.data:
                        for i in self.data[key]:
                            result += key + ' ' + str(self.data[key][i]) + ' ' + str(i) + '\n'
                else:
                    if params[1] in self.data:
                        for i in self.data[params[1]]:
                            result += params[1] + ' ' + str(self.data[params[1]][i]) + ' ' + str(i) + '\n'

            elif params[0] == 'put':
                if params[1] not in self.data:
                    self.data[params[1]] = {int(params[3]): float(params[2])}
                else:
                    self.data[params[1]][int(params[3])] = float(params[2])
            else:
                return 'error\nwrong command\n\n'
        except LookupError:
            return 'error\nwrong command\n\n'
        return result + '\n'

    def protocol_factory(self):
        return ClientServerProtocol(self.process_data)

    def run_server(self):
        loop = asyncio.get_event_loop()
        coro = loop.create_server(
            self.protocol_factory,
            self.host, self.port
        )

        server = loop.run_until_complete(coro)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass

        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()


def run_server(host, port):
    server = DataServer(host, port)
    server.run_server()


if __name__=='__main__':
    run_server("127.0.0.1", 8888)