#-*- coding: utf-8 -*-
# had some problems with ASCII and UTF-8 so did the following 3 line to fix it
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import string
import random
import collections
from itertools import islice
from collections import Counter
import pandas as pd
import numpy as np
import nltk
from nltk.metrics import precision, recall, f_measure
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
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

def graphThings(table,string):
    graphServ = [0,0,0,0,0]
    graphGood = [0,0,0,0,0]
    for i,t in enumerate(table):
        if t[3] == 5:
            if t[2] =='goods':
                graphGood[4] += 1
            elif t[2] =='service':
                graphServ[4] += 1
        if t[3] == 4:
            if t[2] =='goods':
                graphGood[3] += 1
            elif t[2] =='service':
                graphServ[3] += 1
        if t[3] == 3:
            if t[2] =='goods':
                graphGood[2] += 1
            elif t[2] =='service':
                graphServ[2] += 1
        if t[3] == 2:
            if t[2] =='goods':
                graphGood[1] += 1
            elif t[2] =='service':
                graphServ[1] += 1
        if t[3] == 1:
            if t[2] =='goods':
                graphGood[0] += 1
            elif t[2] =='service':
                graphServ[0] += 1
    style.use("ggplot")
    fig, ax = plt.subplots()
    index = np.arange(5)
    bar_width = 0.35
    opacity = 0.4

    rectGoods = ax.bar(index,graphGood, bar_width, alpha=opacity,color='b', label="Goods")
    rectServ = ax.bar(index + bar_width,graphServ, bar_width, alpha=opacity,color='r', label="Service")

    ax.set_xlabel('Stars')
    ax.set_ylabel('Number of Comments')
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(('1','2','3','4','5'))
    ax.set_title('Yelp Review Classification')
    ax.legend(bbox_to_anchor=(0.5,1),loc=0,borderaxespad=0.)
    #ax.legend()
    #fig.tight_layout()
    plt.rcParams
    plt.savefig(string)



#reading dataset
yelp = pd.read_csv('yelp-csv.csv')
x1 = yelp["text"]
xx = tokList(x1[:1000])
yy = yelp["topic"]
sStars = yelp['stars']
trainX = zip(xx,yy[:1000])

# loading training data

fullDist = [word.strip('\n') for word in open('popular1.txt').readlines()]
fullDist_ = fullDist[:1000]

featuresets = [(featuresToFind(rev,fullDist_), category) for (rev, category) in trainX]

#random.shuffle(featuresets[:100])
yelp_train = featuresets[:225]
yelp_test = featuresets[225:400]

classifier = nltk.NaiveBayesClassifier.train(yelp_train)
refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

csObserved = []
for i, (feats, label) in enumerate(featuresets):
    refsets[label].add(i)
    observed = classifier.classify(feats)
    csObserved.append(observed)
    testsets[observed].add(i)

dataO = trainX[:400]
dataOO = zip(x1[:400],yy[:400],csObserved,sStars[:400])

print("Naive Bayes Classifier accuracy: ",(nltk.classify.accuracy(classifier, yelp_test)))
print("Precision of goods:", (precision(refsets['goods'], testsets['goods'])))
print("Recall of goods:", (recall(refsets['goods'], testsets['goods'])))
print("Fmeasure of goods:", (f_measure(refsets['goods'], testsets['goods'])))
print("Precision of service:", (precision(refsets['service'], testsets['service'])))
print("Recall of service:", (recall(refsets['service'], testsets['service'])))
print("Fmeasure of service:", (f_measure(refsets['service'], testsets['service'])))

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(yelp_train)
cssObserved = []
for i, (feats, label) in enumerate(featuresets):
    refsets[label].add(i)
    observed = LinearSVC_classifier.classify(feats)
    cssObserved.append(observed)
    testsets[observed].add(i)
dataOO0 = zip(x1[:400],yy[:400],cssObserved,sStars[:400])

print ""
print("LinearSVC Classifier accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, yelp_test)))
print("Precision of goods:", (precision(refsets['goods'], testsets['goods'])))
print("Recall of goods:", (recall(refsets['goods'], testsets['goods'])))
print("Fmeasure of goods:", (f_measure(refsets['goods'], testsets['goods'])))
print("Precision of service:", (precision(refsets['service'], testsets['service'])))
print("Recall of service:", (recall(refsets['service'], testsets['service'])))
print("Fmeasure of service:", (f_measure(refsets['service'], testsets['service'])))
graphThings(dataOO,"naivebayes.png")
graphThings(dataOO0,"LinearSVC.png")


#sentiment analysis
print "\n", "Sentiment Analysis: \n"

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

refsetsS = collections.defaultdict(set)
testsetsS = collections.defaultdict(set)
classifier = nltk.NaiveBayesClassifier.train(yelpS_train)
for i, (feats, label) in enumerate(Sfeaturesets):
    refsetsS[label].add(i)
    observed = classifier.classify(feats)
    testsetsS[observed].add(i)

print("Naive Bayes Classifier accuracy: ",(nltk.classify.accuracy(classifier, yelpS_test)))
print("Precision of pos:", (precision(refsetsS['pos'], testsetsS['pos'])))
print("Recall of pos:", (recall(refsetsS['pos'], testsetsS['pos'])))
print("Fmeasure of pos:", (f_measure(refsetsS['pos'], testsetsS['pos'])))
print("Precision of neu:", (precision(refsetsS['neu'], testsetsS['neu'])))
print("Recall of neu:", (recall(refsetsS['neu'], testsetsS['neu'])))
print("Fmeasure of neu:", (f_measure(refsetsS['neu'], testsetsS['neu'])))
print("Precision of neg:", (precision(refsetsS['neg'], testsetsS['neg'])))
print("Recall of neg:", (recall(refsetsS['neg'], testsetsS['neg'])))
print("Fmeasure of neg:", (f_measure(refsetsS['neg'], testsetsS['neg'])))

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(yelpS_train)
for i, (feats, label) in enumerate(Sfeaturesets):
    refsetsS[label].add(i)
    observed = LinearSVC_classifier.classify(feats)
    testsetsS[observed].add(i)
print "\n"
print("LinearSVC Classifier accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, yelpS_test)))
print("Precision of pos:", (precision(refsetsS['pos'], testsetsS['pos'])))
print("Recall of pos:", (recall(refsetsS['pos'], testsetsS['pos'])))
print("Fmeasure of pos:", (f_measure(refsetsS['pos'], testsetsS['pos'])))
print("Precision of neu:", (precision(refsetsS['neu'], testsetsS['neu'])))
print("Recall of neu:", (recall(refsetsS['neu'], testsetsS['neu'])))
print("Fmeasure of neu:", (f_measure(refsetsS['neu'], testsetsS['neu'])))
print("Precision of neg:", (precision(refsetsS['neg'], testsetsS['neg'])))
print("Recall of neg:", (recall(refsetsS['neg'], testsetsS['neg'])))
print("Fmeasure of neg:", (f_measure(refsetsS['neg'], testsetsS['neg'])))
