import numpy as np
import pandas as pd

# For reproducible data
np.random.seed(42)

# Number of students
n = 500

# Student details
student_id = np.arange(1001, 1001 + n)

names = [f"Student_{i}" for i in range(1, n + 1)]

branches = np.random.choice(
    ["CSE", "AIML", "IT", "ECE", "EEE", "CSD"],
    size=n
)

# Academic and placement preparation data
cgpa = np.round(np.random.uniform(6.0, 9.8, n), 2)

dsa_problems = np.random.randint(20, 501, n)

aptitude_score = np.random.randint(35, 101, n)

coding_score = np.random.randint(30, 101, n)

communication_score = np.random.randint(40, 101, n)

projects = np.random.randint(0, 6, n)

resume_score = np.random.randint(40, 101, n)

mock_interviews = np.random.randint(0, 11, n)

# Create DataFrame
df = pd.DataFrame({
    "student_id": student_id,
    "name": names,
    "branch": branches,
    "cgpa": cgpa,
    "dsa_problems": dsa_problems,
    "aptitude_score": aptitude_score,
    "coding_score": coding_score,
    "communication_score": communication_score,
    "projects": projects,
    "resume_score": resume_score,
    "mock_interviews": mock_interviews
})

# Save as CSV
df.to_csv("placement_data.csv", index=False)

print("CSV file generated successfully!")
print(f"Total students: {len(df)}")
print("\nFirst 5 students:")
print(df.head())