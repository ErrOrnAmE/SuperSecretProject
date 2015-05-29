import socket, interpretation
 
UDP_IP = "172.30.10.207"
UDP_PORT = 9004
MESSAGE = (b"WeLeakedGot")

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet 
socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
interprete = interpretation.Interpretation()

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("recu :", data)
    message = data.decode()    
    reponse = interprete.routeur(message)
    print ("-> ",reponse)
    if reponse == "win":
        print ("On a perdu ! :(")
        sock.close()
        exit()
    elif reponse == "loose":
        print ("On a gagne ! :)")
        sock.close()
        exit()
    elif reponse == "stop":
        sock.close()
        exit()
    elif reponse != "":
        sock.sendto(reponse.encode(), (UDP_IP, UDP_PORT))