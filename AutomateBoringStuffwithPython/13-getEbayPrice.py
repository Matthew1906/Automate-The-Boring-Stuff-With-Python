import bs4,requests, sys, pyperclip

def getEbayProduct(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    element = soup.select('#vi-lkhdr-itmTitl')
    return element[0].text.strip()

def getEbayPrice(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    element = soup.select('#mm-saleDscPrc')
    return element[0].text.strip()

if len(sys.argv)>1:
    url = sys.argv[1]
else:
    url = pyperclip.paste()
    
name = getEbayProduct(url)
price = getEbayPrice(url)
print("The price of " +name+" is "+price)