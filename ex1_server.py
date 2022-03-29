import argparse
import socket
import math
import struct
from socket import AF_INET, SOCK_DGRAM
from math import sqrt

def main(host, port):
    ss=socket.socket(AF_INET, SOCK_DGRAM)
    ss.bind((host,port))
    n=ss.recvfrom(1024)[0]
    n=n.decode("utf-8")
    n=int(n)
    below=0
    for i in range(0,n):
        buffer,dir=ss.recvfrom(1024)
        coor=struct.unpack('ff',buffer)
        y=sqrt(1-(coor[0]**2))
        if y>coor[1]:
            ss.sendto("below".encode("utf_8"),dir)
            below+=1
            print(below)
        elif y<=coor[1]:
            ss.sendto("above".encode("utf-8"),dir)

        elif coor[0] or coor[1] not in range (0,1):
            ss.sendto("error".encode("utf-8"),dir)
    pi=4*(below/n)
    print (pi)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
