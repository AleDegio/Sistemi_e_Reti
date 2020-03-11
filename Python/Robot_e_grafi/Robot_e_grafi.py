"""
Alessia De Giovannini
4°A ROB 
Robot e grafi 
"""
def toDizionario(matr):
    diz = {}
    for i in range(0, len(matr)):
        vet = []
        for j in range(0, len(matr)):
            vet.append(matr[i][j])
        diz['nodo '+ str(i+1)] = vet
    return diz

def main():
    #creazione del pavimento 
    pavi = []
    dim = input("Inserisci la dimensione del pavimento: ")
    dimM = 0
    for i in range(0, int(dim)):
        riga = []
        for j in range(0, int(dim)):
            riga.append(True)
        pavi.append(riga)
    interruz = False
    while interruz == False:
        ostacolo = input("Inserisci le cordinate della cella dove si trova l'ostacolo (inserisci -1 per terminare): ")
        if ostacolo != "-1":
            cordinate = ostacolo.split(".")
            i = int(cordinate[0])
            j = int(cordinate[1])
            pavi[i][j] = False
            dimM = dimM + 1
        else: 
            interruz = True
    print(pavi)

    dimM = int(dim) * int(dim) - dimM
    m = []
    for i in range(0, dimM): 
        vet = []
        for j in range(0, dimM):
            vet.append(0)
        m.append(vet)

    m2 = []
    cont = 0
    for i in range(0, int(dim)):
        vet = []
        for j in range(0, int(dim)):
            if pavi[i][j] == True:
                vet.append(cont)
                cont = cont + 1
            else: 
                vet.append(-1)
        m2.append(vet)
    print(m2)

    for i in range(0, int(dim)):
        for j in range(0, int(dim)):
            if m2[i][j] != -1:
                i2 = m2[i][j]
                if j+1 < int(dim):
                    if m2[i][j+1] != -1:
                        j2 = m2[i][j+1]
                        m[i2][j2] = 1
                        m[j2][i2] = 1
                if i+1 < int(dim):
                    if m2[i+1][j] != -1: 
                        j2 = m2[i+1][j]
                        m[i2][j2] = 1
                        m[j2][i2] = 1 
    print(m)
    diz = toDizionario(m)

if __name__ == "__main__":
    main()