import csv 
import random as rd
from datetime import datetime, timedelta

Num_Days = 35
rd.seed()

row=[]

for i in range(Num_Days):
    insta_reel=rd.randint(30,60*14)
    insta_post=rd.randint(20,60*2)
    face_post=rd.randint(1,60*24)
    face_reel=rd.randint(1,60*24)
    what_message=rd.randint(1,60*24)
    what_status=rd.randint(1,60*24)

    row.append([insta_reel,insta_post,face_post,face_reel,what_message,what_status])
#print(row)
with open(
    "digital_behavior_analysis.csv",
    "w",
    newline='',
    encoding="utf-8"
) as f:
    x=csv.writer(f)
    x.writerow(["insta_reel","insta_post","face_post","face_reel","what_message","what_status"])
    x.writerows(row)
print("CSV file created successfully!")














































