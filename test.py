# -*- coding: utf-8 -*-
# had some problems with ASCII and UTF-8 so did the following 3 line to fix it
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import string
from itertools import islice
from collections import Counter
import pandas as pd
import nltk
from nltk.stem import PorterStemmer

# lower_tokenizer will tokenize, lowercase each word, remove stop_words, and stem them
def lower_tokenizer(text):
    tok = nltk.word_tokenize(text)
    token = [t.decode('utf8') for t in tok]
    token = [t.lower() for t in tok]
    stop_words = [word.strip('\n') for word in open('stopwords.txt').readlines()]
    ps = PorterStemmer()
    content = []
    for t in token:
        if t not in stop_words:
            content.append(t)
    final_w = [ps.stem(t) for t in content]
    return final_w

#reading dataset
yelp = pd.read_csv('yelp.csv')
yelp['user topic'] = ' '
yelp.to_csv('yelp.csv')

#only interested in the 'text' since it the comments
X = yelp['text']

#grabbing the first 1k comments
yelp_train = X[:1000]
train_s = ""

#all comments are going in one huge string, since it is for training
for i in yelp_train:
    train_s = train_s + i

#Tokinging the training corpus
train_tok = lower_tokenizer(train_s)

#Counting all the words
train_w = Counter(train_tok)
top = train_w.most_common()
with open('popular.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in top))
fp.close()
with open('popular1.txt', 'w') as fp:
    fp.write('\n'.join(x[0] for x in top))
fp.close()
