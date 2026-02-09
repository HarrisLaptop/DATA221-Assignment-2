# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 4

# Import the pandas package using the alias pd
import pandas as pd

# Read the contents of the csv file using the pandas package to convert the data into a dataframe
data_frame_of_students = pd.read_csv("student.csv")


# Filter the students we want to include in the new file according to the desired conditions
data_frame_of_students = data_frame_of_students[data_frame_of_students["studytime"] >= 3]
data_frame_of_students = data_frame_of_students[data_frame_of_students["internet"] == 1]
data_frame_of_students = data_frame_of_students[data_frame_of_students["absences"] <= 5]

# Convert our data frame into a csv file called high_engagement.csv
data_frame_of_students.to_csv('high_engagement.csv')

# Store the number of students in the filtered data frame here
number_of_high_engagement_students = len(data_frame_of_students)
# Store the sum of all filtered student grade values here
sum_of_grades_of_high_engagement_students = data_frame_of_students["grade"].sum()
# Store the average of all student grade values here. Round to 4 decimals
average_grade_of_high_engagement_students = round(sum_of_grades_of_high_engagement_students/number_of_high_engagement_students, 4)

# Print how many students there are saved in the new csv file and the average grade of these students
print("There are " + str(number_of_high_engagement_students) + " students saved in the high engagement file")
print("The average grade of these students is " + str(average_grade_of_high_engagement_students) + ".")