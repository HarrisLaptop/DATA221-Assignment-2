# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 8

# Import packages needed for website scraping
import requests
from bs4 import BeautifulSoup

# Open a new file in write mode and call it "headings.txt"
headings_file = open("headings.txt", "w")

# Store the Wikipedia URL as a sting
wikipedia_url = "https://en.wikipedia.org/wiki/Data_science"

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

# Find all headings inside the main content using the h2 tag
headings_in_wiki_article = content_div.find_all("h2")

# Store the substring "[edit]" here in case we need to remove it from any of the headings
remove_substring = "[edit]"

# For every heading in the headings in the main content of the wiki article
for heading in headings_in_wiki_article:

    # Get the heading text and store it here
    heading_text = heading.get_text()

    # If the words "References", "External Links", "See also", and "Notes" are not in the header
    if ("References" not in heading_text
            and "External Links" not in heading_text
            and "See also" not in heading_text
            and "Notes" not in heading_text):

        # Write the headings text to the headings.txt file without the substring "[edit]"
        headings_file.write(heading_text.replace(remove_substring, "") + "\n")