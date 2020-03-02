"""
Alessia De Giovannini
4°A ROB
1) chiedere all'utente una lista di parole,
2) inserire in un'altra lista (l2) le parole più lunghe
3) stampare la lista (l2)
(usare il comando length)
"""

dim = input("quante parole vuoi? ")
max = 0
lista = []
l2 = []
for i in range(int(dim)): #CONVERSIONE di un tipo (più o meno come il casting)
    parola = input("inserisci una parola: ")
    lista.append(parola) #prende una stringa
print(lista)


for parola in lista:
    if (len(parola)>=max):
        max = len(parola)
        
#foreach (per ogni) scorrere la lista
for parola in lista:
    if (len(parola)>=max):
        l2.append(parola)

#scorrere la lista
for i in range(len(lista)):
    print(lista[i])

print(l2)
