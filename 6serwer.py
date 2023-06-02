import socket
import ssl

HOST = '127.0.0.1'
PORT = 1234
CERTIFICATE = 'moj_server.crt'
PRIVATE_KEY = 'moj_server.key'


if __name__ == '__main__':
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile=CERTIFICATE, keyfile=PRIVATE_KEY)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            connection, address = s.accept()
            with ssl_context.wrap_socket(connection, server_side=True) as wrapped_connection:
                while True:
                    data = wrapped_connection.recv(1024)
                    if not data:
                        break
                    print(f'received data: {data.decode()}')
                    wrapped_connection.sendall(data)
