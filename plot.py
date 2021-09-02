import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import os
import math

#helper functions
def step_info(t,yout,name):
    print (f"{name} OS: %f%s"%((max(yout)/yout[-1]-1)*100,'%'))
    print (f"{name} Tr: %fs"%(t[next(i for i in range(0,len(yout)-1) if yout[i]>yout[-1]*.90)]-t[0]))
    print (f"{name} Ts: %fs"%(t[next(len(yout)-i for i in range(2,len(yout)-1) if abs(yout[-i]/yout[-1])>1.02)]-t[0]))

def sens(inpt,output,name,unit = "not mentioned"):
	sensitivity = 0
	avgcount = 0
	for i in range(0,len(inpt)-2):
		if (inpt[i+1]-inpt[i]) > 0:
	 		sensitivity+=(output[i+1]-output[i])/(inpt[i+1]-inpt[i])
	 		avgcount+=1
	sensitivity = sensitivity / avgcount
	print(f"K of {name}:{sensitivity} {unit}")

def gain(inpt,output,name):
	gain = 0
	avgcount = -1
	for i in range(1,len(inpt)-1):
		if (inpt[i+1]-inpt[i]) > 0:
	 		gain+=output[i]/inpt[i]
	 		avgcount+=1	
	gain = gain / avgcount
	print(f"Am of {name}:{gain}")

def dampingratio(yout,name):
	overshoot = ((max(yout)/yout[-1]-1)*100)
	damp = math.sqrt(pow((math.log(overshoot/100)),2)/(pow(math.pi,2)+pow((math.log(overshoot/100)),2)))
	print(f"{name} damping ratio : {damp}")

def peaktime(t,yout,name,unit):
	max_value = max(yout)
	max_index = yout.index(max_value)
	print(f"{name} peak time : {t[max_index]} {unit}")

def steadystateerror(yout,name):
	ess=0
	for i in  range(190 ,200) :
		ess+= (yout[i]-60)
	ess = ess/10
	print(f"{name} Ess : {ess}")

def timeconstant(t,out,name):
	con = out[-1]*0.66
	absolute_difference_function = lambda list_value : abs(list_value - con)
	con = min(out, key=absolute_difference_function)
	time_index = out.index(con)
	print(f"Tm of {name} : {t[time_index]}s")

#file inputs
df1 = pd.read_csv("./Pot_Data.csv")
df2 = pd.read_csv("./Motor_Speed.csv")
df3 = pd.read_csv("./Motor_Position_4.55.csv")
df4 = pd.read_csv("./Motor_Position_10.csv")
df5 = pd.read_csv("./Motor_Position_21.4.csv")
df6 = pd.read_csv("./Motor_Position_21.4_tacho.csv")
df7 = pd.read_csv("./Motor_Position_21.4_tacho_positive.csv")

#loading values for calculations
x1 = df1["Shaft angular position"].tolist()
y1 = df1["Wiper voltage"].tolist()
t2 = df2["time"].tolist()
x2 = df2["Tacho output"].tolist()
y2 = df2["Motor Speed"].tolist()
x3 = df3["time"].tolist()
y3 = df3["rotor angular position"].tolist()
x4 = df4["time"].tolist()
y4 = df4["rotor angular position"].tolist()
x5 = df5["time"].tolist()
y5 = df5["rotor angular position"].tolist()
x6 = df6["time"].tolist()
y6 = df6["rotor angular position"].tolist()

#calculations
sens(x1,y1,"Potentiometer","V/deg")
sens(y2,x2,"System","rad/Vs")
gain(x2,y2,"System")
timeconstant(t2,x2,"System")
step_info(x3,y3,"At 4.55 gain")
dampingratio(y3,"At 4.55 gain")
peaktime(x3,y3,"At 4.55 gain","s")
steadystateerror(y3,"At 4.55 gain")

step_info(x4,y4,"At 10 gain")
dampingratio(y4,"At 10 gain")
peaktime(x4,y4,"At 10 gain","s")
steadystateerror(y4,"At 10 gain")

step_info(x5,y5,"At 21.4 gain")
dampingratio(y5,"At 21.4 gain")
peaktime(x5,y5,"At 21.4 gain","s")
steadystateerror(y5,"At 21.4 gain")

step_info(x6,y6,"At 21.4 tacho gain")
dampingratio(y6,"At 21.4 tacho gain")
peaktime(x6,y6,"At 21.4 tacho gain","s")
steadystateerror(y6,"At 21.4 tacho gain")

#plots
fig, axs = plt.subplots(3, 3, constrained_layout=True)
fig.suptitle('Control Lab Assignment 1', fontsize=16)
axs[0,0].plot(df1["Shaft angular position"].to_numpy(), df1["Wiper voltage"].to_numpy(), color='hotpink')
axs[0,0].set_title('Potentiometer Data')
axs[0,0].set_xlabel('Shaft angular position')
axs[0,0].set_ylabel('Wiper voltage')

axs[0,1].plot(df2["time"].tolist(), df2["Motor Speed"].tolist(), color='indigo')
axs[0,1].set_title('Motor Speed')
axs[0,1].set_xlabel('Time')
axs[0,1].set_ylabel('Motor Speed')

axs[0,2].plot(df2["time"].tolist(), df2["Tacho output"].tolist(), color='teal')
axs[0,2].set_title('Motor Speed')
axs[0,2].set_xlabel('Time')
axs[0,2].set_ylabel('Tacho Output')

axs[1,0].plot(df3["time"].tolist(), df3["rotor angular position"].tolist(), color='mediumspringgreen')
axs[1,0].set_title('Motor_Position_4.55')
axs[1,0].set_xlabel('Shaft angular position')
axs[1,0].set_ylabel('Wiper voltage')

axs[1,1].plot(df4["time"].tolist(), df4["rotor angular position"].tolist(), color='gold')
axs[1,1].set_title('Motor_Position_10')
axs[1,1].set_xlabel('time')
axs[1,1].set_ylabel('rotor angular position')

axs[1,2].plot(df5["time"].tolist(), df5["rotor angular position"].tolist(), color='orangered')
axs[1,2].set_title('Motor_Position_21.4')
axs[1,2].set_xlabel('time')
axs[1,2].set_ylabel('rotor angular position')

axs[2,0].plot(df6["time"].tolist(), df6["rotor angular position"].tolist(), color='lightcoral')
axs[2,0].set_title('Motor_Position_21.4_tacho')
axs[2,0].set_xlabel('time')
axs[2,0].set_ylabel('rotor angular position')

axs[2,1].plot(df7["time"].tolist(), df7["rotor angular position"].tolist(), color='hotpink')
axs[2,1].set_title('Motor_Position_21.4_tacho_positive')
axs[2,1].set_xlabel('time')
axs[2,1].set_ylabel('rotor angular position')

axs[2,2].plot(df2["Motor Speed"].tolist(), df2["Tacho output"].tolist(), color='aqua')
axs[2,2].set_title('Motor Speed')
axs[2,2].set_xlabel('Motor Speed')
axs[2,2].set_ylabel('Tacho Output')
plt.show()
