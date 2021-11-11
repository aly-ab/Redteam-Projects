import socket

# create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
server_addr = ('127.0.0.1', 2000)
client.connect(server_addr)

# start sending data
while True:
    message = input('enter message: ')
    print('Sending message...\n')
    client.sendall(bytes(message, 'ascii'))
    if message == 'q':
        break

client.close()
print('Closing client.')
