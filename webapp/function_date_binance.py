from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

from webapp.model import db, bit_currency



sub_urls = {
    ('Sell', 'USDT', 'Tinkoff', 'Binance'): 'sell/USDT?fiat=RUB&payment=TinkoffNew',
    ('Buy', 'USDT', 'Tinkoff', 'Binance'): 'TinkoffNew/USDT?fiat=RUB',
    ('Sell', 'USDT', 'RosBank', 'Binance'): 'sell/USDT?fiat=RUB&payment=RosBankNew',
    ('Buy', 'USDT', 'RosBank', 'Binance'): 'RosBankNew/USDT?fiat=RUB',
    ('Sell', 'USDT', 'RaiffeisenBank', 'Binance'): 'sell/USDT?fiat=RUB&payment=RaiffeisenBank',
    ('Buy', 'USDT', 'RaiffeisenBank', 'Binance'): 'RaiffeisenBank/USDT?fiat=RUB',
    ('Sell', 'BTC', 'Tinkoff', 'Binance'): 'sell/BTC?fiat=RUB&payment=TinkoffNew',
    ('Buy', 'BTC', 'Tinkoff', 'Binance'): 'TinkoffNew/BTC?fiat=RUB',
    ('Sell', 'BTC', 'RosBank', 'Binance'): 'sell/BTC?fiat=RUB&payment=RosBankNew',
    ('Buy', 'BTC', 'RosBank', 'Binance'): 'RosBankNew/BTC?fiat=RUB',
    ('Sell', 'BTC', 'RaiffeisenBank', 'Binance'): 'sell/BTC?fiat=RUB&payment=RaiffeisenBank',
    ('Buy', 'BTC', 'RaiffeisenBank', 'Binance'): 'RaiffeisenBank/BTC?fiat=RUB',
}





def get_price(sub_url):
    driver = Chrome()
    driver.get(f"https://p2p.binance.com/ru/trade/{sub_url}")
    sleep(8)
    search_price = driver.find_element(By.CSS_SELECTOR, '[class="css-1m1f8hn"]')
    driver.close()
    return search_price.text

def save_binance(all_prices):
    bin_bin = bit_currency(sell_purchase=all_prices[1], currency=all_prices[2], bank=all_prices[3], site=all_prices[4], price=all_prices[0])
    db.session.add(bin_bin)
    db.session.commit()


def db_binance():
    for key, sub_url in sub_urls.items():
        all_prices = []
        price = get_price(sub_url)
        all_prices.append(price)
        for i in key:
            all_prices.append(i)
        
        save_binance(all_prices)
   
