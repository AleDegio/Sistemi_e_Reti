"""
Alessia De Giovannini
Dato n trovare l'n-esimo numero primo 
"""

def primo(numero):
    j = 0
    k = 0 
    i = 2
    while k < numero: 
        div = 2
        count = 0
        while div<=i/2 and count==0:
            if i%div==0:
                count+=1
            div+=1
        if count==0:
            j = i
            k = k + 1
        
        i = i + 1
    #print("il "+ str(numero) + "° numero primo" + " e':" + str(j))
    return j

def main():
    num = int(input("Inserisci un numero: "))
    primo(num)

if __name__ == "__main__":
    main()