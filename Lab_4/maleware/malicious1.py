# malicious2.py
# Another harmless fake, but looks suspicious

import base64
import socket

def connect_and_decode():
    data = "U29tZVRleHQ="  # just a fake base64 string
    decoded = base64.b64decode(data)  # <--- flagged
    s = socket.socket()
    s.connect(("127.0.0.1", 8080))  # <--- flagged
    print(decoded)

connect_and_decode()
