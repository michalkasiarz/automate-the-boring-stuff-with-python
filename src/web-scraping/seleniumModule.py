from selenium import webdriver

# Selenium  module

# setting up a driver
browser = webdriver.Firefox()

# navigating to a webpage
browser.get("https://www.automatetheboringstuff.com")

# finding chapter 0
elem = browser.find_element_by_css_selector(".main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)")

# clicking on chapter 0 link
elem.click()

# looking for p elements
elems = browser.find_elements_by_css_selector("p")
print(len(elems))

# navigating to Google.com
browser.get("https://www.google.com")

# locating google searchbar
googleSearchbar = browser.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")

# filling text into a searchbar
googleSearchbar.send_keys("Automate the Boring Stuff with Python")

# submitting the search
googleSearchbar.submit()

# navigating back
browser.back()

# navigating forward
browser.forward()

# closing the browser
browser.close()
