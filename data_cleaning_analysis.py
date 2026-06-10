import pandas as pd
import numpy as np

# -----------------------------
# Create Messy Dataset
# -----------------------------

students = [
    {"name": "Khaled", "math": 90, "science": 88, "major": "AI"},
    {"name": "khaled", "math": 85, "science": 92, "major": "ai"},
    {"name": "Sara", "math": np.nan, "science": 80, "major": "AI"},
    {"name": "Ahmed", "math": "Ninety", "science": 87, "major": "AI"},
    {"name": "  Omar  ", "math": 78, "science": 82, "major": "Data Science"},
    {"name": "Mariam", "math": 95, "science": np.nan, "major": "AI"},
    {"name": "Layla", "math": 88, "science": 91, "major": "data science"},
    {"name": "", "math": 70, "science": 75, "major": "AI"},
    {"name": "Ali", "math": 60, "science": 65, "major": None},
    {"name": "Noor", "math": 92, "science": 90, "major": "AI"},
    {"name": "Yousef", "math": 85, "science": 79, "major": "AI"},
    {"name": "Fatima", "math": np.nan, "science": 88, "major": "Data Science"},
    {"name": "Zaid", "math": 73, "science": 70, "major": "AI"},
    {"name": "Rana", "math": 81, "science": 85, "major": "AI"},
    {"name": "Hassan", "math": 77, "science": 74, "major": "data science"}
]

df = pd.DataFrame(students)

print("===== MESSY DATASET =====")
print(df)

# Save original messy dataset
df.to_json("messy_students.json", orient="records", indent=4)

# -----------------------------
# Detect Data Problems
# -----------------------------

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DATA TYPES =====")
print(df.dtypes)

# -----------------------------
# Clean Dataset
# -----------------------------

# Convert math column to numeric
df["math"] = pd.to_numeric(df["math"], errors="coerce")

# Fill missing math values
math_mean = df["math"].mean()
df["math"] = df["math"].fillna(math_mean)

# Fill missing science values
science_mean = df["science"].mean()
df["science"] = df["science"].fillna(science_mean)

# Clean names
df["name"] = df["name"].str.strip()
df["name"] = df["name"].replace("", "Unknown")
df["name"] = df["name"].str.title()

# Clean major values
df["major"] = df["major"].fillna("Undeclared")
df["major"] = df["major"].str.title()

print("\n===== CLEANED DATASET =====")
print(df)

# Verify cleaning
print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

# -----------------------------
# Create Derived Feature
# -----------------------------

df["average"] = (df["math"] + df["science"]) / 2

# Grade Category
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

df["grade_category"] = df["average"].apply(get_grade)

print("\n===== DATASET WITH NEW FEATURES =====")
print(df)

# -----------------------------
# Group Analysis
# -----------------------------

print("\n===== STUDENT COUNT BY GRADE CATEGORY =====")
grade_counts = df.groupby("grade_category").size()
print(grade_counts)

print("\n===== AVERAGE SCORE BY MAJOR =====")
major_average = df.groupby("major")["average"].mean()
print(major_average)

# -----------------------------
# Save Clean Dataset
# -----------------------------

df.to_json("cleaned_students.json", orient="records", indent=4)

print("\nClean dataset saved successfully!")
