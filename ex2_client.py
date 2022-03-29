import argparse
import socket
def main(host, port, filein, fileout):
    calcetin=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    calcetin.connect((host, port))
    fichero= open(filein,'rt')
    texto=fichero.read(2048);
    calcetin.send(texto.encode('utf8'))
    fichero.close()
    buffer1=calcetin.recv(2048)
    buffer2=calcetin.recv(2048)
    print(buffer2.decode('utf8'))
    texto=buffer1.decode('utf8')
    fichero= open(fileout,'wt')
    print(texto)
    word=texto.split()
    for i in range(0,len(word)):
        fichero.write(word[i])
        fichero.write('\n')
        print(word)
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
