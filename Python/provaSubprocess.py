import subprocess #libreria che permette di lanciare processi di sistema
p = subprocess.Popen(['ping', '-c 2', '127.0.0.1'], stdout=subprocess.PIPE) #lancia il processo
ping = p.communicate() #eseguie il programma 
print(ping[0].decode()) #legge il programma 