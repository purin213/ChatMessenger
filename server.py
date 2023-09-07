import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_add = '/udp_socket_file'

try:
    os.unlink(server_add)
except FileNotFoundError:
    pass

fake = Faker()
print('Hi, I\'m {}. starting on {}'.format(fake.name(), server_add))

sock.bind(server_add)

while True:
    print('\nWaiting message')
    data, address = sock.recvfrom(4096)
    print('recieved {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes to {}'.format(sent, address))
