#####test#####
import socket,sys
from pathlib import Path

try:
	fqdn = sys.argv[1]
except:
	fqdn = None
if fqdn is None:
	print(3)
	sys.exit() 

file_path='/data/python_script/'

try:
	#####Read last check FQDN IP#####
	my_file = Path(file_path + "ipCheck.txt")
	if my_file.is_file():
		text_file = open(file_path +'ipCheck.txt','r')
		dt = text_file.readline()
		text_file.close
		#print(dt)
	else:
		dt = '0.0.0.0'
		#print(dt)

	#####Check FQDN's IP#####
	#fqdn="api.hec99.com"
	ip_list = []
	ais = socket.getaddrinfo(fqdn,0,0,0,0)
	for result in ais:
		ip_list.append(result[-1][0])
	ip_list = list(set(ip_list))
	#print(ip_list[0])

	#####Responce to Zabbix alert#####
	if ip_list[0] == dt:
		print(0) #target FQDN IP is not change
	else:
		print(1) #target FQDN IP is change 

	#####Write IP in txt file#####	
	text_file=open(file_path + 'ipCheck.txt','w')
	text_file.write(ip_list[0])
	text_file.close
except OSError as err:
	print(2) #python script error
	text_file=open(file_path + 'error.log','w')
	text_file.write("OS error: {0}".format(err))
	text_file.close
except ValueError:
	print(2) #python script error
	text_file=open(file_path + 'error.log','w')
	text_file.write("Could not convert data to an integer.")
	text_file.close
except:
	print(2) #python script error
	text_file=open(file_path + 'error.log','w')
	text_file.write("Unexpected error:", sys.exc_info()[0])
	text_file.close


 

