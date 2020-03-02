"""
Alessia De Giovannini
4°A ROB
"""
import subprocess #libreria che permette di lanciare processi di sistema
#p = subprocess.Popen(['ping', '-c 2', '127.0.0.1'], stdout=subprocess.PIPE) #lancia il processo
#ping = p.communicate() #eseguie il programma 
#print(ping[0].decode()) #legge il programma 


ipaddress = "192.160.10.0"
mask = 30

ipaddress_splitted = [int(i) for i in ipaddress.split(".")]  #[contiene tot numeri interi]

ipaddress_bin = 0
for e, group in enumerate(ipaddress_splitted):  #enumerate serve per ciclare su entrambi 
    ipaddress_bin = ipaddress_bin + group*(2**(((3-e)*8)))

ipaddress_host = ipaddress_bin
for c in range(1,2**(32-mask)-1):
    ipaddress_host = ipaddress_host + 1

    #rimette tutto in un formato leggibile
    l = '.'.join([str(int(bin(ipaddress_host)[i:i+8],2)) for i in range(2,34,8)]) #for = da 2 a 34 saltando di 8 in 8 
    print(l)

    p = subprocess.Popen(['ping', l], stdout=subprocess.PIPE) #lancia il processo
    ping = p.communicate() #eseguie il programma 
    #print(f"numero di occorrenze: {ping[0].decode().count('tempo approssimativo')}")
    if (ping[0].decode().count('tempo approssimativo') > 0):
        print(f"l'host {l} e' attivo")
    else: 
        print(f"l'host {l} e' inattivo")



"""
join() 
metodo di python utilizzato su stringhe e caratteri 
unisce i vari elementi della lista 
visualizzandoli con il carattere passato
esempio:
l = ["192"."168"."10"."1"]
"c".join(l)
"""