import argparse
import socket
import pickle
import os
def main(host, port, filein, fileout):
    calcetin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    calcetin.connect((host, port))
    fichero = open(filein,'rt')
    tam = os.path.getsize(filein)
    calcetin.send(str(tam).encode('utf8'))
    texto = fichero.read(2048);
    calcetin.send(texto.encode('utf8'))
    fichero.close()
    buffer1 = calcetin.recv(tam)
    buffer2 = calcetin.recv(2048)
    print(buffer2.decode('utf8'))
    texto = pickle.loads(buffer1)
    fichero = open(fileout,'wt')
    print(texto)
    for i in range(0,len(texto)):
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
