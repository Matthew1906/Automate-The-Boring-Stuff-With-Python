spam = ['cat','bat','rat','elephant']

print(spam)
spam[1] = 'apple'
print(spam)

spam.append(['apple', 'orange','mango', 'grapefruit'])
print(spam[4][2])

# print with negative index = from length of list

#slicing with 2 arguments
print(spam[1:3])
#slicing with 3 arguments
print(spam[::2])

rangeList = list(range(0,100,3))
#range is an iterable 
#using range into list of integers

pencilcase = ['pencil','pen','table','notebook']

for i in range(len(pencilcase)):
    print (pencilcase[i])

for i in pencilcase:
    print(i)

#multiple assignments

pencil,pen,table,notebook = pencilcase
print(pencil)

print(pencilcase.index("table"))

#if index to high, it will append them
pencilcase.insert(8,'throwing-stars')
pencilcase.append('stapler')

#must be of similar data type
pencilcase.sort()
print(pencilcase)

pencil = "apple"
print(pencilcase)

import copy
# deepcopy => create a specific different list of
spam = pencilcase.copy()
spam[1] ="apple"
spam2 = copy.deepcopy(spam)
spam2[1] = "orange"
print(spam)
print(spam2)
print(pencilcase)