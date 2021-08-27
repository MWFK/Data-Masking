import re
import pandas as pd

# To find and replace all sensitive numbers (phone numbers, ssn, latitude and longitude coordinates, some zipcodes)
# in the data frame by xxx we can create a function such as below:
def sensitive_numerics(number):
    number = re.sub(r'[\+\(]?\d[\d .\-\(\)]{6,}', r'xxx', number)
    # [0-9] matches a single digit in the range 0 through 9 (inclusive), {4} indicates that four such digits should occur in a row,
    # - means a hyphen, and | means an OR and separates the two patterns you mention.
    # '123-4-5648' '1-234-5-6789'
    number = re.sub('[0-9]-[0-9]{3}-[0-9]-[0-9]{4}|[0-9]{3}-[0-9]-[0-9]{4}', 'xxx', number)
    return number

def numerics(data):

    return pd.Series(data.apply(sensitive_numerics))

############################################# Test
##################################################

# Texts = ['1231451469', '42.2', '123 145 1469', '123.145.1469', '(123) 145.1469', '(123) 145 1469',
#          '(123) 145–1469', '123–145–1469', '+1(123) 145–1469 ', '1234567890999111', '123HELLO56',
#          '-123', '04/04/1998', 'it’s015–96–0342 you know my number call me', '+123–145–1469',
#          '48236–123', 'I live close to (42.293564, -83.638916)', '123-4-5648', '1-234-5-6789']
# data = pd.Series(Texts)
# print(numerics(data))
