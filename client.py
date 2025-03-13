import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'

address = '/tmp/udp_client_socket_file'

try:
    os.unlink(address)
except FileNotFoundError:
    pass

sock.bind(address)

try:
    message = input()
    message_binary = message.encode('UTF-8')
    
    print('sending {!r}'.format(message))
    sent = sock.sendto(message_binary, server_address)

    print('waiting to receive')

    data, server = sock.recvfrom(4096)

    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
