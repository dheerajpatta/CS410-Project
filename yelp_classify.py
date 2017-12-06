# -*- coding: utf-8 -*-
# had some problems with ASCII and UTF-8 so did the following 3 line to fix it
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import string
import random
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

def featuresToFind(doc, gsWords):
    words = set(doc)
    features = {}
    for w in gsWords:
        features[w] = (w in words)
    return features


#reading dataset
yelp = pd.read_csv('yelp-csv.csv')

#only interested in the 'text' since it the comments
X = (yelp['text'],yelp['user topic'])

#grabbing the first 1k comments
yelp_= X[:1000]
yelp_train = yelp[:50]
yelp_test = yelp[50:]

# loading training data
goods_tt = [word.strip('\n') for word in open('goods.txt').readlines()]
service_tt = [word.strip('\n') for word in open('service.txt').readlines()]
tt =goods_tt + service_tt

t = [(goods_tt, 'goods') + (service_tt, 'service')]
random.shuffle(t)
#print t

"""randomDoc = lower_tokenizer(yelp_corpus[1500])
print((featuresToFind(randomDoc,tt)))
"""

#classifier = nltk.NaiveBayesClassifier.train(tt)
