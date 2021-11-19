from bs4 import BeautifulSoup
import requests
from mail import WEATHER_FORMAT
from info import AREA


def prepare_soup():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    r = requests.get(
        'https://search.naver.com/search.naver?query='+'+'.join(AREA.split(' '))+'+날씨', headers=headers)
    bs = BeautifulSoup(r.text, 'lxml')
    return bs


def get_weather_table():
    bs = prepare_soup()
    cur_temp = bs.find('div', {'class': 'temperature_text'}
                       ).text.replace('도씨', '')
    minmax_temp = bs.find_all('li', {'class': 'week_item today'})[0].find('span', {'class': 'temperature_inner'}).text.strip()
    weather = bs.find('span', {'class': 'weather'}).text.strip()
    dust_info = bs.find_all('li', {'class': 'item_today'})
    fine_dust = dust_info[0].find('span', {'class': 'txt'}).text.strip()
    ultrafine_dust = dust_info[1].find('span', {'class': 'txt'}).text.strip()
    ozone = dust_info[2].find('span', {'class': 'txt'}).text.strip()
    weather_table = WEATHER_FORMAT.format(
        cur_temp, minmax_temp, weather, fine_dust, ultrafine_dust, ozone)
    return weather_table
