"""
Alessia De Giovannini
4°A ROB
liste 
"""
def somma(a, b):
    return a + b

lista = [1, 'ciao', 3, somma(3, 4)]

#for che stampa gli elementi della lista
#scorri la lista e stampa l'elemento della lista (i)
#si cicla sull'elemento della lista (i)
for i in lista:
    print(i)

print(lista)

posizione = 1
print(lista[-1])    #stampa l'ultimo elemento della lista
print(lista[3:5])    #stampa da 3 a 5
print(lista[3:])    #stampa da 3 fino alla fine della lista
len(lista)   #ritorna un intero che dice qunato è lunga la lista (stampa la lung della lista)
