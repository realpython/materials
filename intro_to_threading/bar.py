#!/usr/bin/env python3
import threading
import time

def server():
    print("starting server")
    time.sleep(0.1)
    print("server done sleeping")
    b.wait()
    print("released")
    b.reset()
    print("starting server")
    time.sleep(0.1)
    print("server done sleeping")
    b.wait()
    print("released")
    # while True:
        # connection = accept_connection()
        # process_server_connection(connection)

def client():
    print("starting client")
    time.sleep(1.0)
    print("client done sleeping")
    b.wait()
    print("released")
    print("starting client")
    time.sleep(1.0)
    print("client done sleeping")
    b.wait()
    print("released")
    # while True:
        # connection = make_connection()
        # process_client_connection(connection)



print("here I am")
b = threading.Barrier(2, timeout=5)
s = threading.Thread(target=server)
c = threading.Thread(target=client)
s.start()
c.start()
s.join()
c.join()
