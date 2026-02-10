# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 10

# Define a function that takes in a file and a keyword and returns the lines containing that keyword
def find_lines_containing(filename, keyword):
    
    # Open the file in read mode
    file_to_search = open(filename, 'r')
    
    # Store the contents of the file in a list
    contents_of_file = file_to_search.readlines()
    
    # Create a list of lines containing 
    lines_containing_keyword_information = []

    # For every line in the file
    for line_index in range(len(contents_of_file)):

        # if the keyword is in the contents of the file (lowercased both for case-insensitivity)
        if keyword.lower() in contents_of_file[line_index].lower():

            # Append a tuple containing the line number and the contents of the line
            lines_containing_keyword_information.append((line_index + 1, contents_of_file[line_index]))

    # Return the list of matching lines information
    return lines_containing_keyword_information

# Define a variable containing the returned list from sample-file after searching for the word "lorem"
word_searcher = find_lines_containing("sample-file.txt", "lorem")

# Print the number of lines that contained the keyword
print("There are " + str(len(word_searcher)) + " lines containing the keyword in the file.")

# Define a variable to count how many iterations of the for loop have occurred
iterations_of_for_loop_counter = 0

# For the first three matching lines
for line in range(len(word_searcher)):
    # Print the line number and the line itself
    print(str(word_searcher[line][0]) + ": " + word_searcher[line][1])

    # Increment the number of iterations tracker
    iterations_of_for_loop_counter += 1

    # If we have hit 3 iterations
    if iterations_of_for_loop_counter == 3:
        # Break out of the for loop.
        break