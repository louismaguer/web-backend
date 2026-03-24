"""
this client just blindly:

- lists the current contacts
- adds a hard-wired new contact
"""

import socket
import json
class ContactClient:
    def __init__( self, host, port):
        self.__host = host
        self.__port = port

    def connect(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((self.__host, self.__port))

    def command(self, cmd, **args):

        self.connect()
        data = {"cmd": cmd, "args": args}

        to_send = json.dumps(data).encode()

        # send packet
        _size = self.__socket.send( to_send )

        # receive answer
        buff = self.__socket.recv(1024).decode()
        data_srv = buff
        while buff != "":
            buff = self.__socket.recv(1024).decode()
            data_srv += buff

        # decode answer
        ret = json.loads(data_srv)
        if ret["status"] is False:
            print("ERROR : " + ret["msg"])
            return
        else:
            return ret["msg"], ret["data"]


c = ContactClient("localhost", 3001)

print("----------- list command --------------")
out = c.command("list")
print(out)
print("----------- add command --------------")
out = c.command("add", name="Basile Marchand", mail="basile.marchand@minesparis.psl.eu")
print(out)