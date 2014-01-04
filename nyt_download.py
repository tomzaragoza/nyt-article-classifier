import requests
import time
from pymongo import MongoClient
from nytimes_api import NYTAPI
from pprint import pprint as pretty

mongo = MongoClient()
db = mongo['nyt-article-classifier']
collection = db['articles']

def retrieve_articles(api, news_desks):
	for news_desk in news_desks:
		count = 0
		page = 1
		while count <= 2000:
			page += 1
			for article in api.article_search(news_desk, page):
				print count
				count += 1
				print
				# print article
				print article['web_url']
				print article['snippet']
				print article['headline']['main']
				collection.insert({
									'url': article['web_url'], 
									'snippet': article['snippet'],
									'headline': article['headline']['main'],
									'news-desk': article['news_desk']
									})
			time.sleep(1.5)



if __name__ == "__main__":
	news_desks = ["Arts", "Business", "Obituaries", "Sports", "World"]
	api = NYTAPI("")
	
	retrieve_articles(api, news_desks)
