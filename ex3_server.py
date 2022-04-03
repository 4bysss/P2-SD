import argparse
import socket
from socket import AF_INET, SOCK_DGRAM
import numpy  as np
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
    matrix_p1=np.matrix(txt_bp1)
    print("Processed:")
    print(matrix_p1)
    lives_p1 = np.count_nonzero(matrix_p1)


    #Player 2 conection
    buffer,addr_p2 = s_s.recvfrom(1024)
    p2_name = buffer.decode('utf8')
    print("Player:",p2_name," has connected succcessfully!")
    buffer = s_s.recvfrom(1024)[0]
    txt_bp2 = buffer.decode('utf8')
    print("Board Player 2:")
    print(txt_bp2)
    print("Processed:")
    matrix_p2=np.matrix(txt_bp2)
    print(matrix_p2)
    lives_p2 = np.count_nonzero(matrix_p2)

    turns=1
    end=False
    c_player = addr_p1
    n_turn ="Turn "+str(turns)
    while(not end):
        s_s.sendto(n_turn.encode('utf-8'),c_player)
        buffer,c_player = s_s.recvfrom(1024)
        move = buffer.decode('utf8')
        x_axis = ord(move[0])-65
        if len(move)==2:
            y_axis = int(move[1])-1
        else:
            y_axis = 9
        if(c_player == addr_p1):
            if(matrix_p2[x_axis,y_axis] == 1):
                matrix_p2[x_axis,y_axis] = 0
                lives_p2 = lives_p2 -1
                if(lives_p2 == 0):
                    s_s.sendto("You win".encode('utf-8'),addr_p1)
                    s_s.sendto("You lost".encode('utf-8'),addr_p2)
                    end = True
                else:
                    s_s.sendto("Hit".encode('utf-8'),addr_p1)
                    n_p = addr_p1
            else:
                s_s.sendto("Fail".encode('utf-8'),addr_p1)
                n_p = addr_p2
        if(c_player == addr_p2):
            if(matrix_p1[x_axis,y_axis] == 1):
                matrix_p1[x_axis,y_axis] = 0
                lives_p1 = lives_p1 -1
                if(lives_p1 == 0):
                    s_s.sendto("You win".encode('utf-8'),addr_p2)
                    s_s.sendto("You lost".encode('utf-8'),addr_p1)
                    end = True
                else:
                    s_s.sendto("Hit".encode('utf-8'),addr_p2)
                    n_p = addr_p2
            else:
                s_s.sendto("Fail".encode('utf-8'),addr_p2)
                n_p = addr_p1
        turns = turns + 1
        n_turn ="Turn "+str(turns)
        c_player = n_p




    s_s.close()








if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
