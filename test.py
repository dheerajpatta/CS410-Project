"""
This is a tutorial from:
https://medium.com/tensorist/classifying-yelp-reviews-using-nltk-and-scikit-learn-c58e71e962d9
"""
import json
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report

import nltk
from nltk.corpus import stopwords


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
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


yelp = pd.read_csv('yelp.csv')

X = yelp['text']
yelp_train = X[:1000]
train_s = []
for i in yelp_train:
    if i == 0:
        train_s = text_process(yelp_train[i])
    else:
        train_s = train_s + text_process(yelp_train[0])

train_w =nltk.FreqDist(train_s)
print(train_w.most_common(2000))
