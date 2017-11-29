"""
CS410 - Project - Yelp Sentimate Analysis
This file will take the review.json file and reduce it to a managable size of 100 for testing.
"""
import json
import metapy
from itertools import islice

o = open('new-review.json', 'w+')
r = open('review.json')
for line in islice(r, 500):
    o.write(line)
o.close()
