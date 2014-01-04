import requests
class NYTAPI():
	def __init__(self, api_key):
		self.api_key = api_key
		self.url = 'http://api.nytimes.com/svc/search/v2/'

	def article_search(self, news_desk, page=1):
		request_url = self.url + 'articlesearch.json?&fq=news_desk:("{0}")&page={1}&sort=newest&api-key={2}'.format(news_desk, page, self.api_key)
		response = requests.get(request_url)
		
		return response.json()['response']['docs']