# Marco Greco 40285114
# COEN 366 Lab 2 UDP Client
# Adapted from Lab Slides

import socket  # for sockets
import sys     # for exit
import threading
import os

#Timer Thread function to handle server timeout
def timeout(sock):
    print ("Server timed out")
    s.close()
    os._exit(0)

# Client address and port
client_host = '0.0.0.0'
client_port = 8889

# Open socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
except socket.error:
    print('Failed to create socket') # In case of error creating socket
    sys.exit()

# Bind socket
try:
    s.bind((client_host, client_port)) # Assign specific local IP and port to socket
except socket.error as e:
    print(f'Bind failed: {e}') # In case of error binding socket
    sys.exit(1)

# Server address and port
host = 'localhost'
port = 8888

while(1):
    msg = input('Enter message: ') # message input by user

    try:
        s.sendto(msg.encode('utf-8'), (host, port)) # send message to server  (encode to transfer bytes to server, not string)

        timer = threading.Timer(3, timeout, [s]) # create timer thread to handle timeout
        timer.start() # start timer

        d = s.recvfrom(1024) # receive message back from server
        timer.cancel() # cancel timeout timer

        reply = d[0].decode('utf-8') # decode bytes to string

        print('Server replied: ' + reply) # display reply from server

    except socket.error as e: 
        print(f'Error' + {e}) # error handling

s.close()
