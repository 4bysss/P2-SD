import argparse
import socket
import random
import struct
from socket import AF_INET, SOCK_DGRAM
def main(host, port, n):
    below=0
    sc=socket.socket(AF_INET,SOCK_DGRAM)
    sc.sendto(str(n).encode("utf-8"),(host,port))

    for i in range(0,n):
        sc.sendto(struct.pack('ff',random.random(),random.random()),(host,port))
        word=sc.recvfrom(1024)[0]

        if (word.decode("utf_8")=="below"):
            below= below + 1
            print(below)

    pi=4*(below/n)
    print (pi)




if __name__ =='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--number', default=100000, help="number of random points to be generated")
    args=parser.parse_args()
    main(args.host, args.port, args.number)
