import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('google.com', 80))