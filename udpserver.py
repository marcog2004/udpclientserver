# Marco Greco 40285114
# COEN 366 Lab 2 UDP Server
# Adapted from Lab Slides

import socket
import sys
import time

HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 8888        # Arbitrary non-privileged port

# Create Socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET -> Specifies IPv4 Addresses // SOCK_DGRAM -> UDP
except socket.error as e:
    print(f'Failed to create socket: {e}') # In case of error creating socket
    sys.exit(1)

# Bind socket
try:
    s.bind((HOST, PORT)) # Assign specific local IP and port to socket
except socket.error as e:
    print(f'Bind failed: {e}') # In case of error binding socket
    sys.exit(1)

message_count = 0 # total received messages

# Listen for messages from client
print('UDP Server listening on port', PORT)  # indicate listening status of server
while True:
    try:
        data, addr = s.recvfrom(1024) # when data is received, store data and address + port it came from
        if not data:
            break
        
        message_count += 1 # increment total received messages

        if message_count % 3 == 0: # simulate timeout on every third message
            time.sleep(5) # delay to simulate timeout
        else:
            reply = b'OK...' + data # store reply (to be sent to client)
            s.sendto(reply, addr) #  send response to client
            print(f"Received from {addr}: {data.decode('utf-8').strip()}") # print received message and client IP + port

    except KeyboardInterrupt:
        print('\nServer shutting down...') # shut down server on keyboard interrupt
        break
    except Exception as e: 
        print(f'Error: {e}') # error handling
        break

s.close()
