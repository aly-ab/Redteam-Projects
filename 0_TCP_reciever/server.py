import socket

server_socket = ('127.0.0.1', 2000)
print('Server listening for connections on {0} port {1}'.format(server_socket[0],
    server_socket[1]))

# create a TCP/IP socket and bind it
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket)

# start listening for incoming connections
server.listen()

# wait for a connection
print('Waiting for a connection...')
connection, client_addr = server.accept()
print('Connection established with {0}'.format(client_addr))

# connection established, begin echoing stuff
while True:
    recieved = connection.recv(1024)
    if recieved:
        print('recieved: ' + recieved.decode('ascii'))
        if recieved.decode('ascii') == 'q':
            print('Waiting for a connection...')
            server.listen()
            connection, client_addr = server.accept()
            print('Connection established with {0}'.format(client_addr))

print('Closing server.')
