import requests, bs4

urlFront = "https://xkcd.com/"
imageAddress = "./13-getPictures/image"
counter = 1

def getPicture(url,counter):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    tags = soup.find_all("div", id="comic")
    # print(tags)
    image = [f.find("img") for f in tags]
    # print(image)
    src = [img['src'] for img in image]
    # print(src)
    retrieved = requests.get("http:"+src[0])
    file = open(imageAddress+str(counter)+".png", "wb")
    file.write(retrieved.content)
    file.close()
    tag1 = soup.find('ul',{"class":"comicNav"})
    tag2 = tag1.find_all('a')
    tag3 = [a['href']for a in tag2]
    res = urlFront+tag3[1]
    return res
    
url = urlFront

# THIS CODE WILL RETRIEVE ALL PICTURES IN https://xkcd.com/ UNTIL THERE IS NO LONGER ANY PICTURES
# DO NOT EXECUTE THE PROGRAM

while True:
    res = requests.get(url)
    if res.status_code!=200 or counter>5:
        # remove the "or counter>5 if you want to download all images"
        break
    url = getPicture(url,counter)
    counter+=1
    
