import argparse
import socket
import pickle
def main(host, port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen()
    sockt_c,c_addr = s.accept()
    tam = sockt_c.recv(1024)#Recibimos el tamaño del fichero
    tam = int(tam.decode('utf-8'))#Decodificamos
    fichero = sockt_c.recv(tam)#Recibimos la cadena que contiene el texto del fichero 
    texto = fichero.decode('utf-8')
    num = 0
    cadenaC = []
    word=texto.split()
    for i in range(0,len(word)):#Filtramos las palabras que cumplan la condicion
        if "a" in word[i]:
            cadenaC.append(word[i])
            num = num + 1
            print (num)
            print (word[i])
    sockt_c.send(pickle.dumps(cadenaC))#Preparamos la lista pàra ser mandada
    sockt_c.send(str(num).encode('utf-8'))#Y se manda
    sockt_c.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
