from flask import Flask, jsonify
from news_scraper import SiteScraperFactory

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return 'Welcome to news'

@app.route('/news/tutby', methods=['GET'])
def get_tutby_news():
    news_tutby = SiteScraperFactory().get_scraper('TutByScraper').get_news()
    return jsonify(news_tutby)

@app.route('/news/yandexru', methods=['GET'])
def get_yandexru_news():
    news_yandexru = SiteScraperFactory().get_scraper('YandexScraper').get_news()
    return jsonify(news_yandexru)

@app.route('/news/rbcru', methods=['GET'])
def get_rbcru_news():
    news_rbcru = SiteScraperFactory().get_scraper('RbcRuScraper').get_news()
    return jsonify(news_rbcru)

@app.route('/news', methods=['GET'])
def get_news():
	news_tutby = SiteScraperFactory().get_scraper('TutByScraper').get_news()
	news_yandexru = SiteScraperFactory().get_scraper('YandexScraper').get_news()
	news_rbcru = SiteScraperFactory().get_scraper('RbcRuScraper').get_news()

	news = news_tutby + news_yandexru + news_rbcru
	return jsonify(news)

if __name__ == "__main__":
    app.run()

