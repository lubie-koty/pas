import socket

def read_hex_number(iterable):
    return f'{int("".join(iterable), 16)}'

def read_hex_text(iterable):
    return ''.join(list(map(lambda x: chr(int(x, 16)), iterable)))

hex_packet = """
0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18
00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee
00 1a 4c ee 68 65 6c 6c 6f 20 3a 29
""".split()

src_port = read_hex_number(hex_packet[:2])
dest_port = read_hex_number(hex_packet[2:4])
data = read_hex_text(hex_packet[32:])
result = f'zad14odp;src;{src_port};dst;{dest_port};data;{data}'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('212.182.24.27', 2909))
    s.sendall(result.encode('utf-8'))
    received_data = s.recv(1024).decode('utf-8')

print(received_data)
