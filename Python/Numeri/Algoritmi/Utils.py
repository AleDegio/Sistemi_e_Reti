"""
Utils
"""
#creo una variabile alfabeto 
#per associare ad ogni lettere un numero (A=0,...) 
#attraverso il metodo alfabeto.index("A") 
#(restiuisce 0 essendo A la prima lettera)
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#funzione inversa a fromStringToInt 
#dato un intero lo converte nel carattere corrispettivo 
#in base alla posizione nell'alfabeto
def fromIntToString(somma):
    parolaCifrata = []
    for i in range(0, len(somma)):
        parolaCifrata.append(alfabeto[somma[i]])
    
    return parolaCifrata

#converte la parola e la chiave 
#nel corrispettivo valore numero 
#in base all'alfabeto
def fromStringToInt(parola):
    parola = parola.upper()
    intParola = []

    #converto le lettere della parola in numeri A = 0 ecc.
    for i in range(0, len(parola)):
        intParola.append(alfabeto.index(parola[i])) #alfabeto.index restituisce l'index in cui è stato trovato il carattere 
    
    return intParola #vettori di interi

