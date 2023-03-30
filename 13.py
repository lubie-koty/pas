import socket

def read_hex_number(iterable):
    return f'{int("".join(iterable), 16)}'

def read_hex_text(iterable):
    return ''.join(list(map(lambda x: chr(int(x, 16)), iterable)))

hex_packet = """
ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61
6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f
6e 20 69 73 20 66 75 6e
""".split()

src_port = read_hex_number(hex_packet[:2])
dest_port = read_hex_number(hex_packet[2:4])
data = read_hex_text(hex_packet[8:])
result = f'zad13odp;src;{src_port};dst;{dest_port};data;{data}'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('212.182.24.27', 2910))
    s.sendall(result.encode('utf-8'))
    received_data = s.recv(1024).decode('utf-8')

print(received_data)
