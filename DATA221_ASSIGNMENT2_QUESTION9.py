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
tables = content_div.find_all("table")

target_table = None

# 1. Locate the first table with at least 3 data rows (<tr> excluding header)

for table in tables:
    rows = table.find_all("tr")

    data_row_counter = 0

    for row in rows:
        if row.find_all("td"):
            data_row_counter += 1

    if data_row_counter >= 3:
        target_table = table
        break

header_cells = target_table.find_all("th")
headers = []

if header_cells:
    for th in header_cells:
        headers.append(th.get_text().strip())
else:
    # If no headers, build generic ones based on first data row
    first_data = target_table.find_all("tr")[0].find_all(["td", "th"])
    headers = [f"col{i+1}" for i in range(len(first_data))]

# 3. Extract data rows and pad missing values
rows = target_table.find_all("tr")
table_data = []

for r in rows:
    cells = r.find_all(["td", "th"])
    if cells:
        row_values = [c.get_text().strip() for c in cells]
        # Pad the row if it has fewer cells than headers
        while len(row_values) < len(headers):
            row_values.append("")
        table_data.append(row_values)

print(table_data)

with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for row in table_data:
        writer.writerow(row)
