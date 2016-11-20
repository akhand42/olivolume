import socket
import subprocess

HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces
PORT = 4269            # Arbitrary non-privileged port
p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
p.bind((HOST, PORT))
while(1):
	p.listen(1)
	conn, addr = p.accept()
	# print 'Connected by', addr[0]
	for i in range(1):
		data = conn.recv(1024)
		subprocess.Popen('osascript -e "set volume output volume "' + data, shell=True)
		conn.close()