# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 5

# Import the pandas package using the alias pd
import pandas as pd
# Import the numpy package using the alias np
import numpy as np

# Read the contents of the csv file using the pandas package to convert the data into a dataframe
data_frame_of_students = pd.read_csv("student.csv")

# Create the conditions for what grade band label each student will get
conditions_for_grade_band = [
    data_frame_of_students["grade"] <= 9,
    (data_frame_of_students["grade"] > 9) & (data_frame_of_students["grade"] <= 14),
    data_frame_of_students["grade"] > 14
]

# Create the grade band labels
grade_band_labels = ["Low", "Medium", "High"]

# Create a new column called grade_band that uses the conditions and labels to assign each student's grade band
data_frame_of_students["grade_band"] = np.select(conditions_for_grade_band, grade_band_labels, default=None)

# Create a grouped summary table
summary_table_of_students_by_grade_bands = (
    # Using the data frame of students, aggregate new table values
    data_frame_of_students.groupby("grade_band").agg(
        # Assign the number of students in this grade band
        number_of_students = ("grade", "count"),
        # Assign the average absences of this grade band
        average_absences = ("absences", "mean"),
        # Assign the percentage of students who have internet in this grade band
        percentage_internet = ("internet", lambda x: x.mean() * 100)
    )
)

# Convert our grouped summary table into a csv file called student_bands.csv
summary_table_of_students_by_grade_bands.to_csv('student_bands.csv')