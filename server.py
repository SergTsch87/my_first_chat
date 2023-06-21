import socket
import sys
import time

# Створимо сокет та отримаємо ім'я хосту
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

# Зв’яжемо разом порт і хост
new_socket.bind((host_name, port))
print("Binding successfull!")
print(f"This is your IP: {s_ip}")
