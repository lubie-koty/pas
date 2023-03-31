import socket
import re

IP = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((IP, PORT))