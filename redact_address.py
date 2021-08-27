import re
import pandas as pd
from functools import reduce
from itertools import product
import nltk
import os
PROXY = ""
os.environ["HTTP_PROXY"]  = PROXY
os.environ["HTTPS_PROXY"] = PROXY

# All other function works fully with Series, except this one, it uses a dataframe
def address(df):

    data = pd.DataFrame(columns=['Text'], data=df)

    # Identifies the address but also adds extra text.
    # returns addresses with a few extra characters
    def addy(x):
        mi = re.findall(r'\d+?[A-Za-z\-\,\ \d+]{4,}', x)
        return mi
    ####################### Test addy
    # x = "I liked their services 22000 moross rd, detroit MI 48236"
    # w = addy(x)
    # print(w)

    # Cleans up addy and limits the additional data that is identified as part of the address.
    def addy2(w):
        gm = re.sub(r'(\d\w+\b)\s+\b(\w+)\b\s+(\w+)\s+\b\D+$', r'\1 \2 \3', w)
        return gm
    ###################### Test addy2
    #print(addy2(w[0]))


    # Get the exact address's
    data['addressadd']  = data['Text'].apply(addy)
    data['addressadd2'] = data['addressadd'].map(lambda x: [addy2(i) for i in x])
    #print(data)

    # Replace the addresses from the data set.
    # reduce() applies the lambda function in a loop to compute the cumulative sum of the items in numbers.
    # The lambda function takes two arguments and returns their sum. numbers = [1, 2, 3, 4] reduce(lambda a, b: a + b, numbers)
    # itertools.product() is used to find the cartesian product from the given iterator. arr1 = [1, 2] arr2 = [5, 6] list(product(arr1, arr2)) => [(1, 5), (1, 6), (2, 5), (2, 6)], therefore if we have strings each char of the first string will be multiplied by the chars of the other
    # The use of list comprehension and mapping functions to eliminate the need to explicitly create loops and to increase speed.
    # Full Explanation
    # we use apply to go throughthe the whole series. going through the whole series we apply reduce
    data['Redacted_Address'] = data.apply(lambda x: reduce(lambda a, r: a.replace(*r),list(product(x['addressadd2'], ['xxx'])), # this is part of the second lambda
                                                           x['Text']), axis=1) # this is part of the first lambda
                                                           # reduce(lambda a, b: a + b, numbers)
    return pd.Series(data['Redacted_Address'])


############################################### Test
####################################################

# # Here, by combining regex with list comprehension and a few mapping functions, we are able to identify and remove several different address formats from a data set.
# Texts = ["I had an ok experience and I live close by 2000 Vernier rd grosse pointe woods MI 48236. I had a good time at 2999 vernier",
#          "I used to know someone who lived at, 2025 magna rd grosse pointe MI 48237 they loved it and told us many cool stories about the lake",  "I liked their services 22000 moross rd, detroit MI 48236", "lots of diverse life experiences at 6233 orlina st, apt 1001, detroit MI 48217",
#          "2013 1st ambonstreet", "245e ousterkade 9", "oh yeah, I had a great time at 20225 Liverni a really really good time" ]
# data = pd.Series(Texts)
# print(address(data))
