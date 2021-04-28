""" code for zmq msg pattern using PAIR-client
connect to the port
Recieve msg from server
expect reply to server
"""
import time
import zmq
PORT = "7777"
CONTEXT = zmq.Context()
SOCKET = CONTEXT.socket(zmq.PAIR)
SOCKET.connect("tcp://localhost:%s"%PORT)
while True:
    MSG = SOCKET.recv()
    print MSG
    SOCKET.send("hi from the client")
    time.sleep(1)
