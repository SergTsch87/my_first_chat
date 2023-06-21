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

# Прослуховуємо з'єднання
name = input('Enter name:')
new_socket.listen(1)

# Прийняття вхідних підключень
# Змінна conn підключається до сокета,
# а змінна 'add' призначається IP-адресі клієнта
conn, add = new_socket.accept()
print(f"Received connection from {add[0]}")
print(f"Connection established. Connected from: {add[0]}")