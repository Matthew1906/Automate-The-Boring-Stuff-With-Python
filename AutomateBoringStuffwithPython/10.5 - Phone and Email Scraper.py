import re, pyperclip

# 1. CREATE REGEX OBJECT FOR PHONE NUMBERS AND EMAIL ADDRESS
phoneRegex = re.compile(r'''(
(\d\d\d | (\(\d\d\d))? #area code
(-|\s){1}#separator
([\d]{3}
-
[\d]{4} )# last 4 numbers
(\s*((ext(\.)?)|x)? # word part
\s(\d){2,5})?)# number part
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ #name part
@ # @ symbol
[a-zA-Z0-9_.+]+ # domain name
''',re.VERBOSE)

# 2. GET TEXT OFF THE CLIPBOARD
text = pyperclip.paste()

# 3. EXTRACT THE EMAIL, PHONE FROM THIS TEXT
phoneMatches = phoneRegex.findall(text)
emailMatches = emailRegex.findall(text)

# 4. CLEAN THE RESULTS
phoneResults = []
for i in phoneMatches:
    phoneResults.append(i[0])

phoneResults = "\n".join(phoneResults)

emailResults = []
for i in emailMatches:
    emailResults.append(i)
emailResults = "\n".join(emailResults)

combinedResults = 'All Phone Numbers:\n' + phoneResults +'\n\nAll Emails:\n'+ emailResults

# 5. PUT INTO CLIPBOARD
pyperclip.copy(combinedResults)