import socket

HOST = '212.182.24.27'
PORT = 29443


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            user_input = input('>')
            s.send(user_input.encode())
            response = s.recv(1024)
            print(f'server response: {response.decode()}')
