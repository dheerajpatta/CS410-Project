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

# loading training data
t = [word.strip('\n') for word in open('goods.txt').readlines()]
training = set([({word: (word in t for word in t}, x[1]) for x in train])

#only interested in the 'text' since it the comments
X = yelp['text']

#grabbing the first 1k comments
yelp_corpus = X[1000:2000]
classifier = nltk.NaiveBayesClassifier.train(training)
