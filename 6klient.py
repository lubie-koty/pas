import socket
import ssl

HOST = '127.0.0.1'
PORT = 1234
CERTIFICATE = 'moj_server.crt'


if __name__ == '__main__':
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.load_verify_locations('server.crt')
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        with ssl_context.wrap_socket(socket, server_hostname=HOST) as wrapped_socket:
            wrapped_socket.connect((HOST, PORT))
            while True:
                user_input = input('>')
                wrapped_socket.send(user_input.encode())
                response = wrapped_socket.recv(1024)
                print(f'server response: {response.decode()}')
