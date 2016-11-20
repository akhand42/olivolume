# modules used in this program
from Tkinter import *
import socket
import subprocess
import sys

# defining a global variable
message = " "

PORT = 4269 

def connectButton():
	HOST = clientIPAddress.get() # The remote host
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((HOST, PORT))
		s.send(message)
		s.close()
	except socket.timeout:
		pass
	return

def get_value(val):
	valueOS = float(val)
	global message
	message = str(valueOS)
	return

app = Tk()
app.geometry('500x300')
app.title('Olivolume - Control music remotely')

connectionStatus = StringVar()
userIPAddress = StringVar()
connectButtonText = StringVar()
clientIPAddress = StringVar()

heading = Label(app, text = 'OLIVOLUME', font = ('-weight bold', 44)).pack()
connected = Label(app, textvariable = connectionStatus, font = ('-weight bold', 16)).pack()
userIP = Label(app, textvariable = userIPAddress, font = ('-weight bold', 22)).pack()
clientIPLabel = Label(app, text = 'Enter friend\'s IP here', font = ('-weight bold', 22)).pack()

ipEntry = Entry(font = ('-weight bold', 22), textvariable = clientIPAddress).pack()

volumeSlider = Scale(app, from_= 0, to = 100, orient = HORIZONTAL, font = ('-weight bold', 22), length = 400, command = get_value).pack()

connect = Button(app, textvariable = connectButtonText, font = ('-weight bold', 22), command = connectButton).pack()
connectButtonText.set("SET VOLUME")

connectionStatus.set("CONTROL MUSIC")
userIPAddress.set("Your IP is: " + socket.gethostbyname(socket.gethostname()))

app.mainloop()