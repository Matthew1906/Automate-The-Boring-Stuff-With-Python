# 1. REGEX BASIC

''' 
    ctrl-f => search
    regex = mini language to specify text patterns
    we can use regex to search text patterns
    most apps (word, docs, etc.) already have regular expressions
'''

# US or Canada phone number: xxx-xxx-xxxx
def isPhoneNumber(text):
    if len(text)!=12:
        return False
    elif not text[0:3].isdecimal():
        return False
    elif text[3]!='-' or text[7]!='-':
        return False
    elif not text[4:7].isdecimal():
        return False
    elif not text[8:].isdecimal():
        return False
    else:
        return True

print(isPhoneNumber("444-444-4444"))

'''
However in text sometimes we need to search for the string
which makes it hard, and tiring to just search it one by one
Below is an example code of looking for phone number in a string
'''

message = " Call me at 415-555-1011 tomorrow, or at 134-123-8977"

# Without RegEx
foundNumber = False
for i in range(len(message)):
    chunk  = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone Number found!")
        foundNumber = True
        break
if not foundNumber:
    print("Couldn't find phone number")

''' 
    Using Regular Expressions, we can make the pattern matching significantly shorter
'''
# With RegEx
import re
phoneRegex = re.compile(r'[\d]{3}-[\d]{3}-[\d]{3}')#use raw string because there are lots of backslashes
firstMatched = phoneRegex.search(message) #find first occurence
allMatched = phoneRegex.findall(message) #find all occurence
print(firstMatched.group())#returns object (class)
print(allMatched)# returns list of string


# 2. GROUPS AND PIPE CHARACTERS

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
res = phoneRegex.search(message)
print(res.group(1))
print(res.group(2))

# pipe character  = |
batRegex = re.compile(r'Bat(motor|motorcycle|copter|bat)')
# check also based on who goes first in the pipe group
res = batRegex.findall('Batmotorcycle lost a wheel')
print(res)
# group(0) or group() returns full matching string
# others are based on the groups available
# | can match one of many possible groups based on who goes first

# REPETITION AND GREEDY/NONGREEDY MATCHING

# matching a specific number of repetitions

# ? = zero or once

batRegex = re.compile(r'Bat(wo)?man')
res = batRegex.search("The Adventures of Batman")
print(res.group())
res = batRegex.search("The adventures of Batwoman")
print(res.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
res = phoneRegex.search("My phone number is 431-222-2345")
print(res.group())
#puts area code into groups
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
res = phoneRegex.search("My phone number is 222-2345")
print(res.group())

# * = zero or more
batRegex = re.compile(r'Bat(wo)*man')
res = batRegex.search("The adventures of Batwowowowowowowowowowowowoman")
print(res.group())

# + = one or more
batRegex = re.compile(r'Bat(wo)+man')
res = batRegex.search("The adventures of Batman")
if res==None:
    print("None")
else:
    print(res.group())# error because there are no match

# repetitions use {} 
# 3 to 5 Ha
laughRegex = re.compile(r'(Ha){3,5}')
# we can leave the first or second number, creating limitless bounds
# Greedy Match = match longest posible string
res = laughRegex.search("HaHaHaHa")
print(res.group())

# non greedy match
laughRegex = re.compile(r'(Ha){3,5}?')
# match smallest possible string
res = laughRegex.search("HaHaHaHa")
print(res.group())

# CHARACTER CLASSES AND FINDALL()

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
laughRegex = re.compile(r'(Ha){3,5}')
res = laughRegex.findall("HaHaHaHaHaHaHaHaHa")
# found HaHaHaHaHa and HaHaHaHa
print(res) # result = Ha, Ha
# if there are multiple groups, the find all will match group 0, group 1, group2, .... group n

# ^ none of what's inside
newRegex = re.compile(r'[^a-z]')
res = newRegex.findall("abcdefghijk123239")
print(res)

# REGEX DOT START AND CARET/DOLLAR CHARACTERS

beginsWithHello = re.compile(r'^Hello')
res = beginsWithHello.search("Hello There")
print(res.group())

endsWithBye = re.compile(r'Bye$')
res = endsWithBye.search("GoodBye")
print(res.group())

# . = any character except newline

atRegex = re.compile(r'.*at')
res = atRegex.findall("the cat in the hat sat on the flat mat")
print(res)

# .* anything

name = "First Name: Matthew Last Name: AM1906"
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
res = nameRegex.findall(name)
print(res)

allThings = re.compile(r'.*', re.DOTALL)
res = allThings.findall("Name\napa\n\n")
print(res)

newRegex = re.compile(r'[a-z]', re.IGNORECASE)
res = newRegex.findall("abcdefghijk123239ABCD")
print(res)

# SUB and VERBOSE

codedMessage = "Agent Alice gave the secret documents to Agent Mike"
agentRegex = re.compile(r'Agent \w+')
res = agentRegex.findall(codedMessage)
print(res)

# SUB = SUBSTITUTION

res = agentRegex.sub('REDACTED', codedMessage)
print(res)

agentRegex = re.compile(r'Agent (\w)\w+')
res = agentRegex.findall(codedMessage)
print(res)
res = agentRegex.sub(r'Agent \1', codedMessage)
print(res)

# VERBOSE -> HELPS A LOT TO IMPROVE READABILITY
phoneRegex = re.compile(r'''
\d\d\d #area code
- #dash
\d\d\d # first 3 digits
- # dash
\d\d\d\d # last 4 digits
''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
# use pipe character -> bitwise



