📊 Task 1 – Data Cleaning & Preprocessing

🏢 Internship Task
This project is part of my Data Analyst Internship.
The objective was to clean and preprocess a raw dataset to make it analysis-ready.

📁 Dataset Used
Netflix Movies and TV Shows Dataset
Total records: 8807
Total columns: 12

The dataset contains information about Netflix titles including:
Show ID
Type (Movie/TV Show)
Title
Director
Cast
Country
Date Added
Release Year
Rating
Duration
Genre (listed_in)
Description

🎯 Objective
To perform real-world data cleaning by:
Identifying missing values
Handling null entries
Removing duplicates
Converting incorrect data types
Standardizing dataset structure

🧹 Data Cleaning Steps Performed
1️⃣ Handling Missing Values
Filled missing director values with "Unknown"
Filled missing cast values with "Not Available"
Filled missing country using mode value
Converted date_added column to datetime format
Remaining minimal missing values in rating (4) and duration (3) were retained as they were insignificant

2️⃣ Removing Duplicates
Checked for duplicate rows
Removed duplicates using drop_duplicates()
Final duplicate count: 0

3️⃣ Data Type Conversion
Converted date_added from object → datetime64[ns]
Ensured release_year is integer type

4️⃣ Final Dataset Summary
Metric	Value
Initial Records	8807
Final Records	8797
Duplicate Rows Removed	0
Cleaned Date Format	Yes
Major Missing Values Handled	Yes

🛠 Tools Used
Python
Pandas
VS Code

📌 Key Learnings
Handling real-world missing data
Fixing inconsistent date formats
Avoiding chained assignment warnings
Writing cleaner and safer Pandas code
Making datasets analysis-ready

🚀 Outcome
The dataset is now clean, structured, and ready for further analysis or visualization.

📂 Files Included
Task_1.py – Python script for cleaning
cleaned_netflix_dataset.csv – Final cleaned dataset
Screenshots of execution output

👨‍💻 Author
Jayanth B
