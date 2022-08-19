import pandas as pd
import numpy as np
import requests
import io
import matplotlib.pyplot as plt
from scipy import stats
from math import ceil

url="https://api.covid19india.org/csv/latest/case_time_series.csv"
dataset = requests.get(url).content
df = pd.read_csv(io.StringIO(dataset.decode('utf-8')), header=None, sep=',')
df = df.to_numpy()
df = df[76:]
cnt = 0
t = []
x = []
for idx in df:
	x.append(int(idx[6]))
	t.append(cnt)
	cnt += 1
t = t[1:]
H_t = []
for i in range(1,len(x)):
	temp = x[i]/x[i-1]
	if(temp == 1):
		print(i)
	H_t.append(temp)
slope, intercept, r_value, p_value, std_err = stats.linregress(t, H_t)
y =[]
for i in t:
	y.append(i*slope + intercept)
plt.plot(t, H_t, 'o', label='Covid-19 India data')
plt.plot(t,y, 'r', label='Fitted line')
plt.xlabel('t')
plt.ylabel('H(t)')
plt.suptitle('COVID-19 Data (India)')
a = 1 - intercept
b = float(a/slope)
print(ceil(b))
plt.legend()
plt.show()