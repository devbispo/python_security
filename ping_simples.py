import os

host_ip = input("Digite o IP ou HOST a ser verificado:  ") #Armazenamento do IP ou HOST.

os.system('ping -n 8 {}' .format(host_ip)) #PUSH DOS COMANDOS LIGADO AO SISTEMA 
