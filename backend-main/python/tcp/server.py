import os
import socketserver

class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        print(f"Receive {data}")
        cur_pid = os.getpid()
        response = f'received by server (pid={cur_pid}): {data.decode()}'
        self.request.send(response.encode())
        return

# use ThreadingMixIn rather than ForkingMixIn b/c of Windows
#class ForkingEchoServer(socketserver.ForkingMixIn, socketserver.TCPServer):
class ForkingEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 3000) # let the kernel give us a port
    server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    ip, port = server.server_address # find out what port we were given

    print(f"Server listen at {ip}:{port}")

    t = threading.Thread(target=server.serve_forever)
    #t.setDaemon(True) # don't hang on exit
    t.start()
    print('Server loop running in process:', os.getpid())
