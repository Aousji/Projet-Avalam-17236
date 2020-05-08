
import socket
from transmitJSON import sendJSON

serverHost = 'localhost'
serverPort = 3001

#Create a socket
s = socket.socket()

#Connect to server
s.connect(('127.0.0.1', 3001))

#Send messages
Inscription ={"matricules": ["17236"], "port": 9090, "name": "AOUSJI Med Amine"}

sendJSON(s,Inscription)
