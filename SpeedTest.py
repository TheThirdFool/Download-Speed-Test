import speedtest

def test():
	s = speedtest.Speedtest()
	s.get_servers()
	s.get_best_server()
	s.download()
	s.upload()
	res = s.results.dict()
	return res["download"], res["upload"], res["ping"]

def Main():
	# write to csv
	d, u, p = test()

	#Convert to bytes
	db = 0.125 * d
	ub = 0.125 * u
	
	#Print to file
	f = open("SpeedTest.txt", 'a')
	f.write(str(db) + ", " + str(ub) + ", "+ str(p) + "\n")
	f.close()

Main()

