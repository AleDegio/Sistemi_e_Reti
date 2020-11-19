"""
Alessia De Giovannini 
Euclide  
"""

def main():
    a = int(input("Inserisci il primo numero: "))
    b  = int(input("Inserisci il secondo numero: "))
    print(euclide(a, b))

def euclide(a, b):
    if a>b:
        max = a
        min = b
    else:
        max = b
        min = a
    resto = max%min
    while resto != 0:
        max = min 
        min = resto
        resto = max%min
    return min

if __name__ == "__main__":
    main()