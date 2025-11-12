# Marco Greco 40285114
# COEN 366 Lab 2 UDP Client
# Adapted from Lab Slides

import socket  # for sockets
import sys     # for exit
import threading
import os

def timeout(sock):
    print ("Server timed out")
    s.close()
    os._exit(0)

client_host = '0.0.0.0'
client_port = 8889

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

s.bind((client_host, client_port))

host = 'localhost'
port = 8888

while(1):
    msg = input('Enter message: ')

    try:
        s.sendto(msg.encode('utf-8'), (host, port))

        timer = threading.Timer(3, timeout, [s])
        timer.start()

        d = s.recvfrom(1024)
        timer.cancel()

        reply = d[0].decode('utf-8')
        addr = d[1]
        print('Server replied: ' + reply)

    except socket.error as e:
        print(f'Error' + {e})

s.close()
