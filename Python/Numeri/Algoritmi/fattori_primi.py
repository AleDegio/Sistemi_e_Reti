"""
Alessia De Giovannini
Dato n trovare i suoi fattori primi 
"""

def fattoriPrimi(numero):
	d=2
	while numero != 1:
		if isPrimo(d) and (numero % d == 0):
			print(str(d) + " ")
			numero = numero / d
			d = 2
		else:
			d = d + 1
	
def isPrimo(numero):
	div = 2
	count =  0
	while div<=numero/2 and count==0:
		if numero%div == 0:
			count+=1
		
		div+=1

	if count==0:
		return True
	else:
		return False

def main():
	num = input("Inserisci il numero:")  
	fattoriPrimi(num)
	
if __name__ == "__main__":
	main()
