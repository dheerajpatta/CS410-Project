# -*- coding: utf-8 -*-
# had some problems with ASCII and UTF-8 so did the following 3 line to fix it
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import string
import random
from itertools import islice
from collections import Counter
import pandas as pd
import nltk
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
import pickle
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

def tokList(doc):
    toks = []
    cnt = 0
    for d in doc:
        cnt = cnt +1
        dd = lower_tokenizer(d)
        toks.append(dd)
    return toks

#reading dataset
yelp = pd.read_csv('yelp-csv.csv')
x1 = yelp["text"]
xx = tokList(x1[:1000])
yy = yelp["topic"]

trainX = zip(xx,yy)


# loading training data
goods_tt = [word.strip('\n') for word in open('goods.txt').readlines()]
service_tt = [word.strip('\n') for word in open('service.txt').readlines()]
tt =goods_tt + service_tt

fullDist = [word.strip('\n') for word in open('popular1.txt').readlines()]
fullDist_ = fullDist[:500]


featuresets = [(featuresToFind(rev,fullDist_), category) for (rev, category) in trainX]


yelp_train = featuresets[:50]
yelp_test = featuresets[50:100]

classifier = nltk.NaiveBayesClassifier.train(yelp_train)
print("Classifier accuracy: ",(nltk.classify.accuracy(classifier, yelp_test)))
classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(yelp_train)
print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, yelp_test))
