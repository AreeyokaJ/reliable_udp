import socket

SERVER_ADDR = ("127.0.0.1", 30077)
MESSAGE = "Hello, UDP Server!".encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MESSAGE, SERVER_ADDR)
print(f"[CLIENT] Sent: {MESSAGE.decode()}")

data, addr = sock.recvfrom(1024)
print(f"[CLIENT] Received from {addr}: {data.decode()}")

sock.close()