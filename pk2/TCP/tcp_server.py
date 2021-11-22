from socketserver import BaseRequestHandler, TCPServer

class TestTCPHandler(BaseRequestHandler):

    def handle(self):
        print('Handle activated', self.client_address)
        self.data = self.request.recv(1024).strip()
        self.request.send(self.data, b'(answer from server)')

server = TCPServer(('localhost', 12345), TestTCPHandler)
print('--- Server Start ---')
server.serve_forever()