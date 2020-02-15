'''
funzioni push, pop e strutture
'''
import random

#funzione = contenitore = wrapper
#push
def push(stack, element):
    stack.append(element)
    return stack

#pop
def pop(stack):
    element = stack.pop()
    return stack, element

#prova
'''
pila = [1,2,3,"ciao"]
pila = push (pila, 5)
print(pila)
pila, _ = pop(pila) # => pila, element = pop(pila)
print(pila)
'''

#classe
class Carta(object):
    #__ (doppio underscore) => laziness
    def __init__(self, seme, numero): #self = se stesso
        self.seme = seme
        self.numero = numero
    def stampa(self):
        print(f"la carta ha seme {self.seme} di numero {self.numero}")

#c = Carta("C", 5)
#c.stampa()

Mazzo = []
Semi = ["C", "P", "D", "F",]
m2 = []
m3 = []
for i in range(1,14):
    for s in Semi:
        push(Mazzo,Carta(s,i))


for i in Mazzo:
    i.stampa()

def coppa()
    print(random.randint(0,52))

def stampa(self):
        print(f"la carta ha seme {self.seme} di numero {self.numero}")