# Desenvolvimento de um Cliente TCP
# O Algoritmo verificará se dados são enviados de maneira Íntegra
import socket #importação da biblioteca 
import sys 

def main ():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão FALHOU ")
    print("Erro {}" .format(e))
    sys.exit()
print("Socket Criado com sucesso")

hostalvo = input('Digite o HOST ou IP a ser conectado : ')
portalvo = input('Digite a porta a ser conectada : ')

try: 
    s.connect((hostalvo, int(portalvo)))
    print("Cliente TCP conectado com sucesso no host: " + hostalvo + "e na Porta: " + portalvo)
    s.shutdown(2)
except socket.error as e:
    print("A conexão falhou ")
    print('Error : {}' .format(e))  
    sys.exit()
        
if __name__ == "__main__":
    main()    
