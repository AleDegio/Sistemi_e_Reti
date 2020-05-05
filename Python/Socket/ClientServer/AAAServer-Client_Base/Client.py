"""
Alessia De Giovannini
Client
"""
import socket

msgPerClient = "Salve signor Server"
bytesSend = str.encode(msgPerClient)
porta = ("192.168.1.58", 20001)
bufferSize = 1024

#Creazione del Socket Client 
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Mandare un msg al signor Server 
socketClient.sendto(bytesSend, porta)
msgPerServer = socketClient.recvfrom(bufferSize)
msg = "Messaggio dal signor Server {}".format(msgPerServer[0])

print(msg)