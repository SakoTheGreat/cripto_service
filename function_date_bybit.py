from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm



SUB_URLS = [
    "1&token=USDT&fiat=RUB&paymentMethod=75",
    "0&token=USDT&fiat=RUB&paymentMethod=75",
    "1&token=USDT&fiat=RUB&paymentMethod=185",
    "0&token=USDT&fiat=RUB&paymentMethod=185",
    "1&token=USDT&fiat=RUB&paymentMethod=64",
    "0&token=USDT&fiat=RUB&paymentMethod=64",
    "1&token=BTC&fiat=RUB&paymentMethod=75",
    "0&token=BTC&fiat=RUB&paymentMethod=75",
    "1&token=BTC&fiat=RUB&paymentMethod=185",
    "0&token=BTC&fiat=RUB&paymentMethod=185",
    "1&token=BTC&fiat=RUB&paymentMethod=64",
    "0&token=BTC&fiat=RUB&paymentMethod=64",
]



def get_price(driver, sub_url):
    driver.get(f"https://www.bybit.com/fiat/trade/otc/?actionType={sub_url}")
    sleep(3)
    search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
    return search_price.text


if __name__=='__main__':
    all_date = []
    driver = Chrome()
    for sub_url in SUB_URLS:
        price = get_price(driver, sub_url)
        all_date.append(price)
    print(all_date)
    driver.close()
