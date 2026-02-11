# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 9

# Import packages needed for website scraping
import requests
from bs4 import BeautifulSoup
import csv

# Store the Wikipedia URL as a sting
wikipedia_url = "https://en.wikipedia.org/wiki/Machine_learning"

# Set these headings so that Wikipedia can allow us to scrape from their website
headers_for_wikipedia_access = {
    "User-Agent": "Mozilla/5.0 (compatible; HarrisKhanBot/1.0; +https://example.com/contact)"
}

# Store the contents of the wikipedia article here
contents_of_wikipedia_article = requests.get(wikipedia_url, headers=headers_for_wikipedia_access)

# Allows us to 'parse' or analyze the contents of the wikipedia article
wikipedia_article_parser = BeautifulSoup(contents_of_wikipedia_article.text, 'html.parser')

# Use beautiful soup to find the main article content
content_div = wikipedia_article_parser.find("div", id="mw-content-text")

# Find all tables within the main content
tables_in_wiki_article = content_div.find_all("table")

# Will store the value of the first valid table in this variable
target_table = None

#Locate the first table with at least 3 data rows

# For every table in the wiki article
for table in tables_in_wiki_article:

    # Find all the rows in the table
    rows_in_table = table.find_all("tr")

    # Counts the number of rows that contain some data to see if the table will be valid
    data_row_counter = 0

    # For every row in the table
    for row in rows_in_table:

        # If the row has some data values in it
        if row.find_all("td"):
            # Increment the number of rows that have some data in them
            data_row_counter += 1

    # If the number of rows in the table that have data in them is 3 or greater
    if data_row_counter >= 3:
        # Set this table as our target table and break out of this for loop.
        target_table = table
        break

# Find all of the header cells in the table using the tag <th>
header_cells_in_table = target_table.find_all("th")
# Define an empty list where we will store the extracted header names
headers_in_table = []

# If there are header cells in the table
if header_cells_in_table:
    # For every header in the table
    for header in header_cells_in_table:

        # Append the extracted headers to this list of headers after stripping them
        headers_in_table.append(header.get_text().strip())
else:
    # If there are no headers, build generic ones based on first data row
    first_data = target_table.find_all("tr")[0].find_all(["td", "th"])
    headers = [f"col{i+1}" for i in range(len(first_data))]

# Find all the rows in the table
rows_in_table = target_table.find_all("tr")

# Define an empty list to store each row's data in
table_data = []

# For every row in the table
for row in rows_in_table:

    # Find all header and data cells
    cells_in_table = row.find_all(["td", "th"])

    # If the cells exist
    if cells_in_table:

        # Define an empty list to hold the value of each row
        row_values = []

        # For every cell in the table
        for cell in cells_in_table:
            # Append the cell text to the row
            row_values.append(cell.get_text())

        # Pad the row if it has fewer cells than headers with empty values
        while len(row_values) < len(headers_in_table):
            row_values.append("")

        # After adding all the data to each row, append it to the table data
        table_data.append(row_values)

# Create a new file "wiki_table.csv" in write mode, where each new line is empty.
# Set encoding to "utf-8" so that it may handle special characters
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:

    # Write into a csv file
    writer = csv.writer(f)
    # For the first row, write the headers of the table
    writer.writerow(headers_in_table)
    # For every row in the table data, write each row into the csv file
    for row in table_data:
        writer.writerow(row)
