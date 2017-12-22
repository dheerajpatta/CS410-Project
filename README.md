# Team 47: Yelp Rating Analysis
Paul Moreno and Ilean Monterrubio Jr

This project is for the University of Illinois Urbana-Champaign CS-410 Text Informations Systems class.

## Install
The tool was written in python, some installations are required.

```
pip install -e .
python download_nltk.py
```

## Abstract
Vertical search engines have become increasingly popular, they sift through limited databases for information. In particular location based mobile searching is extensively used for searching businesses that are close to the user or have high user ratings.The broad web searches cannot accommodate all of the users searches when it come to specific topics with implicit assumptions that are not captured in general web searching. One major example is Yelp, its content is specialized for users browsing information on service or goods. General web searches focus on a broad range of web page results while mobile searches focuses on the results closer to the users location. Results from services like yelp allow a user to rank results by distance ,ratings, or reviews. Customer preferences can be tracked by looking at the user’s reviews of visits on yelp. Being able to track user experience at a business could lead to greater traffic and sales at the business.

The software tool we have built allows businesses to classify their reviews and filter them to see if they are lacking certain areas. We chose to focus on analyzing if the customers based their reviews on goods or services provided by the business. Understanding the areas of opportunity and growth for a business are essential to maintain growth and a good client base.

## Introduction
The rise in popularity of mobile devices has led to search algorithms that implement data from the user’s location and movements. Yelp and others leverage information available about the user when implementing searches using mobile devices. Users often use services like Yelp to search for new businesses to visit or to check for best user experience from reviews. Vertical search engines such as Yelp address the need for deeper more specific more relevant search search results from a certain domain. The application of algorithms that leverage domain knowledge and implicit user specific information from the task increase the chances of the user receiving relevant search results.
The results yielded from Yelp can help drive users to certain businesses. This makes business reviews on Yelp a critical component of user feedback. According to this Harvard Business School case study, every star in a review leads to a 5-9% difference in revenue. The star and the review are important to businesses seeking to maximize business from Yelp users. The importance of the star rating can help businesses track their performance as well as identify areas of weakness. Tracking star data can also lead to improved business performance and provide feedback on customer needs. Addressing customer needs is critical to service based business. It is also important for business to identify in what area their business is lacking.

Most of the apps available that leverage Yelp data track the customer habits, needs, and requests. They are centered in providing better search results and service to the users of Yelp. Our software in contrast provides the business user with categorized feedback that they can quickly track and use to target goals.
In this software tool we choose to  identify Yelp reviews according to whether the review is focused on the service provided at the business or goods sold at the business. By tracking these two topics a business could track their business strengths and weaknesses. In a restaurant, for example, it is important to have good service and good food. If one is lacking far behind the other the business could suffer. It also allows management insight into worker interactions with the customer. Poor customer service can be tracked and correlated to a hiring or employee firing. It is also a window into worker morale.

## Related Work

## Background

## Task Definitions
1. Gather data from Yelp Open Dataset, or other source. With the data collected, if data file is in JSON format it will be converted to comma delimited file (CSV). Downloaded the data set from [here](https://www.dropbox.com/s/wc6rzl1a2os721d/yelp.csv?dl=0).
   * Topic mining, finding the words commonly used to describe service and goods to create the training data.
     * This part was challenging, getting the data all cleaned using NLTK. First challenge was tokenizing the first 1000 comments. Second was lowercasing all the words to better pull them together for removing all the stop words. We found that the built in stop words was not as complete as the one used for the machine problems done in class. Last we stemmed using the PorterStemmer built in to NLTK that worked as advertise.
   * Each category will have their own Theat Background:
     * Service - which is if the comment is referring to the service they received.
       * File created.
     * Goods - which is if the comment is referring to the food or any product received.
       * File created.
     * The first 1000 reviews will be used to create the training data.
2. Create Topic Modeling function.
3. Topic model using training data, each training data will be run independently.
   * Create new files:
     * service.csv - This file will collected all comments related to service, upper limit of 500 comments.
     * goods.csv - This file will collected all comments related to good received, upper limit of 500 comments.
     * Find Precision, Recall, F1, for each file.
       * If less than .60 return to Task 3.
4. Create sentiment analysis function.
5. Run sentiment analysis on each file.
   * Use Stars to compare accuracy of analysis.
    * 4-5 stars means positive review.
    * 3 stars means neutral review.
    * 1-2 stars means negative review.
   * Find Precision, Recall, F1, for each file.
6. Visualize all data, to better analysis accuracy of tool created.

## Conclusion

## Useful links
* [Yelp Open Dataset](https://www.yelp.com/dataset)
* [Meta-Toolkit](https://meta-toolkit.org/)
* [NLTK Text Classification](http://text-processing.com/demo/sentiment/)
* [Illini Wiki Yelp Project](https://wiki.illinois.edu/wiki/pages/viewpage.action?spaceKey=timanpub&title=Capstone+design)
* [CS410 Spring 2014 Projects](http://web.engr.illinois.edu/~massung1/su14-cs410/past-projects.html)
* [Capstone Report for Data Science Specialization](https://statsbyslough.files.wordpress.com/2015/11/projectreport2.pdf)
