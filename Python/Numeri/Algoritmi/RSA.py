"""
Alessia De Giovannini 
Algoritmo di RSA 
"""
from random import *
from n_primo import primo
from Euclide import euclide 

def main():
    n, c, m, d = generaChiave()
    frase = input("Inserisci la frase da cifrare: ")
    msgC = cripta(c, n, frase)
    print(msgC)
    s = decripta(msgC, d, n)
    print(s)


def generaChiave():
    #generazione pi e qu
    num = randint(1, 100)
    pi = primo(num)
    num = randint(1, 100)
    qu = primo(num)
    
    #trovare n 
    n = pi*qu 

    #trovare m
    m = int(((pi-1)*(qu-1))/euclide(pi-1, qu-1))
    
    #trovare c
    c=2
    while euclide(m, c) != 1:
        if c>m:
            break
        c=c+1
    
    #trovare d
    d=0
    while (c*d)%m != 1:
        if d>m:
            break
        d=d+1

    return n, c, m, d      

#prende le chiavi pubbliche 
#e cripta il messaggio 
def cripta(c, n, frase):
    vet = []
    #converte i simboli in ASCI e li mette nel vettore 
    for i in range(0, len(frase)):
        vet.append(ord(frase[i])) 
    mes_cifrato = ""

    #prende tutti gli interi corrispondenti ai caratteri 
    #e crea il messaggio cifrato 
    for i in range(0, len(vet)):
        if i == len(vet)-1:
            mes_cifrato = mes_cifrato + str(pow(vet[i], c)%n)
        else:
            #\n divide i caratteri 
            mes_cifrato = mes_cifrato + str(pow(vet[i], c)%n) + "\n" 
    return mes_cifrato
    
#prende d, n e il messaggio cifrato 
#e decripta il messaggio 
def decripta(msgC, d, n):
    i=0
    vet = msgC.split("\n") 

    #decifra gli interi ASCI contenuti in vet 
    for i in range(0, len(vet)):
        vet[i] = (pow(int(vet[i]), d)%n)
    
    #trasfoma i numeri ASCI in caratteri 
    s =""
    for i in range(0, len(vet)):
        s = s + chr(vet[i])
    
    return s

if __name__ == "__main__":
    main()