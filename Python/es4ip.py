"""
chiedere un ip di rete 
chidere una maschera
il programma deve calcolare tutti gli indirizzi ip
"""

def toBin(indirizzo):
    lista = indirizzo.split(".")
    binary = ""
    for i in range(0, len(lista)):
        x = bin(int(lista[i]))[2:]
        s = ""
        if len(x) < 8:
            for i in range(0, 8-len(x)):
                s = s + "0"
        x = s + x
        binary = binary + x
    return binary

def reteHost(binIpRete, binMask):
    rete = ""
    for i in range(0, 31):
        if binIpRete[i] == "1" and binMask[i] == "1":
            rete = rete + "1"
        else: 
            rete = rete + "0"
    return rete

def nSottoreti(binMask):
    cont = 0
    for i in range(0, 32):
        if binMask[i] == "0": 
            cont = cont + 1
    print(f"numero Subnetmask: {cont}")
    return cont

def toDec(ind):
    indDec = ""
    temp = ""
    for i in range(1, len(ind)+1):
        temp = temp + ind[i-1]
        if((i%8)==0):
            indDec = indDec + str(int(temp,2)) + "."
            temp= ""
        elif(i==31):
            indDec = indDec + str(int(temp,2))
            temp= ""
    
    return indDec

def calcoloSubnet(indRete, nHost, cont):
    host = indRete.split(".")
    for j in range(0, cont):
        print(f"{j} subnetmask:")
        print(f"l'indirizzo di rete e' {host}")
        for i in range(0, nHost):
            host[len(host) - 1] = int(host[len(host) - 1]) + 1
            print(f"indirizzo di host: {host}")
        host[len(host) - 1] = int(host[len(host) - 1]) + 1
        print(f"indirizzo di broadcast: {host}")
        host[len(host) - 1] = int(host[len(host) - 1]) + 1


#main
ipdirete = input("inserisci un ip: ")
binIpRete = toBin(ipdirete)


mask = input("inserisci un mask: ")
binMask = toBin(mask)

reteHost = reteHost(binIpRete, binMask)
print(f"rete Host: {reteHost}")

cont = nSottoreti(binMask) 
nHost = pow(2, cont) - 2
print(f"numero di Host: {nHost}")

binReteHost = toDec(reteHost) #int(num, 2)
print(f"numero di rete binario: {binReteHost}")

calcoloSubnet(ipdirete, nHost, cont)

"""
Ip = input("inserisci l'ind...").split(".")
int dell'elemento di tutte le liste (list comprension)
Int_ip = [int(i) for i in Ip]
"""