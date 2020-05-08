
import socket
from transmitJSON import sendJSON

serverHost = 'localhost'
serverPort = 3001

#Create a socket
s = socket.socket()

#Connect to server
s.connect(('127.0.0.1', 3001))

#Send messages
Inscription ={"matricules": ["17235"], "port": 8080, "name": "Mohamed"}

sendJSON(s,Inscription)
