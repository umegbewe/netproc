import psutil
import time
while True:
	time.sleep(1)
	using_network=psutil.net_connections(kind='tcp')
	rows=using_network[0:len(using_network)-1]
	for i in range(0, len(rows)):
		sconn=rows[i][6]
		p = psutil.Process(sconn)
		print ("Network most consuming process is: ",p.name())
