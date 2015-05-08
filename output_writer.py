#!/usr/bin/python

import serial

if __name__ == '__main__':
	#Set USB port
	usbport = 'dev/ttyAMA0'
	control = serial.Serial(usbport, '9600')
	#The final data will be stored here
	data_line = ""
	#WHILE this device is transmitting data...
	while True:
		data_flow = control.read()
		if (data_flow == "\r"):
			print "SENSOR RECEIVED:" + data_line
			data_line = ""
		else:
			data_line = data_line + data_flow
	#Attempts to write the output to output.txt
	with open("output.txt", "w") as output_file:
		output_file.write(data_line)
	#Checks if the file is closed (it should be)
	if output_file.closed == False:
		my_file.close()
	
