# record custom message

import logging
logging.basicConfig(filename="12.5.5- loggingDebug",level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
# better than print (because we need to delete them)
# commment everything instantly
logging.disable(logging.DEBUG)#DISABLE FROM DEBUG LEVEL AND BELOW
# five levels of logging (different priorities)
'''
    DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
'''
logging.debug('start of program')
def factorial(n):
    logging.debug('start of factorial(%s)'%(n))
    total = 1
    for i in range(1,n+1):
        total*=i
        logging.info('i is %s, total is %s'%(i,total))
    return total

print(factorial(5))
logging.debug('end of program')

