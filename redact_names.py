import pandas as pd
import nltk
import os
PROXY = ""
os.environ["HTTP_PROXY"]  = PROXY
os.environ["HTTPS_PROXY"] = PROXY


# redact proper names and company names using nltk
def names(df):
    nltk.set_proxy(None)
    #nltk.download()

    # print('\nTag each row sentences\n')
    tagged_sentences = []
    for text in range(len(df)):
        sentence = df.iloc[text]
        # print('sentence\n', sentence)
        tagged_sentences.append(nltk.tag.pos_tag(sentence.split()))
        # print('tagged_sentences\n', tagged_sentences[text])

    # print('\nEdit each row sentences\n')
    edited_sentences = []
    for sentence in range(len(tagged_sentences)):
        edited_sentence = []
        for word, tag in tagged_sentences[sentence]:
            if tag == 'NNP' or tag == 'NNPS' or tag == 'NNS':
                edited_sentence.append('xxx')
            else:
                edited_sentence.append(word)

        edited_sentences.append(str(' '.join(edited_sentence)))
        # print('edited_sentences\n', edited_sentences)

    return pd.Series(edited_sentences)

######################### Test
##############################

# Texts = ["they work at Microsoft, and my name is Sami", "Google CEO is Sunder Pichai"]
# data = pd.Series(Texts)
# print(names(data))
