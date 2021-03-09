from bs4 import BeautifulSoup
import requests


def prepare_soup():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    r = requests.get('https://news.naver.com', headers=headers)
    bs = BeautifulSoup(r.text, 'lxml')
    return bs


def get_headlines(bs, news):
    main_headline = bs.find_all('p', {'class': 'hdline_flick_tit'})
    headlines = bs.find_all('a', {'class': 'lnk_hdline_article'})
    for headline in main_headline + headlines:
        news['헤드라인'].append(headline.string.strip())


def get_specific_news(bs, news):
    news_types = ['정치', '경제', '사회', '생활/문화', '세계', 'IT/과학']
    for idx, news_type in enumerate(bs.find_all('div', {'class': 'com_list'})):
        news[news_types[idx]].append(news_type.find(
            'dl', {'class': 'mtype_img'}).text.strip())
        for type_news in news_type.find_all('strong'):
            news[news_types[idx]].append(type_news.string)


def get_news():
    news_types = {
        '헤드라인': [],
        '정치': [],
        '경제': [],
        '사회': [],
        '생활/문화': [],
        '세계': [],
        'IT/과학': [],
    }
    bs = prepare_soup()
    get_headlines(bs, news_types)
    get_specific_news(bs, news_types)
    # print(news_types['헤드라인'])
    news = [n.strip().replace('\n', '').replace('동영상', '').replace('기사', '')
            for news_type in news_types.values() for n in news_type if n.replace('\n', '') != '동영상기사']
    news = [n for n in news if len(n.strip())]
    return news
