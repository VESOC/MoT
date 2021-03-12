from bs4 import BeautifulSoup
import requests
from mail import WEATHER_FORMAT


def prepare_soup():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    r = requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9A%B8%EC%82%B0+%EC%8B%A0%EC%A0%952%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%8B%A0%EC%A0%952%EB%8F%99+%EB%82%A0%EC%94%A8&tqi=hZ7h6wp0J14ssCMgp1KssssstC8-332622', headers=headers)
    bs = BeautifulSoup(r.text, 'lxml')
    return bs


def get_weather():
    bs = prepare_soup()
    cur_temp = bs.find('p', {'class': 'info_temperature'}
                       ).text.replace('도씨', '')
    minmax_temp = bs.find('span', {'class': 'merge'}).text.strip()
    weather = bs.find('p', {'class': 'cast_txt'}).text.strip().split(',')[0]
    fine_dust = bs.find('dl', {'class': 'indicator'}).contents[3].contents[1]
    ultrafine_dust = bs.find(
        'dl', {'class': 'indicator'}).contents[7].contents[1]
    ozone = bs.find('dl', {'class': 'indicator'}).contents[11].contents[1]
    weather_table = WEATHER_FORMAT.format(
        cur_temp, minmax_temp, weather, fine_dust, ultrafine_dust, ozone)
    return weather_table
