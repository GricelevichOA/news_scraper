import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class SiteScraper(ABC):

	@abstractmethod
	def get_news():
		pass


class TutByScraper(SiteScraper):
	def __init__(self, url):
		self.url = 'https://www.tut.by/'

	def get_news(self):
		res = requests.get(self.url)
		soup = BeautifulSoup(res.content, 'html.parser')
		all_news = soup.find('div', id='latest')
		news_links = all_news.find_all('a', class_='entry__link io-block-link')

		for news in news_links:
			article_header = news.find('span', class_='entry-head _title').text
			article_link = news.get('href')
			article_res = requests.get(article_link)
			article_soup = BeautifulSoup(article_res.content, 'html.parser')
			article_body = article_soup.find('div', id='article_body').find_all('p')
			article_text = ' '.join([paragraph.get_text() for paragraph in article_body])
			
			print(article_link)
			print(article_header)			
			print(article_text)
			print(' ')

			


		#print(news_links)

bruh = TutByScraper('')

bruh.get_news()		


