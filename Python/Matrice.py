"""
chiedere all'utente il numero di nodi 
per ogni nodo chiedre i vicini di ogni nodo
stampare la lista di adiacenza 
"""

def toDizionario(matr):
    diz = {}
    for i in range(0, len(matr)):
        vet = []
        for j in range(0, len(matr)):
            vet.append(matr[i][j])
        diz['nodo '+ str(i+1)] = vet
    return diz

def nonOrientatoNonPesato(m):
    for i in range(0, len(m)):
        vicini = input(f"Inserire i vicini del nodo {i}: ").split(".")
        for j in vicini:            
            m[i][int(j)] = 1
    print(m)
    #print(toDizionario(m))

def nonOrientatoPesato(m):
    for i in range(0, len(m)):
        vicini = input(f"Inserire i vicini del nodo {i}: ").split(".")
        k = 1
        j = 0
        vic = []
        pesi = []
        for s in range(0,int(len(vicini)/2)):
            vic.append(vicini[j])
            j = j + 2
        for s in range(0,int(len(vicini)/2)):
            pesi.append(vicini[k])
            k = k + 2

        for s in range(0, int(len(vicini)/2)):           
            m[i][int(vic[s])] = int(pesi[s])
            j = j + 2
            k = k + 2
        """
        for s in range(0, int(len(vicini)/2)):           
            m[i][int(vicini[j])] = int(vicini[k])
            j = j + 2
            k = k + 2
        """

def orientatoNonPesato(m):
    for i in range(0, len(m)):
        vicini = input(f"Inserire il nodo puntato dal nodo {i}: ").split(".")
        for j in vicini:            
            m[i][int(j)] = 1
    print(m)

def orientatoPesato(m):
    for i in range(0, len(m)):
        vicini = input(f"Inserire il nodo puntato dal nodo {i}: ").split(".")
        k = 1
        j = 0
        vic = []
        pesi = []
        for s in range(0,int(len(vicini)/2)):
            vic.append(vicini[j])
            j = j + 2
        for s in range(0,int(len(vicini)/2)):
            pesi.append(vicini[k])
            k = k + 2

        for s in range(0, int(len(vicini)/2)):           
            m[i][int(vic[s])] = int(pesi[s])
            j = j + 2
            k = k + 2
        """
        for s in range(0, int(len(vicini)/2)):           
            m[i][int(vicini[j])] = int(vicini[k])
            j = j + 2
            k = k + 2
        """
    print(m)

def menu(scelta, m):
    if scelta == 1:
        orientatoNonPesato(m)
    elif scelta == 2: 
        nonOrientatoNonPesato(m)
    elif scelta == 3: 
        nonOrientatoPesato(m)
    elif scelta == 4: 
        orientatoPesato(m)



def main(): 
    nNodi = input("Quanti nodi ci sono? ")
    m = []

    for i in range(0, int(nNodi)):
        vet = []
        for j in range(0, int(nNodi)):
            vet.append(0)
        m.append(vet)
    diz = toDizionario(m)
    #print(diz['nodo 2']) #stampa solo il nodo 2
    
    print("1: Orientato NON Pesato \n 2: NON Orientato NON Pesato \n 3: NON Orientato Pesato \n 4: Orientato Pesato")
    scelta = input("Che grafo vuoi? ")
    menu(int(scelta), m)


    

if __name__ == "__main__":
    main()