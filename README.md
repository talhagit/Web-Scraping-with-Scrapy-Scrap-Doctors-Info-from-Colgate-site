# Web-Scraping-with-Scrapy-Scrap-Doctors-Info-from-Colgate-site
This code will extract info from : http://www.colgate.com/en/us/oc/oral-health , and extract all doctors Info and can e put in a csv

**Extra Requirements:**

This code will need a .csv file with zips which can be embed with in the Url for scraping.

 zips=pd.read_csv('ziplist/test1zip.csv')# In the code , the path needs to change to match the list.
 
**Prerequisite:**

* pip install scrapy

* pip install pandas

**How to run**

Navigate to where your environment variable(default directory) is set and run :
scrapy runspider Colgatescrape.py

**Overview:**

Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

For more information including a list of features check the Scrapy homepage at: https://scrapy.org

This repo is an example of webcrawler built using the Scrapy python framework.  For more details about Scrapy..

 - [Scrapy Framework](https://github.com/scrapy/scrapy/)
 - [Wiki](https://github.com/scrapy/scrapy/wiki)
