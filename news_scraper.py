import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class SiteScraper(ABC):

	@abstractmethod
	def get_news():
		pass

class TutByScraper(SiteScraper):
	def __init__(self):
		self.url = 'https://www.tut.by/'
		self.name = 'tut.by'

	def get_news(self):
		res = requests.get(self.url)
		soup = BeautifulSoup(res.content, 'html.parser')
		all_news = soup.find('div', id='latest')
		news_links = all_news.find_all('a', class_='entry__link io-block-link')
		news_dict = []

		for news in news_links:
			article_header = news.find('span', class_='entry-head _title').text.replace(u'\xa0', u' ')

			article_link = news.get('href')
			article_res = requests.get(article_link)
			article_soup = BeautifulSoup(article_res.content, 'html.parser')
			article_body = article_soup.find('div', id='article_body').find_all('p')
			article_text = ' '.join([paragraph.get_text() for paragraph in article_body]).replace(u'\xa0', u' ')

			news_dict.append({
				"name": self.name,
				"link": article_link,
				"header": article_header,
				"text": article_text
			})
		return news_dict

class YandexScraper(SiteScraper):
	def __init__(self):
		self.url = 'https://yandex.by/'
		self.name = 'yandex.by'

	def get_news(self):
		res = requests.get(self.url)
		soup = BeautifulSoup(res.content, 'html.parser')
		all_news = soup.find('div', id='wd-_topnews')
		news_links = all_news.find('ol', class_='list news__list').find_all('a', class_='home-link list__item-content list__item-content_with-icon home-link_black_yes')
		news_dict = []

		for news in news_links:
			article_link = news.get('href')
			article_res = requests.get(article_link)
			article_soup = BeautifulSoup(article_res.content, 'html.parser')
			article_header = article_soup.find('span', class_='story__head-wrap').text
			article_text = article_soup.find('div', class_='doc__text').text

			news_dict.append({
				"name": self.name,
				"link": article_link,
				"header": article_header,
				"text": article_text
			})
		return news_dict

class RbcRuScraper(SiteScraper):
	def __init__(self):
		self.url = 'https://www.rbc.ru/'
		self.name = 'rbc.ru'
	def get_news(self):
		res = requests.get(self.url)
		soup = BeautifulSoup(res.content, 'html.parser')
		all_news = soup.find('div', class_='js-news-feed-list')
		news_links = all_news.find_all('a', class_='news-feed__item js-news-feed-item js-yandex-counter')
		news_dict = []
		for news in news_links:
			article_link = news.get('href')
			article_res = requests.get(article_link.strip())
			article_soup = BeautifulSoup(article_res.content, 'html.parser')
			article_header = article_soup.find(itemprop='headline').text
			article_body = article_soup.find('div', itemprop='articleBody').find_all('p')
			article_text = ' '.join([paragraph.get_text() for paragraph in article_body]).replace(u'\xa0', u' ').strip()

			news_dict.append({
				"name": self.name,
				"link": article_link,
				"header": article_header,
				"text": article_text
			})	
		return news_dict

class SiteScraperFactory():
	def get_scraper(self, scraper_name):
		if scraper_name == 'TutByScraper':
			return TutByScraper()
		elif scraper_name == 'YandexScraper':
			return YandexScraper()
		elif scraper_name == 'RbcRuScraper':
			return RbcRuScraper()	




