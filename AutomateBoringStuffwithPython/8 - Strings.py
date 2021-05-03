# Escape sequence = \t \n \' \"
text1 = "he's here"
print(text1)
text2 = 'he\'s here'
print(text2)

# raw strings
print(r'Applebees\'product')

# multi line strings
lyrics = '''Dear future husband
Here's a few things you'll need to know if you wanna be
My one and only all my life'''
print(lyrics)

# indexes, slices, in and not in also work on strings

#conversion
string = "Hellothere"
print(string.upper())
print(string.lower())
print(string.capitalize())
print()
#checking -> for string, all of them must be True
print(string.isalnum())
print(string.isupper())
print(string.isalpha())
print(string.islower())
print(string.istitle())
print(string.isdecimal())
print(string.isspace())
# etc
print()
#starts with and ends with
print(string.startswith("Hello"))
print(string.endswith("Bye"))
print()
animals =  ["cats", "mouses","birds"]
#join method
print(" ".join(animals))
animals2 = " ".join(animals)
#split
print(animals2.split(" "))
#ljust and rjust, text alignment
print(string.ljust(12,"-"))
print(string.rjust(18,"+"))
print(string.center(14,")"))

# strip function
toStrip = string.rjust(20," ")
print(toStrip)
print(toStrip.strip())
toStrip = string.ljust(20,"=")
print(toStrip)
print(toStrip.strip("="))
toStrip = string.center(14,")")
print(toStrip)
print(toStrip.strip(")"))

# string format
name = "alice"
place = "Turnip Street"
time = "6 p.m."
food = "pizza"
print("Hello "+ name + ", You are invited to attend a party at " + place +" at "+ time +". Please bring "+ food)
print("Hello %s, you are invited to a party at %s at %s, Please bring %s"%(name, place, time ,food))


