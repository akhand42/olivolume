import socket

HOST = socket.gethostbyname(socket.gethostname())    # The remote host
PORT = 45459           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((HOST, PORT))
	s.send('10')
	data = s.recv(1024)
	s.close()
	print 'Sent', repr(data)
except socket.timeout:
	print 'Disconnected'