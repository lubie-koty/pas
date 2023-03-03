import socket
import sys

ip_addr = None
arg = sys.argv[1]

try:
    socket.inet_aton(arg)
    ip_addr = arg
except socket.error:
    try:
        ip_addr = socket.gethostbyname(arg)
    except:
        print('adres nieprawidlowy')
    print('adres nieprawidlowy')

if ip_addr:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex((ip_addr, 80)) == 0:
            print('udalo sie nawiazac polaczenie')
        else:
            print('nie udalo sie nawiazac polaczenia')
