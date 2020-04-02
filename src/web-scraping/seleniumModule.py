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
