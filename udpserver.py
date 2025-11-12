import socket
import sys

HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 8888        # Arbitrary non-privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as e:
    print(f'Failed to create socket: {e}')
    sys.exit(1)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    print(f'Bind failed: {e}')
    sys.exit(1)

print('UDP Server listening on port', PORT)
while True:
    try:
        data, addr = s.recvfrom(1024)
        if not data:
            break

        reply = b'OK...' + data
        s.sendto(reply, addr)
        print(f"Received from {addr}: {data.decode().strip()}")

    except KeyboardInterrupt:
        print('\nServer shutting down...')
        break
    except Exception as msg:
        print(f'Error: {msg}')
        break

s.close()
