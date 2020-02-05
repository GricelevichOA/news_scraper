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
		news = soup.findAll('div', id_='latest')

		print(news)

bruh = TutByScraper('')

bruh.get_news()		


