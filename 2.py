import random
import socket

random_number = random.randint(1, 20)
is_number_not_found = True

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    while is_number_not_found:
        connection, address = s.accept()
        with connection:
            while True:
                print(f'nawiazano polaczenie: {address}')
                received_data = connection.recv(1024)
                if not received_data:
                    print('brak odebranych danych')
                    break
                
                try:
                    received_data = int(received_data.decode('utf-8'))
                except ValueError:
                    connection.sendall(b'ERROR')
                
                if received_data == random_number:
                    connection.sendall(b'odgadles liczbe!!!')
                    is_number_not_found = False
                    break
                elif received_data > random_number:
                    connection.sendall(b'wylosowana liczba jest mniejsza od tej przeslanej')
                else:
                    connection.sendall(b'wylosowana liczba jest wieksza od tej przeslanej')
