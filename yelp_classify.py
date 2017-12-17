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
import nltk.metrics
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
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

trainX = zip(xx,yy[:1000])

# loading training data
goods_tt = [word.strip('\n') for word in open('goods.txt').readlines()]
service_tt = [word.strip('\n') for word in open('service.txt').readlines()]
tt =goods_tt + service_tt

fullDist = [word.strip('\n') for word in open('popular1.txt').readlines()]
fullDist_ = fullDist[:1000]

featuresets = [(featuresToFind(rev,fullDist_), category) for (rev, category) in trainX]

#random.shuffle(featuresets[:100])
yelp_train = featuresets[:225]
yelp_test = featuresets[225:400]

classifier = nltk.NaiveBayesClassifier.train(yelp_train)
print("Naive Bayes Classifier accuracy: ",(nltk.classify.accuracy(classifier, yelp_test)))
#print("Precision:", (nltk.classify.precision(classifier, yelp_test)))
#classifier.show_most_informative_features(20)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(yelp_train)
print("LinearSVC Classifier accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, yelp_test)))

#sentiment analysis
print "\n", "Sentiment Analysis: \n"


sStars = yelp['stars']

ssStars = []
for s in sStars:
    if s == 5 or s == 4:
        ssStars.append("pos")
    elif s == 3:
        ssStars.append("neu")
    elif s == 2 or s == 1:
        ssStars.append("neg")

trainStars = zip(xx, ssStars[:1000])

#print trainStars[999:1000]
Sfeaturesets = [(featuresToFind(rev,fullDist_), category) for (rev, category) in trainStars]
yelpS_train = Sfeaturesets[:500]
yelpS_test = Sfeaturesets[500:1000]

classifier = nltk.NaiveBayesClassifier.train(yelpS_train)
print("Naive Bayes Classifier accuracy: ",(nltk.classify.accuracy(classifier, yelpS_test)))

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(yelp_train)
print("LinearSVC Classifier accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, yelp_test)))
