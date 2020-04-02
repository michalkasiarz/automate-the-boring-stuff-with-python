import bs4
import requests

# beautifulsoup4 module

# heading for The Washington Post website
res = requests.get("https://www.washingtonpost.com/")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

# selecting the present date
elems = soup.select("#edition-toggle > div > div > div.full")
print(elems[0].text)
