# Project Title: Yelp Rating Analysis
Team 47: Paul Moreno and Ilean Monterrubio Jr

## Abstract

## Introduction
Yelp is a vertical search engine that allows users to search for place of business. The most search items are related to food, coffee, basically places where goods are delivered to the consumer. It is a platform that allows users to rate the service or good.

The project will focus on sentimential analysis based on the context of the topic. The focus of the context will be Service and Goods, each document will fit into one or both these contexts. After determining that each document will


The tool will track and differentiate the performance of customer services versus goods provided by a company over time. Yelp provides customer feedback with a star rating and review. The star rating does not provide specific reasons why the business earns the rating. We will take data from Yelp and use NLP to find reviews that address a business's customer service or product quality.  We will use Yelp datasets available on their website for educational use.The dataset is a subset of Yelps businesses, reviews, and users.

## Related Work

## Background

## Task definitions
1. Gather data from Yelp Open Dataset, or other source. With the data collected, if data file is in JSON format it will be converted to comma delimited file (CSV).
2. Topic mining, finding the commonly used to describe to create the training data, which is \Theta .
  * Many code already that tokenizes the data. Will modify some existing code for this.
3. Write code tokenize words in dataset to see what words are common and which words people use to describe our different word distributions. Record output and show that we manually choose useful thetas in our sentiment analysis.
4. Task - Define
  Theta 1 for Good Reviews Service
  Theta 2 for Bad Service
  Theta 3 for Good Quality Goods and products
  Theta 4 for Bad quality Goods and products
  Theta Background
* Task  -Filter data collected using user inputs.
* Task  -Clustering data to facilitate browsing. Define similatry function to cluster. Should we use user input to define clustering and allow for ranking? What is cutoff 10 items?
* Task  -Test Clustering and visualize differences.

## Notes (this makes no sense i know just writing my ideas)
We want to categorize each comment into either Service or Goods. Then we want to run the sentiment analysis based on the collection of each category. After the analysis we can determine the distribution based of each category.

The sentiment analysis will be done using the NLTk and the star system will used to see if the prediction of the sentiment analysis is correct, 5-4 stars will be positive and 1-2 star is negative and 3 is neutral.





## Methodology

## Conclusion

## Useful links
* [Yelp Open Dataset](https://www.yelp.com/dataset)
* [Meta-Toolkit](https://meta-toolkit.org/)
* [NLTK Text Classification](http://text-processing.com/demo/sentiment/)
* [Illini Wiki Yelp Project](https://wiki.illinois.edu/wiki/pages/viewpage.action?spaceKey=timanpub&title=Capstone+design)
* [CS410 Spring 2014 Projects](http://web.engr.illinois.edu/~massung1/su14-cs410/past-projects.html)
* [Capstone Report for Data Science Specialization](https://statsbyslough.files.wordpress.com/2015/11/projectreport2.pdf)
* [Markdown Here Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet#links)
* (http://opensourceforu.com/2016/12/analysing-sentiments-nltk/)
* (http://www.nltk.org/howto/sentiment.html)
