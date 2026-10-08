import pandas as pd
import numpy as np

df = pd.read_csv("placement_data.csv")
print(df)
# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

'''project_folder = Path(__file__).parent
csv_file = project_folder / "placement_data.csv"
df = pd.read_csv("csv_file") '''

print("=" * 60)
print("       COLLEGE PLACEMENT READINESS TRACKER")
print("=" * 60)

print("\nTotal Students:", len(df))


# --------------------------------------------------
# 2. CONVERT RAW VALUES INTO 0-100 SCORES
# --------------------------------------------------

# CGPA: maximum CGPA = 10
df["cgpa_score"] = (df["cgpa"] / 10) * 100

# DSA: 500 problems considered as 100%
df["dsa_score"] = np.clip(
    (df["dsa_problems"] / 500) * 100,
    0,
    100
)

# Projects: 5 projects considered as 100%
df["project_score"] = np.clip(
    (df["projects"] / 5) * 100,
    0,
    100
)

# Mock interviews: 10 considered as 100%
df["mock_score"] = np.clip(
    (df["mock_interviews"] / 10) * 100,
    0,
    100
)


# --------------------------------------------------
# 3. CALCULATE PLACEMENT READINESS SCORE
# --------------------------------------------------

df["readiness_score"] = (
    df["cgpa_score"] * 0.15
    + df["dsa_score"] * 0.20
    + df["aptitude_score"] * 0.15
    + df["coding_score"] * 0.20
    + df["communication_score"] * 0.10
    + df["project_score"] * 0.10
    + df["resume_score"] * 0.05
    + df["mock_score"] * 0.05
)

# Round score
df["readiness_score"] = df["readiness_score"].round(2)


# --------------------------------------------------
# 4. CLASSIFY STUDENTS
# --------------------------------------------------

df["readiness_level"] = np.select(
    [
        df["readiness_score"] >= 80,
        df["readiness_score"] >= 65,
        df["readiness_score"] >= 50
    ],
    [
        "Placement Ready",
        "Almost Ready",
        "Needs Improvement"
    ],
    default="Needs Serious Preparation"
)


# --------------------------------------------------
# 5. FIND WEAKEST AREA
# --------------------------------------------------

score_columns = [
    "cgpa_score",
    "dsa_score",
    "aptitude_score",
    "coding_score",
    "communication_score",
    "project_score",
    "resume_score",
    "mock_score"
]

df["weakest_area"] = df[score_columns].idxmin(axis=1)

area_names = {
    "cgpa_score": "CGPA",
    "dsa_score": "DSA",
    "aptitude_score": "Aptitude",
    "coding_score": "Coding",
    "communication_score": "Communication",
    "project_score": "Projects",
    "resume_score": "Resume",
    "mock_score": "Mock Interviews"
}

df["weakest_area"] = df["weakest_area"].map(area_names)


# --------------------------------------------------
# 6. BASIC PLACEMENT ELIGIBILITY
# --------------------------------------------------

df["placement_eligible"] = np.where(
    (df["cgpa"] >= 7.5)
    & (df["coding_score"] >= 60)
    & (df["aptitude_score"] >= 60),
    "Eligible",
    "Not Eligible"
)


# --------------------------------------------------
# 7. DISPLAY STUDENT RESULTS
# --------------------------------------------------

result_columns = [
    "student_id",
    "name",
    "branch",
    "cgpa",
    "readiness_score",
    "readiness_level",
    "weakest_area",
    "placement_eligible"
]

print("\nPLACEMENT READINESS RESULTS")
print("-" * 60)

print(df[result_columns].head(20).to_string(index=False))


# --------------------------------------------------
# 8. OVERALL STATISTICS
# --------------------------------------------------

print("\n" + "=" * 60)
print("OVERALL STATISTICS")
print("=" * 60)

print("\nAverage CGPA:",
      round(df["cgpa"].mean(), 2))

print("Average DSA Problems:",
      round(df["dsa_problems"].mean(), 2))

print("Average Coding Score:",
      round(df["coding_score"].mean(), 2))

print("Average Aptitude Score:",
      round(df["aptitude_score"].mean(), 2))

print("Average Communication Score:",
      round(df["communication_score"].mean(), 2))

print("Average Readiness Score:",
      round(df["readiness_score"].mean(), 2))


# --------------------------------------------------
# 9. READINESS DISTRIBUTION
# --------------------------------------------------

print("\nREADINESS DISTRIBUTION")
print("-" * 60)

print(df["readiness_level"].value_counts())


# --------------------------------------------------
# 10. PLACEMENT ELIGIBILITY
# --------------------------------------------------

print("\nPLACEMENT ELIGIBILITY")
print("-" * 60)

print(df["placement_eligible"].value_counts())


# --------------------------------------------------
# 11. BRANCH-WISE ANALYSIS
# --------------------------------------------------

print("\nBRANCH-WISE READINESS")
print("-" * 60)

branch_analysis = df.groupby("branch").agg(
    students=("student_id", "count"),
    average_cgpa=("cgpa", "mean"),
    average_coding=("coding_score", "mean"),
    average_dsa=("dsa_problems", "mean"),
    average_readiness=("readiness_score", "mean")
)

branch_analysis = branch_analysis.round(2)

print(branch_analysis)


# --------------------------------------------------
# 12. SAVE FINAL RESULTS
# --------------------------------------------------

#output_file = project_folder / "placement_readiness_results.csv"

#df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("Analysis completed successfully!")
print("Results saved to:")
#print(output_file)
print("=" * 60)