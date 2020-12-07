"""
Alessia De Giovannini
Diffie-Hellman Client UDP
"""
import socket
import random

def generate_private_key(N,g):
    b = random.randint(1, N)
    B = (g ** b) % N
    return B, b

def decifra(A, N ,b):
    k  = (A ** b) % N
    return k
    
def client():
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_porta = ("127.0.0.1", 20001)
    bufferSize = 1024

    msgPerServer = "INIZIO SCAMBIO"
    bytesSend = str.encode(msgPerServer)
    socketClient.sendto(bytesSend, ip_porta)

    datisocket = socketClient.recvfrom(bufferSize)
    N, g, A = datisocket[0].decode().split(" ")
    N = int(N)
    g = int(g)
    A = int(A)

    #B pubblica b privata
    B,b = generate_private_key(N, g)

    #invio chiave publica B al server
    bytesSend =  str.encode(str(B))
    socketClient.sendto(bytesSend, ip_porta)

    print(decifra(A, N, b))


def main(): 
    client()

if __name__ == "__main__":
    main()