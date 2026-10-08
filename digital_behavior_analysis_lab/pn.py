import pandas as pd
import csv
df = pd.read_csv("digital_behavior_analysis_lab/digital_behaviour.csv")
print(df.head()) 
print(df.tail())
print(df.shape)
print(df.columns)
print(df["Instagram_Minutes"])
print(df[["Instagram_Minutes","Date"]])
print(df.describe())
print(df["Instagram_Minutes"].sum())
print(df["Study_Minutes"].mean())
print(df["YouTube_Minutes"].max())
p=df[df["Instagram_Minutes"]>100]
print(p["Date"])
p=df[df["YouTube_Minutes"]>180]
print(p["Date"])
l=df["Instagram_Minutes"].max()
k=df["Study_Minutes"].min()
print(df[df["Instagram_Minutes"]==l])