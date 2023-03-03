import socket
import sys

ip_addr = sys.argv[1]

print(socket.gethostbyaddr(ip_addr)[0])