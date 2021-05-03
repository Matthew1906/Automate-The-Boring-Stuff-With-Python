
import webbrowser, sys, pyperclip

# open a website
# webbrowser.open("https://automatetheboringstuff.com/")

# open google maps with the address
sys.argv
# Check if command line arguments were passed
if len(sys.argv)>1: # if the user inserted an address
    address = ' '.join(sys.argv[1:])
else: # assumming that it is stored in the clipboard
    address = pyperclip.paste()

url = "https://www.google.com/maps/place/"+address
webbrowser.open(url)

