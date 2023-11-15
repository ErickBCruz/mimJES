import socket

# Configuración del cliente
host = '192.168.223.16'  # Cambia por la dirección IP del servidor
port = 5555  # Puerto de comunicación

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Conexión establecida con el servidor")

while True:
    # Enviar mensaje al servidor
    message = input("Escribe tu mensaje: ")
    client_socket.send(message.encode())

    # Recibir mensaje del servidor
    data = client_socket.recv(1024).decode()
    print(f"Servidor: {data}")
