import socket
import sys

arg = sys.argv[1]
ip_addr = None

try:
    socket.inet_aton(arg)
    ip_addr = arg
except socket.error:
    try:
        ip_addr = socket.gethostbyname(arg)
    except:
        print('adres nieprawidlowy')
  
if ip_addr:  
    print(f'skanuje porty adresu: {ip_addr}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        for port_number in range(1, 65535):
            if s.connect_ex((ip_addr, port_number)) == 0:
                print(f'port {port_number} jest otwarty;{socket.getservbyport(port_number, "tcp")}')
            else:
                print(f'port {port_number} jest zamkniety')