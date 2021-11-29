import socket

target = input('Enter target ip: ')
port_range = input('Enter the port range: ')

# parse inputs
ports = port_range.split('-')

lower_bound = int(ports[0])
upper_bound = int(ports[1])

print('Initiating scan on target: ' + target)

output = []

for i in range(lower_bound, upper_bound):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = 'Port #' + str(i) + ' is '
    current = (target, i)
    # attempt to connect
    if not sock.connect_ex(current):
        output.append(result + 'OPEN\n')
    else:
        output.append('\t' + result + 'CLOSED\n')

    sock.close()

# report results
print(''.join(output))