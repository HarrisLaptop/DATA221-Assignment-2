# Notes:
- The given .txt and .csv files are also listed in this Git repository, as these are the files that are required for some of the programs to function as intended.
- The files created by the programs have also been listed here in this Git repository.

# Question 1:
- This program reads the text content from sample-file.txt and splits the lines into tokens (words), then prints the most frequent words in the program and the number of times they appeared.

# Question 2:
- This program reads the text content from sample-file.txt and splits the lines into tokens (words), then constructs bigrams after lower-casing and stripping the tokens of their punctuation.
- After that, the program prints out the 5 most frequent bigrams in the program and their frequency count in descending order.

# Question 3:
- This program reads the text content from sample-file.txt, then converts the text into lowercase and removes any punctuation and whitespace to check if there are other near-duplicate lines.
- After identifying if there are any near-duplicate lines, the program prints the first two sets of near-duplicate lines and their respective line numbers in their original form.
- I was unsure if the assignment asked for the modified lines or not, but I included the first two sets of modified lines anyway to show how they are near-duplicates of each other.

# Question 4:
- Using the pandas package, this program reads the csv content from student.csv and loads that data into a dataframe.
- After creating the dataframe, the program filters students whose studytime value is >= 3, internet = 1, and absences is <= 5, and saves that data into a new file called high_engagement.csv
- Finally, the program prints the number of students saved in the new csv file and their collective average grade.

# Question 5:
- Using the pandas package, this program reads the csv content from student.csv and creates a new column called grade_band and assigns each student a categorical value depending on their grade performance.
- After that, the program creates a grouped summary table showing, for each band, the number of students, average absences, and the percentage of students with internet access.
- The grouped summary table is then saved as student_bands.csv.

# Question 6:
- Using the pandas package, this program reads the csv content from crimes.csv and creates a new column called risk.
- For each row, they are assigned either a high or low risk rating depending on whether their ViolentCrimesPerPop value is >= 50 or < 50, respectively.
- After that, the program creates a summary table grouped by the risk column and calculates each group's PctUnemployed values. The table is then printed to the console.

# Question 7:
- Using the requests and beautiful soup packages, this program scrapes the Wikipedia page on Data Science.
- The program extracts and prints the title, and the first paragraph from the main content that contains > 50 characters (after stripping whitespace)

# Question 8:
- Using the requests and beautiful soup packages, this program scrapes the same Wikipedia page on Data Science.
- The program extracts all section headers and saves them to a headings.txt file, except for headers containing the words: References, External links, See also, and Notes.
- If any of the headings contain the text "[edit]", then the program removes that bit of text from the header before saving it to the txt file.

# Question 9:
- Using the requests and beautiful soup packages, this program scrapes the Wikipedia page on Machine Learning.
- The program finds the first table that contains three rows that contain some data in them.
- Then, the program extracts the <th> table headers from the table if they exist. Otherwise, generic column names are created instead.
- After that, any rows that have fewer columns than others are padded with new columns containing empty strings.
- Finally, the extracted table is saved to wiki_table.csv.

# Question 10:
- This program defines a function that searches for a keyword within a given .txt file and returns a list of tuples containing the line number and the line contents.
- After that, the program prints how many matching lines were found and the first three matching lines with their line number.
- IMPORTANT NOTE: The keyword "lorem" is used in the program since that is what the assignment asks for; there are no words in the file that contain this keyword. You may change this while testing if you like
