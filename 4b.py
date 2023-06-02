import os.path
import socket
import ssl

HOST = '212.182.24.27'
PORT = 29443
SERVER_CERT = './certyfikat.pem'


if __name__ == '__main__':
    ssl_context = ssl.create_default_context()
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.check_hostname = True
   
    if os.path.exists(SERVER_CERT):
        ssl_context.load_verify_locations(SERVER_CERT)    
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        with ssl_context.wrap_socket(socket, server_hostname=HOST) as wrapped_socket:
            wrapped_socket.connect((HOST, PORT))
            while True:
                user_input = input('>')
                wrapped_socket.send(user_input.encode())
                response = wrapped_socket.recv(1024)
                print(f'server response: {response.decode()}')
