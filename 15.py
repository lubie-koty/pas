import socket

def read_hex_number(iterable):
    return f'{int("".join(iterable), 16)}'

def read_hex_ip(iterable):
    return f'{read_hex_number(iterable[0])}.{read_hex_number(iterable[1])}.{read_hex_number(iterable[2])}.{read_hex_number(iterable[3])}'

def read_hex_text(iterable):
    return ''.join(list(map(lambda x: chr(int(x, 16)), iterable)))

hex_packet = """
45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b
c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1
80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01
00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67
72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e
""".split()

protocol_version = int(hex_packet[0][0], 16)
protocol_type = int(hex_packet[9], 16)
src_ip = read_hex_ip(hex_packet[12:16])
dest_ip = read_hex_ip(hex_packet[16:20])

src_port = read_hex_number(hex_packet[20:22])
dest_port = read_hex_number(hex_packet[22:24])
if protocol_type == 6:
    data = read_hex_text(hex_packet[60:])
elif protocol_type == 17:
    data = read_hex_text(hex_packet[32:])
else:
    raise Exception('wrong protocol type')
    
resultA = f'zad15odpA;ver;{protocol_version};srcip;{src_ip};dstip;{dest_ip};type;{protocol_type}'
resultB = f'zad15odpB;srcport;{src_port};dstport;{dest_port};data;{data}'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('212.182.24.27', 2911))
    s.sendall(resultA.encode('utf-8'))
    received_data = s.recv(1024).decode('utf-8')
    print(received_data)
    if received_data == 'TAK':
        s.sendall(resultB.encode('utf-8'))
        received_data = s.recv(1024).decode('utf-8')
        print(received_data)
