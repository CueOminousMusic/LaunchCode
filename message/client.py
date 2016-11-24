import sys
import socket
import select

#split the connection setup into a function
def attempt_connect (sock, host, port):
    try:
        sock.connect((host,port))
    except:
        print("Connection failure")
        sys.exit()

    print ("Connected")
    sys.stdout.write('[Me] '); sys.stdout.flush()


#the loop to run once connected to send/recieve communication
def running_state (sock):
    while True:
        socket_list = [sys.stdin, sock]

        ready_to_read,ready_to_write,in_error = select.select(socket_list, [], [])

        for socket in ready_to_read:
            if socket == sock:
                # incoming message from remote server, s
                data = socket.recv(4096)
                if not data.decode() :
                    print('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print(data.decode())
                    sys.stdout.write(data.decode())
                    sys.stdout.write('[Me] '); sys.stdout.flush()

            else :
                # user entered a message
                msg = sys.stdin.readline()
                sock.send(msg.encode('utf-8'))
                sys.stdout.write('[Me] '); sys.stdout.flush()
    time.sleep(0.2)


def main ():
    #get arguments from the command line
    host = sys.argv[1]
    port = int(sys.argv[2])

    #set up a socket. AF_INET = IPV4, SOCK_STREAM = TCP
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.settimeout(2)

    #try to connect. will exit program if fails.
    #To do: fix this so it returns state rather than exiting (side effect)
    attempt_connect(remote_socket,host,port)

    #If we made it this far, connection was successful.  Enter the comms loop.
    running_state(remote_socket)


if __name__ == "__main__":
    main()
    #sys.exit(chat_client())
