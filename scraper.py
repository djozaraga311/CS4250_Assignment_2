#-------------------------------------------------------------------------
# AUTHOR: Daniel Ozaraga
# FILENAME: scraper.py
# SPECIFICATION: Uses requests, BeautifulSoup, and urljoin that crawls the Circular Links
# section of TestingURL.dev from a starting seed point.
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 1 hour
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
# --> add your Python code here
frontier = [seed]
seen = {seed} #only allows unique elements


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


    # Printing the text contained in the <h1> element
    print(soup.find("h1").get_text())


    # Extracting and processing hyperlinks
    for aTag in soup.find_all("a", href=True):
        href = aTag["href"]

        absURL = urljoin(url, href)

        if absURL.startswith(seed) and absURL not in seen:
            seen.add(absURL)
            frontier.append(absURL)


# Printing all URLs in seen
print("Visited URLs")
for visited in seen:
    print(visited)