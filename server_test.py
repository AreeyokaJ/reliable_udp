import socket

HOST = "127.0.0.1"
PORT = 30077  # assigned port

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"[SERVER] Listening on {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"[SERVER] Received from {addr}: {data.decode()}")
    
    # Respond back to client
    response = "Message received".encode()
    sock.sendto(response, addr)