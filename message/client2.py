import sys
import socket
import select

def attempt_connect (sock, host, port):
    try:
        sock.connect((host,port))
    except:
        print("Connection failure")
        sys.exit()

    print ("Connected")
    sys.stdout.write('[Me] '); sys.stdout.flush()


def running_state (sock):
    while True:
        socket_list = [sys.stdin, sock]

        ready_to_read,ready_to_write,in_error = select.select(socket_list, [], [])

        for socket in ready_to_read:
            if socket == sock:
                # incoming message from remote server, s
                data = socket.recv(4096)
                if not data :
                    print('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()

            else :
                # user entered a message
                msg = sys.stdin.readline()
                sock.send(msg.encode('utf-8'))
                sys.stdout.write('[Me] '); sys.stdout.flush()


def main ():

    host = sys.argv[1]
    port = int(sys.argv[2])
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.settimeout(2)

    attempt_connect(remote_socket,host,port)
    running_state(remote_socket)


if __name__ == "__main__":
    main()
    #sys.exit(chat_client())
