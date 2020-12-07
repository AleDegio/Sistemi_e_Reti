"""
Alessia De Giovannini
Diffie-Hellman Server UDP
"""
import socket
import random

def creating_public_keys():
    N = n_primo(random.randint(1, 10))
    g =  random.randint(1, N)
    return N, g

def creating_private_key(N, g):
    a  = random.randint(1, N) #private keys
    A = (g ** a) % N    #A is public
    return A, a

def decifra(N, a , B):
    k = (B ** a) % N
    return k

def server():
    ip = "127.0.0.1"
    porta = 20001
    bufferSize = 1024

    #Creazione del Socket Server  
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    socketServer.bind((ip, porta))
    print("il signor Server la puo' ricevere")

    #Fase di Ascolto 
    while(True):
        datiSocket = socketServer.recvfrom(bufferSize)
        msgC = datiSocket[0].decode()
        address = datiSocket[1]
        
        
        if msgC == "INIZIO SCAMBIO":
            N, g =  creating_public_keys()
            A , a = creating_private_key(N, g)

            #N, g, A is public
            # a is private 
            msgClientServer = str(N) + " " + str(g) + " " + str(A) #Trasmetto chiavi pubbliche

            bytesSend = str.encode(msgClientServer)
            socketServer.sendto(bytesSend, address)

            datiSocket2 = socketServer.recvfrom(bufferSize)
            B = int(datiSocket2[0].decode()) #ottengo chiave pubblica generata dal client
            
            print(decifra(N, a, B))
    
        

def n_primo(numero):
    j = 0
    k = 0 
    i = 2
    while k < numero: 
        div = 2
        count = 0
        while div<=i/2 and count==0:
            if i % div == 0:
                count+=1
            div += 1
        if count == 0:
            j = i
            k = k + 1
        
        i = i + 1

    return j

def main(): 
    server()

if __name__ == "__main__":
    main()