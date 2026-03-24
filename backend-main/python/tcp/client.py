import socket

server_ip = "127.0.0.1"
server_port = 3000

params = (server_ip, server_port)
# INET = InterNet = IP
# STREAM = TCP (and UDP = DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(params)

MESSAGE = "Hello server"

print(f"Send {MESSAGE}")
s.send(MESSAGE.encode())



# La méthode `send` nous renvoie en sortie la taille du message que l'on a envoyé au serveur.
# À partir de là, il nous faut maintenant recevoir la réponse du serveur.
# Pour cela nous allons utiliser la méthode recv.
# Cependant il y a une particularité à la méthode `recv` qui est qu'elle nécessite en argument
# un entier: la taille du buffer.
# En effet, le client ne sait pas à l'avance la taille du message qu'il va recevoir
# du serveur, il est donc nécessaire de pré-allouer une taille de message fixée
# arbitrairement et de recevoir le message en plusieur morceaux si ce dernier est plus grand
# que la taille du buffer. Cette réception par morceaux peut se faire de la manière suivante


BUFF_SIZE = 1024
a = s.recv(BUFF_SIZE)
msg = a
while a != b"":
    a = s.recv(BUFF_SIZE)
    msg += a

print(f"Le client a reçu du server :\n>>>\n{msg.decode()}\n<<<")


# Et enfin une fois notre échange fini nous pouvons fermer notre client.

s.close()
