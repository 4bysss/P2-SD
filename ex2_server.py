import argparse
import socket
import pickle
def main(host, port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen()
    sockt_c,c_addr=s.accept()
    fichero=sockt_c.recv(2048)
    texto=fichero.decode('utf-8')
    num=0
    cadenaC=[]
    word=texto.split()
    for i in range(0,len(word)):
        if "a" in word[i]:
            cadenaC.append(word[i])
            num = num + 1
            print (num)
            print (word[i])
    sockt_c.send(pickle.dumps(cadenaC))
    sockt_c.send(str(num).encode('utf-8'))
    sockt_c.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
