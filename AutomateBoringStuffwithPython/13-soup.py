# WEB SCRAPING = programs that pull information out of webpages

# locate text , we can parse using beautiful soup

import bs4
import requests

# retrieve price from website
res = requests.get("https://www.ebay.com/itm/123662580942")
res.raise_for_status()

# second parameter = avoid warnings
soup = bs4.BeautifulSoup(res.text,"html.parser")

# select the selector of the price in the website
element = soup.select('#mm-saleDscPrc')

print(element[0].text.strip())

