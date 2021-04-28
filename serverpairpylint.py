"""code for ZMQ Messaging pattern using PAIR- server
bind socket to client
send msg to client
recv msg from client
"""

import time
import zmq
PORT = "7777"
CONTEXT = zmq.Context()
SOCKET = CONTEXT.socket(zmq.PAIR)
SOCKET.bind("tcp://*:%s"%PORT)
while True:
    SOCKET.send("Hello from server")
    MSG = SOCKET.recv()
    print MSG
    time.sleep(1)
