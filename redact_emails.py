import re
import pandas as pd

def email(df):

    return pd.Series(df.apply(lambda text: re.sub("\S+@\S+", r'xxx', text)))

# #################################### Test
# #########################################
#
# Texts = ["I used these two email mouafek.ayadi@esprit.tn, moufak.ayadi@oddo-bhf.com", "this is another email afek.aadi@esit.com" ]
# data = pd.Series(Texts)
# print(email(data))
