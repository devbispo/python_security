import os #Importanto a Biblioteca
import time #Importanto a Biblioteca

with open('host.txt') as file:  #posicionando arquivo txt
    dump = file.read() #Leitura dos arquivo txt
    dump = dump.splitlines() #Seaparando as linhas de cada host ou ip 



for ip in dump: #Para cada ID ou Host 
   print('*' *60)
   print('Verificando ip:' , ip)
   print('*' *60)
   os.system ('ping -n 2 {}' .format(ip)) #PUSH DOS COMANDOS LIGADO AO SISTEMA
   print('*' *60)
   time.sleep(5) #Tempo de espera para cada leitura de IP ou HOST

