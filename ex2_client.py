import argparse
import socket
import pickle
import os
def main(host, port, filein, fileout):
    calcetin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    calcetin.connect((host, port))
    fichero = open(filein,'rt')#Abrimos el archivo
    tam = os.path.getsize(filein)#Calculamos el tamaño del archivo
    calcetin.send(str(tam).encode('utf8'))#Se lo mandamos al servidor para comunicarle el tamaño del fichero
    texto = fichero.read(2048);#SAlmacenamos el contenido del fichero en una cadena
    calcetin.send(texto.encode('utf8'))#Mandamos la cadena
    fichero.close()#Cerramos el fichero puesto que no se usara mas
    buffer1 = calcetin.recv(tam)#Se recibe la lista de palabras filtradas
    buffer2 = calcetin.recv(2048)#Se recibe el numero de palabras que cumplen la condicion
    print(buffer2.decode('utf8'))#Decodificamos el numero antes obtenido 
    texto = pickle.loads(buffer1)#Cargamos la lista de palabras
    fichero = open(fileout,'wt')
    print(texto)
    for i in range(0,len(texto)):#Almacenamos la lista en un fichero
        fichero.write(texto[i])
        fichero.write('\n')
    fichero.close()
    calcetin.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--filein', default='filein.txt', help="file to be read")
    parser.add_argument('--fileout', default='fileout.txt', help="file to be written")
    args = parser.parse_args()

    main(args.host, args.port, args.filein, args.fileout)
