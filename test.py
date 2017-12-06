# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import string
from itertools import islice
from collections import Counter
import pandas as pd
import nltk
from nltk.stem import PorterStemmer


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


yelp = pd.read_csv('yelp.csv')

X = yelp['text']
yelp_train = X[:1000]
train_s = ""

for i in yelp_train:
    train_s = train_s + i


train_tok = lower_tokenizer(train_s)
train_w = Counter(train_tok)
top = train_w.most_common(300)

with open('popular.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in top))
fp.close()
