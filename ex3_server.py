import argparse
import socket
from socket import AF_INET, SOCK_DGRAM
def main(host, port):
    s_s=socket.socket(AF_INET,SOCK_DGRAM)
    s_s.bind((host,port))

    #Player 1 conection
    buffer,addr_p1 = s_s.recvfrom(1024)
    p1_name = buffer.decode('utf8')
    print("Player:",p1_name," has connected succcessfully!")
    buffer = s_s.recvfrom(1024)[0]
    txt_bp1 = buffer.decode('utf8')
    print("Board Player 1:")
    print(txt_bp1)
    i=j=0
    matrix_p1[0][0] = 0
    for lines in txt_bp1.split(';'):
        for numbers in lines.split(' '):
            matrix_p1[i][j] = int(numbers)
            j+1
        i+1
    print("Processed:")
    print(matrix_p1)



    #Player 2 conection
    buffer,addr_p2 = s_s.recvfrom(1024)
    p2_name = buffer.decode('utf8')
    print("Player:",p2_name," has connected succcessfully!")
    buffer = s_s.recvfrom(1024)[0]
    txt_bp2 = buffer.decode('utf8')
    print("Board Player 2:")
    print(txt_bp2)
    i=j=0
    matrix_p2[0][0] = 0
    for lines in txt_bp2.split(';'):
        for numbers in lines.split(' '):
            matrix_p2[i][j] = int(numbers)
            j+1
        i+1
    print("Processed:")
    print(matrix_p2)




    s_s.close()








if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
