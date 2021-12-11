import requests
from bs4 import BeautifulSoup

USD_EUR = 'https://www.fontanka.ru/currency.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


class USDEURConverter:

    @staticmethod
    def check_currency(currency1, currency2):
        try:
            full_page = requests.get(USD_EUR, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            classes = soup.findAll("td")

            values = soup.findAll("td", {"class": str(classes[7]).split("\"")[1]})
            curr = soup.findAll("td", {"class": str(classes[4]).split("\"")[1]})
            units = soup.findAll("td", {"class": str(classes[6]).split("\"")[1]})
        except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException,
                requests.exceptions.ConnectionError, requests.exceptions.HTTPError,):
            print("Oops! We have a problem with request!")

        num_of_cur = len(curr)
        currencies = {}
        for i in range(num_of_cur - 1):
            currencies[curr[i + 1].text] = i

        s = "ok"
        try:
            form_curr = currencies[currency1]
            to_curr = currencies[currency2]
        except KeyError:
            print("Invalid currency")
            s = "Invalid currency"
        if s == "ok":
            form_curr_ = float(values[form_curr].text) / int(units[form_curr].text)
            to_curr_ = float(values[to_curr].text) / int(units[to_curr].text)
            s = str(form_curr_ / to_curr_)
        return s

    @staticmethod
    def calculate_value(currency, value):
        return currency * value