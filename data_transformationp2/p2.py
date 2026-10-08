import pandas as pd
import csv
df=pd.read_csv('day02_usage.csv')
ch=df['Chat'].to_numpy()
vi=df['Video'].to_numpy()
st=df['Study'].to_numpy()
gm=df['Games'].to_numpy()
print(f"chat: {ch.sum()}")
print(f"video: {vi.sum()}")
print(f"study: {st.sum()}")
print(f"games: {gm.sum()}")
print(round(ch.sum()/(24*60),1))
print(round(vi.sum()/(24*60),1))
print(round(st.sum()/(24*60),1))
print(round(gm.sum()/(24*60),1)) 
diff=st-gm
print(diff)
print(diff.argmax());
print(diff.argmin())
day=[]
for i in range(len(diff)):
    day.append(int(max(ch[i],vi[i],st[i],gm[i])))
print(day)
res=[ch+vi+st+gm]
