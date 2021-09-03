import pandas as pd
from time import sleep

import redact_address
import redact_numerics
import redact_emails
import redact_names
import redact_urls
import redact_datetime

# Texts = [
#          'I had an ok experience and I live close by 2000 Vernier rd grosse pointe woods MI 48236. I had a good time at 2999 vernier',
#          'I used to know someone who lived at, 2025 magna rd grosse pointe MI 48237 they loved it and told us many cool stories about the lake',
#          'I liked their services 22000 moross rd, detroit MI 48236", "lots of diverse life experiences at 6233 orlina st, apt 1001, detroit MI 48217',
#          '2013 1st ambonstreet", "245e ousterkade 9", "oh yeah, I had a great time at 20225 Liverni a really really good time',
#          '1231451469', '42.2', '123 145 1469', '123.145.1469', '(123) 145.1469', '(123) 145 1469',
#          '(123) 145–1469', '123–145–1469', '+1(123) 145–1469 ', '1234567890999111', '123HELLO56',
#          '-123', '04/04/1998', 'it’s015–96–0342 you know my number call me', '+123–145–1469',
#          '48236–123', 'I live close to (42.293564, -83.638916)', '123-4-5648', '1-234-5-6789',
#          'I used these two email mouafek.ayadi@esprit.tn, moufak.ayadi@oddo-bhf.com',
#          'this is another email afek.aadi@esit.com',
#          'they work at Microsoft, and my name is Sami',
#          'Google CEO is Sunder Pichai',
#          'http://url.com','http://www.url.com/',
#          'https://url.com/bla3/blah3/', 'www.google.com',
#          'I eat potato at 05:30 PM and im happy, then i eat again at 10:12 AM',
#          '2018-03-14 06:08:18, he went on 2018-03-15 06:08:18,2018-03-15 slkfldfjezli'
#     ]
#
# print(redact_address.address(pd.Series(Texts)))
# print(redact_numerics.numerics(pd.Series(Texts)))
# print(redact_emails.email(pd.Series(Texts)))
# print(redact_names.names(pd.Series(Texts)))
# print(redact_urls.urls(pd.Series(Texts)))
# print(redact_datetime.datestimes(pd.Series(Texts)))


def redact(data):

    # Redaction
    original_text = data

    print('Redact Dates and Times...')
    data = redact_datetime.datestimes(data)
    sleep(1)
    print('Redact Address...')
    data = redact_address.address(data)
    sleep(1)
    print('Redact Numerics...')
    data = redact_numerics.numerics(data)
    sleep(1)
    print('Redact Emails...')
    data = redact_emails.email(data)
    sleep(1)
    print('Redact Names...')
    data = redact_names.names(data)
    sleep(1)
    print('Redact Urls...')
    data = redact_urls.urls(data)
    sleep(1)

    df = pd.DataFrame(columns=['Original', 'Redacted'])
    df['Original'] = original_text
    df['Redacted'] = data

    return data

############################################ Test
#################################################

# The following is a simulated dataset that have address, sensitive numerics, emails and entity names.
# Texts = [
#          'I had an ok experience and I live close by 2000 Vernier rd grosse pointe woods MI 48236. I had a good time at 2999 vernier',
#          'I used to know someone who lived at, 2025 magna rd grosse pointe MI 48237 they loved it and told us many cool stories about the lake',
#          'I liked their services 22000 moross rd, detroit MI 48236", "lots of diverse life experiences at 6233 orlina st, apt 1001, detroit MI 48217',
#          '2013 1st ambonstreet", "245e ousterkade 9", "oh yeah, I had a great time at 20225 Liverni a really really good time',
#          '1231451469', '42.2', '123 145 1469', '123.145.1469', '(123) 145.1469', '(123) 145 1469',
#          '(123) 145–1469', '123–145–1469', '+1(123) 145–1469 ', '1234567890999111', '123HELLO56',
#          '-123', '04/04/1998', 'it’s015–96–0342 you know my number call me', '+123–145–1469',
#          '48236–123', 'I live close to (42.293564, -83.638916)', '123-4-5648', '1-234-5-6789',
#          'I used these two email mouafek.ayadi@esprit.tn, moufak.ayadi@oddo-bhf.com',
#          'this is another email afek.aadi@esit.com',
#          'they work at Microsoft, and my name is Sami',
#          'Google CEO is Sunder Pichai',
#          'http://url.com','http://www.url.com/',
#          'https://url.com/bla3/blah3/', 'www.google.com',
#          'I eat potato at 05:30 PM and im happy, then i eat again at 10:12 AM',
#          '2018-03-14 06:08:18, he went on 2018-03-15 06:08:18,2018-03-15 slkfldfjezli'
#     ]
# print(redact(pd.Series(Texts)).values)


