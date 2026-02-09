# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 3

# Open the sample file in read mode
sample_file_to_read = open("sample-file.txt", "r")

# Read the lines of the sample file and store them into this list of lines variable
lines_in_sample_file = sample_file_to_read.readlines()

# Close the file now that we have read the information that we need from it.
sample_file_to_read.close()

# Store the characters to remove in a variable
remove_chars = ",!-. \n"

# Create an empty list to hold the modified versions of each line in sample file
updated_list_of_lines_in_sample_file = []

# For every line in the sample file
for line in lines_in_sample_file:
    # Remove the unwanted punctuation and characters from the line. Lowercase the line.
    line = line.translate(str.maketrans('', '', remove_chars))
    line = line.lower()

    # After modifying the line, append it to our list of modified lines
    updated_list_of_lines_in_sample_file.append(line)

# Create an integer variable to track the number of near duplicate sets of lines.
number_of_near_duplicate_sets = 0
# Create an empty list that will hold the line number information for the near duplicate sets of lines.
list_of_line_information = []

# For every line in our modified list of lines in sample file
for current in range(len(updated_list_of_lines_in_sample_file)):

    # For every line after the current line we are tracking to the end of the modified sample file lines
    for pointer in range(current + 1, len(updated_list_of_lines_in_sample_file)):

        # if the two lines we are tracking are equal to each other and they are empty lines, we have found a near duplicate set
        if updated_list_of_lines_in_sample_file[current] == updated_list_of_lines_in_sample_file[pointer]\
                and len(updated_list_of_lines_in_sample_file[current]) > 1:

            # Increment the number of near duplicate sets
            number_of_near_duplicate_sets += 1
            # Append a tuple of the line number information of the near duplicate sets
            list_of_line_information.append((current, pointer))

# Print how many unique sets of near duplicate lines there are
print("There are " + str(number_of_near_duplicate_sets) + " unique sets of near-duplicate lines.")

# Of the first two sets, print their original lines and their respective line number
print("\nOriginal Lines: ")
# For the first two sets of near duplicate lines
for set in range(0,2):
    # Print each set's original line and their respective line number
    print("Set ", str(set + 1))
    print(str(list_of_line_information[set][0] + 1) + ":  " + lines_in_sample_file[list_of_line_information[set][0]], end="")
    print(str(list_of_line_information[set][1] + 1) + ": " + lines_in_sample_file[list_of_line_information[set][1]])

# Of the first two sets, print their modified lines and their respective line number
print("\nModified Lines: ")
# For the first two sets of near duplicate lines
for set in range(0,2):
    # Print each set's modified line and their respective line number
    print("Set ", str(set + 1))
    print(str(list_of_line_information[set][0] + 1) + " -->  " + updated_list_of_lines_in_sample_file[list_of_line_information[set][0]])
    print(str(list_of_line_information[set][1] + 1) + " --> " + updated_list_of_lines_in_sample_file[list_of_line_information[set][1]], "\n")