from bs4 import BeautifulSoup
import requests
from mail import NEWS_TABLE_FORMAT, ARTICLE_FORMAT


def prepare_soup():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    r = requests.get('https://news.naver.com', headers=headers)
    bs = BeautifulSoup(r.text, 'lxml')
    return bs


def get_headline_table(bs):
    articles = ''
    for img_headline in bs.find_all('a', {'class': 'lnk_hdline_main_article'}) + bs.find_all('a', {'class': 'lnk_hdline_article'}):
        link = ('https://news.naver.com' if img_headline['href'].startswith(
            '/') else '') + img_headline['href']
        title = img_headline.text.strip(' \n')
        articles += ARTICLE_FORMAT.format(link, title)
    headline_table = NEWS_TABLE_FORMAT.format(
        TYPE='헤드라인', ARTICLES=articles.rstrip('\n'))
    return headline_table


def get_specific_news_table(bs):
    news_types = ('정치', '경제', '사회', '생활/문화', '세계', 'IT/과학')
    news_table = ''
    for news_type, news_list in zip(news_types, bs.find_all('div', {'class': 'com_list'})):
        articles = ''
        for article in news_list.find_all('a'):
            if title := article.text.strip(' \n').replace('동영상 기사', ''):
                link = article['href']
                articles += ARTICLE_FORMAT.format(link, title)
        news_table += NEWS_TABLE_FORMAT.format(TYPE=news_type,
                                               ARTICLES=articles.rstrip('\n'))
    return news_table


def get_news_table():
    bs = prepare_soup()
    news_table = get_headline_table(bs) + get_specific_news_table(bs)
    return news_table
