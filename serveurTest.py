import socket

UDP_IP = "172.30.10.20"
UDP_PORT = 9004
 
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind(('', UDP_PORT))

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print ("received message:", data)
envoie = "1-Bonjour "+data.decode()+"\nVous etes le Joueur 1 (ROUGE), attente suite ..."
sock.sendto(envoie, addr)

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
    recu = data.decode()
    mes = input("envoyer ? ")
    sock.sendto(mes.encode(), addr)