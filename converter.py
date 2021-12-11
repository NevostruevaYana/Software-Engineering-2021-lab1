import requests
from bs4 import BeautifulSoup

USD_EUR = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+' \
          '%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%' \
          'D0%B2%D1%80%D0%BE&aqs=chrome..69i57j0i20i263i512j0i512l7j0i20i263i512.2923j1j15&' \
          'sourceid=chrome&ie=UTF-8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


class USDEURConverter:

    @staticmethod
    def check_currency():
        full_page = requests.get(USD_EUR, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
        return convert[0].text

    @staticmethod
    def calculate_value(currency, value):
        return currency * value