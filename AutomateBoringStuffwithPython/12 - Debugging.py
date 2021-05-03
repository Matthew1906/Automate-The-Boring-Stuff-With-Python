# raise your own exceptions

# raise Exception("This is the error message.")

def boxPrint(symbol, width, height):
    try:
        if len(symbol)!=1:
            raise Exception("Symbol Error")
        elif width<2 or height<2:
            raise Exception("Width or Height Error")
        print(symbol*width)
        for i in range(height-2):
            print(symbol+((" ")*(width-2))+symbol)
        print(symbol*width)
    except TypeError:
        print("Wrong Type man!")

boxPrint("$",9,9)

# the errors are shown in a traceback

# GET THE TRACEBACK STRING

import traceback
try:
    raise Exception("Error message")
except:
    errorFile = open('12.5 - errorlog.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written in errorlog.txt")

# ASSERTIONS AND THE ASSERT STATEMENT
# SANITY CHECK OF CODES

# assert False, "This is the error message"

market_2nd = {'ns':'green', 'ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key]=='green':
            intersection[key] = 'yellow'
        elif intersection[key]=='yellow':
            intersection[key] = 'red'
        elif intersection[key]=='red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red' + str(intersection)
  
print(market_2nd)    
switchLights(market_2nd)
print(market_2nd)



