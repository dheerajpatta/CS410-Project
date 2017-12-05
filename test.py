"""
This is a tutorial from:
https://medium.com/tensorist/classifying-yelp-reviews-using-nltk-and-scikit-learn-c58e71e962d9
"""
import json
import string
from itertools import islice
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.corpus import word wordnet
from nltk.tokenize import word_tokenize


def text_process(text):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in text if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)

    # Now just remove any stopwords
    #return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return [word for word in nopunc.split() if word.lower() and
                   word.decode('utf8') not in stopwords.words('english')]



yelp = pd.read_csv('yelp.csv')
o = open('token.txt', 'w+')
oo = open('popular.txt', 'w+')
X = yelp['text']
yelp_train = X[:500]
train_s = ""
print stopwords.words('english')
#print text_process(yelp_train[0]) + text_process(yelp_train[1]) + text_process(yelp_train[2])
for i in yelp_train:
    train_s = train_s + i

train_tok = text_process(train_s)
train_w = Counter(train_tok)
for word in train_s:
    o.write(word)
o.close()

top = train_w.most_common(100)
"""for word in top:
    oo.write(word)
oo.close()"""
#print(top)
