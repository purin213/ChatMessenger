import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_add = '/udp_socket_file'
client_add = '/udp_client_socket_file'
message = b'Message to send to client.'

try:
    os.unlink(client_add)
except FileNotFoundError:
    pass

sock.bind(client_add)

try:
    print('sending{!r}'.format(message))
    sent = sock.sendto(message, server_add)
    print('waiting to recieve')
    data, server = sock.recvfrom(4096)
    print('recieved {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()
