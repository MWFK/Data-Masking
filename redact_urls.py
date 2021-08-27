# from urlextract import URLExtract
import re
import pandas as pd
import sys
sys.setrecursionlimit(1500) # after 1500 makes python kernal break

def urls(df):

    pattern1 = r'^https?:\/\/.*[\r\n]*'
    pattern2 = r'(?:http://)?\w+\.\S*[^.\s]'
    df = df.apply(lambda text: re.sub(pattern1, 'xxx', text, flags=re.MULTILINE))
    df = df.apply(lambda text: re.sub(pattern2, 'xxx', text, flags=re.MULTILINE))

    return pd.Series(df)


############################################ Test
#################################################
# #
# Texts = [
#               'http://url.com','http://www.url.com/',
#               'https://url.com/bla3/blah3/', 'www.google.com'
#     ]
# print(urls(pd.Series(Texts)))
