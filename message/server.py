import sys
import socket
import select
import time


def chat_server():
    host = ''
    port = 5555
    socket_list = []
    recieve_buffer = 4096

    # IPV4 Address/hostname, TCP connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Where to listen
    server_socket.bind((host, port))
    # Listen, with a backlog of n connections
    server_socket.listen(10)

    # add server socket object to the list of readable connections
    socket_list.append(server_socket)

    print("Chat server started on port " + str(port))


    # server loop
    while True:
        # don't use 100% of CPU...
        time.sleep(0.1)

        #
        ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)

        # loop over sockets with stuff
        for sock in ready_to_read:
            # if server_socket has stuff, it's a new connection request
            if sock == server_socket:
                # accept the connection
                sockfd, addr = server_socket.accept()
                # drop the new client socket into the list to be iterated over
                socket_list.append(sockfd)
                print(socket_list)
                print("Client (%s, %s) connected" % addr)

                # tell the others
                broadcast(socket_list, server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)

            # the rest of the sockets are clients that have been added.
            # if one has stuff, it's a message from a client
            else:
                # process data recieved from client,
                try:
                    # receiving data from the socket.
                    data = sock.recv(recieve_buffer)
                    # Have to decode data, since the client encoded to send thru the socket
                    # This if checks that the data isn't 0, i.e. the socket is still connected
                    if data.decode():
                        # there is something in the socket, so send it.
                        broadcast(socket_list, server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data.decode())
                    #else:
                        # socket returned 0, which probably means it's broken
                        #if sock in socket_list:
                            #socket_list.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        #broadcast(socket_list, server_socket, sock, "Client (%s, %s) is offline\n" % addr)

                # exception
                except:
                    broadcast(socket_list, server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()



# broadcast chat messages to all connected clients
def broadcast (socket_list, server_socket, sock, message):
    print(message)
    for socket in socket_list:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message.encode())
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in socket_list:
                    socket_list.remove(socket)

if __name__ == "__main__":

    sys.exit(chat_server())
