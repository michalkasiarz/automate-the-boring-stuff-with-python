import bs4
import requests

# beautifulsoup4 module

# heading for The Washington Post website
res = requests.get("https://www.washingtonpost.com/")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

# selecting the present date
elems = soup.select("#edition-toggle > div > div > div.full")

# printing the date
print("Present date of The Washington Post date is " + elems[0].text + ".")
# Present date of The Washington Post date is April 2, 2020.
