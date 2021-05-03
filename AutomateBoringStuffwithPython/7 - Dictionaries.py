# dictionary data type

myCat = {'size':144, 'color':'orange'}

print(myCat)
print("My Cat's color is "+ myCat['color'])

# check keys
print('color' in myCat)

#without typecasting, it will return a tuple

#print keys
print(myCat.keys())

#print values
print(myCat.values())

#print items
print(myCat.items())

#get value get (key, fallback default value)
print(myCat.get('name', "No Name"))
# default fallback default value is None

myCat.setdefault('name',"Jackie")
print(myCat)
print(myCat['name'])

# character counter application
message = "it was a bright cold day in April, and the clocks are striking thirteen"
count = {}

for char in message.lower():
    count.setdefault(char,0)
    count[char]+=1
print(count)