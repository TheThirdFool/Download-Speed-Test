
import csv 
import matplotlib.pyplot as plt
import numpy as np

def GetData(No_Days):
	time = []
	down = []
	up = []
	ping = []
    
	with open('SpeedTest.txt') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			down.append(float(row[0]) * 1e-5)
			up.append(float(row[1])   * 1e-5)
			ping.append(float(row[2]))
			time_var = float(row[3])
			if((time_var % 1 - 0.3)**2 < 0.05**2):
				time_var = time_var + 0.2
			if(time_var == 0.0):
				No_Days = No_Days + 1
			time.append(time_var)
 
	return time, down, up, ping, No_Days

def CleanData(time, down, up, ping):
	clean_t = []
	clean_d = []
	clean_u = []
	clean_p = []

	i = 0
	while i < len(time):
		ghoul = True
		var_t = time[i]
		j = 0
		while j < len(clean_t):
			if var_t == clean_t[j]:
				clean_d[j] = 0.5 * (clean_d[j] + down[i])
				clean_u[j] = 0.5 * (clean_u[j] + up[i])
				clean_p[j] = 0.5 * (clean_p[j] + ping[i])
				ghoul = False
			j = j + 1
	
		if(ghoul):
			clean_t.append(time[i])	
			clean_d.append(down[i])	
			clean_u.append(up[i])	
			clean_p.append(ping[i])	
		i = i +1

	return clean_t, clean_d, clean_u, clean_p

def GetAverage(down):
	d_av = []

	total = 0
	for i in down:
		total = total + i

	d_av.append(total / len(down))
	d_av.append(total / len(down))

	return d_av

def PlotData(time, down, up, ping, Av_Down, Av_Up, Av_Ping):
	plt.rcParams['font.serif'] = "Times New Roman"
	plt.rcParams['font.family'] = "serif"

	plt.xlabel("Time [hrs]")
	plt.xticks(np.arange(0, 24, step=1))
	plt.ylabel("Speed [Mb/s]")
	plt.ylim(0,100)

	plt.plot([0,23.5], Av_Ping, color="hotpink", linestyle="--", alpha=0.5 ,label=f"Average Ping = {Av_Ping[0]:.1f}")
	plt.plot(time, ping, label="Ping", color="hotpink")

	plt.plot([0,23.5], Av_Up, color="blue", linestyle="--", alpha=0.5 ,label=f"Average Upload = {Av_Up[0]:.1f}")
	plt.plot(time, up, label="Upload", color="blue")

	plt.plot([0,23.5], Av_Down, color="red", linestyle="--", alpha=0.5 ,label=f"Average Download = {Av_Down[0]:.1f}")
	plt.plot(time, down, label="Download", color="red")

	#plt.gcf().autofmt_xdate()

	plt.legend(loc="center")

	plt.show()

def Main():
	
	time = []
	down = []
	up = []
	ping = []

	No_Days = 0

	time, down, up, ping, No_Days = GetData(No_Days)

	print("")
	print("There were ", (0.5 * len(time)), " hours averaged, taken across ", No_Days, " days.")
	print("")

	time, down, up, ping = CleanData(time, down, up, ping)
	Av_Down = GetAverage(down)
	Av_Up = GetAverage(up)
	Av_Ping = GetAverage(ping)

	PlotData(time, down, up, ping, Av_Down, Av_Up, Av_Ping)


Main()
