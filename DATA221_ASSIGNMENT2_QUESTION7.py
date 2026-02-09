# Harris Khan
# February 7, 2026
# DATA221, Assignment 2, Question 7

# Import packages needed for website scraping
import requests
from bs4 import BeautifulSoup

wikipedia_url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; HarrisKhanBot/1.0; +https://example.com/contact)"
}

contents_of_wikipedia_article = requests.get(wikipedia_url, headers=headers)
soup = BeautifulSoup(contents_of_wikipedia_article.text, 'html.parser')

title = soup.find("title").get_text()
print(title)

# Find the main article content
content_div = soup.find("div", id="mw-content-text")

# Find the first paragraph inside that div
first_paragraph = content_div.find("p")

print(first_paragraph.get_text(strip=True))
