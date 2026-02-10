# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 7

# Import packages needed for website scraping
import requests
from bs4 import BeautifulSoup

# Store the Wikipedia URL as a sting
wikipedia_url = "https://en.wikipedia.org/wiki/Data_science"

# Set these headers so that Wikipedia can allow us to scrape from their website
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; HarrisKhanBot/1.0; +https://example.com/contact)"
}

# Store the contents of the wikipedia article here
contents_of_wikipedia_article = requests.get(wikipedia_url, headers=headers)

# Allows us to 'parse' or analyze the contents of the wikipedia article
wikipedia_article_parser = BeautifulSoup(contents_of_wikipedia_article.text, 'html.parser')

# Find the title tag of the wikipedia article using beautiful soup
title_of_wiki_article = wikipedia_article_parser.find("title")

# Print out the title of the wikipedia article
print("Title of Wikipedia Article:")
print(title_of_wiki_article.get_text())

# Use beautiful soup to find the main article content
content_div = wikipedia_article_parser.find("div", id="mw-content-text")

# Find all paragraphs inside the main content using the paragraphs tag
paragraphs_in_wiki_article = content_div.find_all("p")

# Create an empty string variable to hold the value of the first valid paragraph in the article
first_valid_paragraph_in_wiki_article = ""

# Loop through each paragraph until we find a paragraph with >= 50 characters
for paragraph in paragraphs_in_wiki_article:

    # Get the text of the paragraph and store it in this variable
    text_of_paragraph = paragraph.get_text()

    # If the text of the paragraph after being stipped of whitespace is greater than or equal to 50
    if len(text_of_paragraph.strip()) >= 50:
        # Set our first valid paragraph in the article to the text of the current paragraph
        first_valid_paragraph_in_wiki_article = text_of_paragraph

        # Break the for loop now that we have found our first valid paragraph
        break

# Print the first valid paragraph that is greater than or equal to 50 characters
print("\nFirst Paragraph of Wikipedia Article (Greater than or Equal to 50 Characters):")
print(first_valid_paragraph_in_wiki_article)

