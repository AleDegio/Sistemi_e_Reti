'''
Alessia De Giovannini
4°A ROB
Date 2 liste (l1 e l2), calcolare l'intersezione
(trova i valori uguale nelle due liste)
creare una terza lista che contenga solo le parole uguali in l1 e l2
(evitare di usare la lunghezza delle liste)
'''

lista1 = ['1', '5', '4', '9']
lista2 = ['7', '9', '5', '8']
lista3 = []

for i in lista1:
    if i in lista2:
        lista3.append(i)
print(lista3)
