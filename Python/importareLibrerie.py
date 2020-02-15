'''
importare una libreria
'''

#per importare le LIBRERIE
import random
#oppure
import random as rnd

nomeLista = ['Mario Rossi', 'Jhon Doe', 'Tizio Caio']

print(f"Viene interrogato: {nomeLista[random.randint(0, len(nomeLista)-1)]}")
print(f"Viene interrogato: {nomeLista[rnd.randint(0, len(nomeLista)-1)]}")

#si cicla su due variabili (num e studenti) separate da virgole
#cicli sia sull'ELEMENTO che sulla POSIZIONE
for num, studenti in enumerate(nomeLista):
    print(f"{num}-{studenti}")
