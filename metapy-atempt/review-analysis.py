import math
import sys
import time

import metapy
import pytoml

def tokens_lowercase(doc):
    #Write a token stream that tokenizes with ICUTokenizer,
    #lowercases, removes words with less than 2 and more than 5  characters
    #performs stemming and creates trigrams
    '''Place your code here'''
    #1st order of business Tokenize the string, I decided to remove XML tags
    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)

    #2nd order of business make string to lowercase
    tok = metapy.analyzers.LowercaseFilter(tok)

    #3rd order of business remove any words with less than 2 char and more than 5 char
    tok = metapy.analyzers.LengthFilter(tok, min=2, max=5)

    #4th order of business Steamming the string
    tok = metapy.analyzers.Porter2Filter(tok)

    #5th order of business create Trigrams
    #ana = metapy.analyzers.NGramWordAnalyzer(3, tok)
    #character_trigrams = ana.analyze(doc)

    #test code
    tok.set_content(doc.content())
    tokens = [token for token in tok]
    return tokens
    #end of test code

    #leave the rest of the code as is
    #tok.set_content(doc.content())
    #tokens, counts = [], []
    #for token, count in character_trigrams.items():
    #    counts.append(count)
    #    tokens.append(token)
    #return tokens



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} config.toml".format(sys.argv[0]))
        sys.exit(1)

    cfg = sys.argv[1]
    print('Building or loading index...')
    idx = metapy.index.make_forward_index('config.toml')
    ''''
    with open(cfg, 'r') as fin:
        cfg_d = pytoml.load(fin)
    '''
    doc = metapy.index.Document()
    print('Running queries')
    #with open()
    #tokens = tokens_lowercase(doc)
    print idx.num_docs()
    tok =  metapy.analyzers.ICUTokenizer(suppress_tags=True)
    dset = metapy.learn.Dataset(idx)
    lda_inf = metapy.topics.LDACollapsedVB(dset, num_topics=2, alpha=1.0, beta=0.01)
    lda_inf.run(num_iters=500)
    lda_inf.save('lda-cvb0')
    model = metapy.topics.TopicModel('lda-cvb0')
    model.top_k(tid=0)
    print [(fidx.term_text(pr[0]), pr[1]) for pr in model.top_k(tid=0)]
