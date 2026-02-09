# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 1

# Open the sample file in read mode
sample_file_to_read = open("sample-file.txt", "r")

# Read the contents of the sample file and store them into this contents variable
contents_of_sample_file = sample_file_to_read.read()

# Close the file now that we have read the information that we need from it.
sample_file_to_read.close()

# Split the contents of the sample file into a list of tokens (words) and store it in this variable
tokens_in_sample_file = contents_of_sample_file.split()

# Create an empty list of valid tokens to use later on
updated_list_of_tokens_in_sample_file = []

# For every token in the sample file
for token in range(0, len(tokens_in_sample_file)):

    # Convert the token to lowercase
    tokens_in_sample_file[token] = tokens_in_sample_file[token].lower()
    # Remove any punctuation from both sides of the token
    tokens_in_sample_file[token] = tokens_in_sample_file[token].strip(".,-!")

    # if the length of the token contains at least two alphabetic characters, append it our list of valid tokens
    if len(tokens_in_sample_file[token]) >= 2:
        updated_list_of_tokens_in_sample_file.append(tokens_in_sample_file[token])

# Create an empty dictionary to track each token's frequency
frequency_dictionary_of_tokens_in_sample_file = {}

# For every token in our updated list of valid tokens
for token in updated_list_of_tokens_in_sample_file:

    # If the token is not a key in our frequency dictionary
    if token not in frequency_dictionary_of_tokens_in_sample_file.keys():
        # Create a new key and set its frequency to 1
        frequency_dictionary_of_tokens_in_sample_file[token] = 1
    else: # Otherwise, if the token is already in our frequency dictionary
        # Increment the frequency value of the token by 1
        frequency_dictionary_of_tokens_in_sample_file[token] += 1

# Create a new sorted dictionary of the frequency of each token in descending order of their frequency.
sorted_frequency_dictionary_of_tokens = sorted(frequency_dictionary_of_tokens_in_sample_file.items(), key=lambda x:x[1], reverse=True)

# For the top ten tokens with the highest frequency in our sorted dictionary
for token_in_sorted_dictionary in range(0, 10):
    # Print the token followed by an arrow pointing to its respective frequency count
    print(sorted_frequency_dictionary_of_tokens[token_in_sorted_dictionary][0], "-->",
          sorted_frequency_dictionary_of_tokens[token_in_sorted_dictionary][1])
