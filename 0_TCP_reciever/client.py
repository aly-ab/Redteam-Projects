import socket

# create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
server_addr = ('localhost', 1000)
client.connect(server_addr)

# start sending data
while True:
    message = input('enter message: ')
    print('Sending message...\n')
    client.sendall(message)