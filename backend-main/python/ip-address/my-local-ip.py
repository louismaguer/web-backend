import socket

def get_outgoing_ip():
    with socket.create_connection(("8.8.8.8", 53)) as s:
        return s.getsockname()[0]

print("Outgoing IP:", get_outgoing_ip())
