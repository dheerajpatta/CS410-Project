# Team 47: Yelp Rating Analysis
Paul Moreno and Ilean Monterrubio Jr

This project is for the University of Illinois Urbana-Champaign CS-410 Text Informations Systems class.

## Abstract
This section will contain an abstract of the project.

## Introduction
Yelp is a vertical search engine that allows users to search for place of business. The most search items are related to food, coffee, basically places where goods are delivered to the consumer. It is a platform that allows users to rate the service or good.

The project will focus on sentimential analysis based on the context of the topic. The focus of the context will be Service and Goods, each document will fit into one or both these contexts. After determining that each document will

The tool will track and differentiate the performance of customer services versus goods provided by a company over time. Yelp provides customer feedback with a star rating and review. The star rating does not provide specific reasons why the business earns the rating. We will take data from Yelp and use NLP to find reviews that address a business's customer service or product quality.  We will use Yelp datasets available on their website for educational use.The dataset is a subset of Yelps businesses, reviews, and users.

## Related Work

## Background

## Task Definitions
1. Gather data from Yelp Open Dataset, or other source. With the data collected, if data file is in JSON format it will be converted to comma delimited file (CSV).
   * Topic mining, finding the commonly used to describe to create the training data, which is Theta_B.
   * Each category will have their own Theat Background:
     * Service - which is if the comment is refering to the service they recieved.
     * Goods - which is if the comment is refering to the food or any product recieved.
     * The first 50 or 100 reviews will be used to create the training data.
2. Create Topic Modelling function.
3. Topic model using training data, each traning data will be run independently.
   * Create new files:
     * service.csv - This file will collected all comments related to service, upper limit of 500 comments.
     * goods.csv - This file will collected all comments related to good recieved, upper limit of 500 comments.
     * Find Precision, Recall, F1, for each file.
       * If less than .80 return to Task 3 .
4. Create sentiment analysis fucntion.
5. Run sentiment analysis on each file.
   * Use Stars to compare accuracy of analysis.
    * 4-5 stars means positive review.
    * 3 stars means neutral review.
    * 1-2 stars means negative review.
   * Find Precision, Recall, F1, for each file.
6. Visualize all data, to better analysis accuracy of tool created.

## Toolkits
The following toolkits where used:
* NLTK
* Scipy
* Pandas

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
