import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


import os
os.chdir('# put the working directory here #')  # put the working directory path inside the quotation mark


df = pd.read_excel('Lab 2 - Part 2b Set 6.xlsx',  skiprows=2)
# use the name of the file you want to read
name = 'm1t1'

df = df.drop([0])
t = df['Time(s)'].values
print(df)

T1 = df['T1(Deg C)']
P1 = df['P1(PSI)']
Q  = df['Heater Energy (kJ)']
dm = df['Mass Flowrate(g/min)']

l = []
l.append([t,T1])


plt.figure(figsize=(10, 4), dpi=100, facecolor='w', edgecolor='k')
for i in l:
    plt.plot(i[0],i[1])
plt.title('Figure 2.1.2: Temperature (Deg C) v.s. Time(s)')
plt.ylabel('T(Deg C)')
plt.xlabel('t(s)')
plt.legend(['a','b','c','d'])
plt.show()


initial = 8.2
final = 72.4
i = int(10*initial+2)
f = int(10*final+2)

dt = final - initial

c = ((Q[f]-Q[i])/dt-0.1191)/(0.0532*(T1[f]-T1[i])/dt)
print(c)
# print(Q[f])
# (T1[f]-T1[i])/(final-initial)

print((T1[f]-T1[i])/dt)


timestamp = -1
df.iloc[timestamp-50:timestamp].describe()


fig, ax1 = plt.subplots(figsize=(10, 4), dpi=100, facecolor='w', edgecolor='k')

color = 'tab:red'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Temperature (degree C)', color=color)
ax1.plot(t, T1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([-20,80])

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Pressure (psi)', color=color)  # we already handled the x-label with ax1
ax2.plot(t, P1, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim([-20,80])
ax2.set_title('Figure 3.1: Temperature and Pressure v.s. Time for Left Tank with Micrometer Needle Valve')

fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.show()
plt.savefig(name+'.jpg')


timestamp = 7609
df.iloc[timestamp-50:timestamp].describe()

df[-50:-1].describe()

