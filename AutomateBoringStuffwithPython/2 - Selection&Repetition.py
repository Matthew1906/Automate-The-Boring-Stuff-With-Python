name = "bob"

if name == "alice":
    print("Hi alice")
    #indentation matters in python
elif name =="bob":
    print("Hi Bob, i'm looking for alice")
else:
    print("You're not alice")
print("done")

test = 0

while test<5:
    test+=1
    if(test%2==0):
        continue
    print("test "+ str(test))

name = ""
while(len(name)<10):
    name = input("What is your name? ")
print(name)

# there is no do while

newName =""
while True: #HARUS KAPITAL
    newName = ""
    newName = input("what is your name? ")
    if len(newName)>=10:
        break
print(newName)

#for loop

for i in range(10):
    print("tester "+ str(i))

total = 0
for num in range(101):
    total+=num
print(total)

string = "apple"
for letter in string:
    print(letter)

for j in range(100,10,-10):
    print(j)