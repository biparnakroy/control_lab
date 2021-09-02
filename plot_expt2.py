import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import os
import math

def step_info(t,yout,name):
    print (f"{name} OS: %f%s"%((max(yout)/yout[-1]-1)*100,'%'))
    print (f"{name} Tr: %fs"%(t[next(i for i in range(0,len(yout)-1) if yout[i]>yout[-1]*.90)]-t[0]))
    print (f"{name} Ts: %fs"%(t[next(len(yout)-i for i in range(2,len(yout)-1) if abs(yout[-i]/yout[-1])>1.02)]-t[0]))

df = pd.read_csv("./TR_data.csv")

x1 = df["Input"].tolist()
y1 = df["Output"].tolist()
t2 = df["Time"].tolist()

fig, axs = plt.subplots(2, 1, constrained_layout=True)
fig.suptitle('Control Lab Assignment 2', fontsize=16)

axs[0].plot(df["Time"].to_numpy(), df["Input"].to_numpy(), color='hotpink')
axs[0].set_title('Input Signal')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Wiper voltage')

axs[1].plot(df["Time"].to_numpy(), df["Output"].to_numpy(), color='hotpink')
axs[1].set_title('Output Signal')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Output')

plt.show()
