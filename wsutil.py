# python 2.7.x

import subprocess
import socket
import sys

cmd = "ipconfig"
cmdParam = " /displaydns"

while True:
	p = subprocess.Popen(cmd + cmdParam, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		line = line.strip()
		if "Record Name" in line and "usaa" in line:
			currentDomain = line.split(' ')[-1]
			print("Port scanning: " + currentDomain)
			for port in [23,21,25,3389,110,143,3306,1723,995,993,5900,587,8888,199,1720,465]:
				try:		
					print "Trying port: " + str(port)
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(1)
					s.connect((currentDomain, port))
				except: # socket.error, msg:
					#print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
					pass
