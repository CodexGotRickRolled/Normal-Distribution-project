import pandas as pd
import statistics
import math
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
data=df["Avg Rating"].tolist()
mean=statistics.mean(data)
fig = ff.create_distplot([data],["Mobile Brand"], show_hist=False) 
fig.show()
