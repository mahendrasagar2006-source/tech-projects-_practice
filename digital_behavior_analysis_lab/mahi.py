import csv
APP = "Instagram_Minutes"
minutes=[]
with open("C:/Users/U Mahendra/OneDrive/Documents/Desktop/tech_projects/digital_behavior_analysis_lab/digital_behaviour.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(((row["Instagram_Minutes"])))


for i in range(len(minutes)):
    minutes[i] =int (minutes[i])

minutes[:7:]
total =(sum(minutes))
avg=total//len(minutes)
print((max(minutes)))
c=0
for row in minutes:
    if row > avg:
        c+=1
print(c)
print(APP)
