from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm



sub_urls = [
    'sell/USDT?fiat=RUB&payment=TinkoffNew',
    'TinkoffNew/USDT?fiat=RUB',
    'sell/USDT?fiat=RUB&payment=RosBankNew',
    'RosBankNew/USDT?fiat=RUB',
    'sell/USDT?fiat=RUB&payment=RaiffeisenBank',
    'RaiffeisenBank/USDT?fiat=RUB',
    'sell/BTC?fiat=RUB&payment=TinkoffNew',
    'TinkoffNew/BTC?fiat=RUB',
    'sell/BTC?fiat=RUB&payment=RosBankNew',
    'RosBankNew/BTC?fiat=RUB',
    'sell/BTC?fiat=RUB&payment=RaiffeisenBank',
    'RaiffeisenBank/BTC?fiat=RUB',
]


def get_price(sub_url):
    driver.get(f"https://p2p.binance.com/ru/trade/{sub_url}")
    sleep(8)
    search_price = driver.find_element(By.CSS_SELECTOR, '[class="css-1m1f8hn"]')
    return search_price.text


if __name__=='__main__':
    all_prices = []
    driver = Chrome()
    for sub_url in sub_urls:
        price = get_price(sub_url)
        all_prices.append(price)
    print(all_prices)
    driver.close()
