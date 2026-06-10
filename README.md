# week2-data-cleaning-pandas
Focused on data cleaning, transformation, feature engineering, and grouped analysis using pandas.
Overview

This project was completed as part of the Artificial Intelligence Internship Program at Sohail Smart Solutions.

The objective of this assignment was to learn how to identify, clean, transform, and analyze messy datasets using the pandas library. Real-world datasets often contain missing values, inconsistent formatting, incorrect data types, and incomplete records. This project demonstrates practical techniques used to prepare data before analysis and Machine Learning.

Learning Objectives

This project focused on:

Detecting missing values
Handling incomplete records
Understanding data types
Converting invalid data formats
Creating derived features
Performing grouped analysis
Preparing datasets for future AI and Machine Learning workflows
Dataset Description

A student dataset containing academic records was intentionally modified to simulate real-world data quality problems.

Examples of issues introduced:

Missing grades
Missing majors
Empty student names
Extra spaces in names
Inconsistent capitalization
Invalid data types (e.g., "Ninety" instead of a numeric value)
Data Cleaning Process
1. Missing Values

Used:

df.isnull()
df.fillna()

Missing grades were replaced using the column mean to preserve records while maintaining dataset completeness.

2. Data Type Conversion

Used:

pd.to_numeric(errors="coerce")

Invalid values were converted to numeric format and handled appropriately.

3. Name Standardization

Used:

str.strip()
str.title()

Names were cleaned by removing extra spaces and applying consistent capitalization.

4. Missing Categories

Missing majors were replaced with:

Undeclared

to preserve records for analysis.

Feature Engineering

A new feature was created:

average
df["average"] = (df["math"] + df["science"]) / 2

This derived feature represents the average academic performance of each student.

grade_category

Students were classified into performance categories:

Average Score	Category
90+	A
80–89	B
70–79	C
Below 70	D
Group Analysis

Two grouped analyses were performed using pandas:

Student Count by Grade Category
df.groupby("grade_category").size()
Average Score by Major
df.groupby("major")["average"].mean()

These analyses demonstrate how pandas can summarize and aggregate large datasets efficiently.

Technologies Used
Python 3
pandas
NumPy
JSON
Repository Structure
week3-data-cleaning-pandas/
│
├── data_cleaning_analysis.py
├── messy_students.json
├── cleaned_students.json
└── README.md
Key Learning Outcomes

Through this project, I learned how to:

Detect data quality issues
Clean and standardize datasets
Handle missing values responsibly
Transform data for analysis
Create derived features
Perform grouped analysis using pandas
Prepare datasets for future Machine Learning workflows
Conclusion

Data cleaning is one of the most important stages in the data science process. This project demonstrated how raw, inconsistent data can be transformed into a structured and reliable dataset suitable for analysis and future AI applications.

The skills developed in this assignment provide a strong foundation for upcoming Machine Learning and Artificial Intelligence projects.
