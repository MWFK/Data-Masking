import pandas as pd
from time import sleep
import redact_all

Path = r'path_to_file.xlsx'

def main():

    # The following is a simulated dataset that have address, sensitive numerics, emails and entity names.
    Texts = [
        "I had an ok experience and I live close by 2000 Vernier rd grosse pointe woods MI 48236. I had a good time at 2999 vernier",
        "I used to know someone who lived at, 2025 magna rd grosse pointe MI 48237 they loved it and told us many cool stories about the lake",
        "I liked their services 22000 moross rd, detroit MI 48236",
        "lots of diverse life experiences at 6233 orlina st, apt 1001, detroit MI 48217",
        "2013 1st ambonstreet", "245e ousterkade 9",
        "oh yeah, I had a great time at 20225 Liverni a really really good time",
        '1231451469', '42.2', '123 145 1469', '123.145.1469', '(123) 145.1469', '(123) 145 1469',
        '(123) 145–1469', '123–145–1469', '+1(123) 145–1469 ', '1234567890999111', '123HELLO56',
        '-123', '04/04/1998', 'it’s015–96–0342 you know my number call me', '+123–145–1469',
        '48236–123', 'I live close to (42.293564, -83.638916)', '123-4-5648', '1-234-5-6789',
        "I used these two email mouafek.ayadi@esprit.tn, moufak.ayadi@oddo-bhf.com",
        "this is another email afek.aadi@esit.com",
        "they work at Microsoft, and my name is Sami",
        "Google CEO is Sunder Pichai",
        'http://url.com', 'http://www.url.com/',
        'https://url.com/bla3/blah3/', 'www.google.com'
        ]

    return redact_all.redact(pd.Series(Texts))


if __name__ == "__main__":
    # main()
    # print(main())

    print('Redaction Started...\n')
    sleep(1)
    data = main()
    data.to_excel(Path, sheet_name='Redacted_Data', index=False)
    print('\nRedaction Finished and Data exported successfully!')
    data.to_excel(Path, sheet_name='emails', index=False)
