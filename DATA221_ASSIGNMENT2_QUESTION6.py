# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 6

# Import the pandas package using the alias pd
import pandas as pd
# Import the numpy package using the alias np
import numpy as np

# Read the csv file and store it as a dataframe in this variable
data_frame_of_crime_stats = pd.read_csv("crime.csv")    

# Create the conditions for what grade band label each student will get.
conditions_for_risk_label = [
    data_frame_of_crime_stats["ViolentCrimesPerPop"] >= 0.5,
    data_frame_of_crime_stats["ViolentCrimesPerPop"] < 0.5
]

# Create the crime risk labels
crime_risk_labels = ["HighCrime", "LowCrime"]

# Create a new column called risk that uses the conditions and labels to assign each group's risk level
data_frame_of_crime_stats["risk"] = np.select(conditions_for_risk_label, crime_risk_labels, default=None)

# Create a grouped summary table
summary_table_of_crime_stats_by_risk = (
    # Using the data frame of crime stats, aggregate new table values
    data_frame_of_crime_stats.groupby("risk").agg(
        # Assign the average absences of this grade band
        average_percent_unemployed = ("PctUnemployed", "mean"),
    )
)

# Print the summary table of crime risk levels and their associated average unemployment percentage
print(summary_table_of_crime_stats_by_risk)