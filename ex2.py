# -*- coding: utf-8 -*-

import quandl
import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = "gf5eAsmr4BqnDX6nYHrc"

data = quandl.get("WIKI/AAPL", rows=5)
print(data)
#data.to_csv('aapl1.csv')
#df=pd.read_csv('aapl1.csv',header=0)
#print(df)
#rural = quandl.get("WORLDBANK/USA_SP_RUR_TOTL_ZS")
#urban = quandl.get("WORLDBANK/USA_SP_URB_TOTL_IN_ZS")
#plt.subplot(2, 1, 1)
#plt.plot(rural.index,rural)
#plt.xticks(rural.index[0::3],[])
#plt.title("American Population")
#plt.ylabel("% Rural")
#plt.subplot(2, 1, 2)
#plt.plot(urban.index,urban)
#plt.xlabel("year")
#plt.ylabel("% Urban")
#plt.show()