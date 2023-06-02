import requests
import socket
import ssl

from typing import Optional

HOST = 'irc.freenode.net'
PORT = 7000
BOT_NAME = 'pogodynka'
BOT_CHANNEL = '#kanal_pogodynki'

CERTIFICATE = 'dac9024f54d8f6df94935fb1732638ca6ad77c13.pem'
API_KEY = 'd4af3e33095b8c43f1a6815954face64'


def get_weather_data(location: str) -> Optional[str]:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f'{weather}; {temperature}'
    else:
        return None


if __name__ == '__main__':
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.load_verify_locations(cafile=CERTIFICATE)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
        with ssl_context.wrap_socket(socket, server_hostname=HOST) as wrapped_socket:
            wrapped_socket.connect((HOST, PORT))
            wrapped_socket.send(f'USER {BOT_NAME} {BOT_NAME} {BOT_NAME} {BOT_NAME}\r\n'.encode())
            wrapped_socket.send(f'NICK {BOT_NAME}\r\n'.encode())
            wrapped_socket.send(f'JOIN {BOT_CHANNEL}\r\n'.encode())
            while True:
                data = wrapped_socket.recv(1024).decode()
                if 'PING' in data:
                    wrapped_socket.send(b'PONG\r\n')
                elif 'PRIVMSG' in data:
                    sender = data.split('!')[0][1:]
                    message = data.split(f'PRIVMSG {BOT_CHANNEL} :')[1].strip()
                    if message.startswith('!pogoda'):
                        location = message.split('!pogoda ')[1]
                        location_weather = get_weather_data(location)
                        response = f'Aktualna pogoda w {location}: {location_weather}'
                        wrapped_socket.send(f'PRIVMSG {BOT_CHANNEL} : {response}\r\n'.encode())
