import csv
import pandas as pd
import plotly.graph_objects as go

read=pd.read_csv("data.csv")

df=read.groupby("level")["attempt"].mean()
fig=go.Figure(go.Bar(x=df,y=["Level 1","Level 2","Level 3","Level 4"],orientation="h"))
fig.show()
print(df)
