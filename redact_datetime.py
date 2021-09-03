# https://regexr.com/3iok2
import re
import pandas as pd

def datestimes(df):
    df = df.apply(lambda text: re.sub(r'\d{4}-\d{2}-\d{2}',    r'xxx', text))    # 2018-03-15
    df = df.apply(lambda text: re.sub(r'[\d ]\d:\d\d \w\w',    r'xxx', text))    # 05:30 PM
    df = df.apply(lambda text: re.sub(r'\d\d:[0-5]\d:[0-5]\d', r'xxx', text)) # 06:08:18
    return df

############################## Test
###################################

# text = "I eat potato at 05:30 PM and i'm happy, then i eat again at 10:12 AM, " \
#        "2018-03-14 06:08:18, he went on 2018-03-15 06:08:18, lets play, 2018-03-15 slkfldfjezli"
# print(datestimes(pd.Series(text)).values)




