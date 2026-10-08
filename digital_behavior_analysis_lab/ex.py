import numpy as np
import csv
insta_list = []
study_time = []
with open(r"C:\Users\U Mahendra\OneDrive\Documents\Desktop\tech_projects\digital_behavior_analysis_lab\digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_time.append(int(row["LinkedIn_Minutes"]))

insta_list = insta_list[:7]
study_time = study_time[:7]
insta_array = np.array(insta_list)
study_array = np.array(study_time)
print(insta_array)
total = insta_array.sum()
#avg = total / len(insta_array)
avg=insta_array.mean()
print(avg)
maximum = np.max(insta_array)
print(maximum)
minimum = np.min(insta_array)
print(minimum)
print(insta_array.sum())
print(insta_array[0])
print(insta_array[-1])
print(insta_array[4])
print(insta_array[:3:])
print(insta_array[-1::])
print(insta_array[2:5:])
insta_array1=insta_array/60
diff=insta_array-study_array
dif_array=[insta_array>100]
print(dif_array)
dif_array=insta_array[insta_array>100]
print(dif_array)
print(len(dif_array))
diff_array=insta_array[insta_array>avg]
print(dif_array)