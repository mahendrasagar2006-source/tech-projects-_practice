import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import pandas as pd
import csv
df = pd.read_csv("digital_behavior_analysis_lab/digital_behaviour.csv")

plt.title("screen time")
df["Total_Screen_Time"] = df["Instagram_Minutes"] + df["YouTube_Minutes"] + df["Study_Minutes"]+df["LinkedIn_Minutes"]
df["day_time"]=[f"D{i+1}" for i in range(len(df))]
plt.figure(figsize=(10,5))
plt.xlabel("day_time")
plt.ylabel("Total_Screen_Time")
plt.tight_layout()
plt.bar(df["day_time"],df["Total_Screen_Time"],label="Total_Screen_Time",color="blue")
#plt.show()
# Total minutes for each app
apps = [
    "Instagram",
    "YouTube",
    "WhatsApp",
    "LinkedIn"
]

app_times = [
    df["Instagram_Minutes"].sum(),
    df["YouTube_Minutes"].sum(),
    df["WhatsApp_Minutes"].sum(),
    df["LinkedIn_Minutes"].sum()
]

plt.figure(figsize=(8, 5))

plt.bar(apps, app_times, label="Total Time", color="blue")

plt.title("Total Time by App")
plt.xlabel("App")
plt.ylabel("Minutes")

plt.legend()
plt.tight_layout()
plt.show()

# Find app with maximum time
max_index = app_times.index(max(app_times))

print("App that took the most time:", apps[max_index])
print("Total time:", app_times[max_index], "minutes")




df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)

df["day_time"] = [f"D{i+1}" for i in range(len(df))]

plt.figure(figsize=(10, 5))

# Study line
plt.plot(
    df["day_time"],
    df["Study_Minutes"],
    marker="o",
    label="Study Minutes"
)

# Screen time line
plt.plot(
    df["day_time"],
    df["Total_Screen_Time"],
    marker="o",
    label="Total Screen Time"
)

plt.title("Study vs Screen Time")
plt.xlabel("Day")
plt.ylabel("Minutes")

# Legend
plt.legend()

plt.tight_layout()
plt.show()




apps = [
    "Instagram",
    "YouTube",
    "WhatsApp",
    "LinkedIn"
]

app_times = [
    df["Instagram_Minutes"].sum(),
    df["YouTube_Minutes"].sum(),
    df["WhatsApp_Minutes"].sum(),
    df["LinkedIn_Minutes"].sum()
]

plt.figure(figsize=(8, 8))

plt.pie(
    app_times,
    labels=apps,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Share of My App Time")

plt.show()