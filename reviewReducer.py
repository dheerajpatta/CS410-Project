"""
CS410 - Project - Yelp Sentimate Analysis
This file will take the review.json file and reduce it to a managable size of 100 for testing.
"""
import json
import metapy
from itertools import islice

a = open('new-review.json', 'w+')
f = open('review.json')
for line in islice(f, 100):
    a.write(line)
a.close()
