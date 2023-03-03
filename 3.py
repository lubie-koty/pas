import socket

ip_addr = input()

try:
    socket.inet_aton(ip_addr)
    print('adres prawidlowy')
except socket.error:
    print('adres nieprawidlowy')