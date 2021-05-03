import requests

#returns a response object
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# returns status code
print(res.status_code)

# retrieve the text (in string)
textContent = res.text

# raise an exception if there is an error
res.raise_for_status()

# badRes = requests.get('https://automatetheboringstuff.com/files/rnj.txt')
# badRes.raise_for_status()

playFile = open('13-RomeoAndJuliet.txt','wb')

# calls to save downloaded file to a hard drive
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

# requests.readthedocs.org

