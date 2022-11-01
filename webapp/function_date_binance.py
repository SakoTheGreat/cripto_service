from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

from webapp.model import db, BitCurrency


action_types ={
    'Sell': 'sell',
    'Buy': '',
}

tokens = ['USDT', 'BTC']
payment_methods = {
    'Tinkoff': 'TinkoffNew',
    'RosBank': 'RosBankNew',
    'RaiffeisenBank': 'RaiffeisenBank',
}

SUB_URLS_PROGRAMIMIMI = {}

for token in tokens:
    for bank, bank_id in payment_methods.items():
        for action, action_id in action_types.items():
            key = (action, token, 'RUB', bank, 'Binance')
            if action == 'Sell':
                SUB_URLS_PROGRAMIMIMI[key] = f"{action_id}/{token}?fiat=RUB&payment={bank_id}"
            elif action == 'Buy':
                SUB_URLS_PROGRAMIMIMI[key] = f"{bank_id}/{token}?fiat=RUB"



def get_price(sub_url):
    driver = Chrome()
    driver.get(f"https://p2p.binance.com/ru/trade/{sub_url}")
    sleep(6)
    search_price = driver.find_element(By.CSS_SELECTOR, '[class="css-1m1f8hn"]')
    driver.close()
    return search_price.text

def save_binance(all_prices):
    for price_info in all_prices:
        bin_bin = BitCurrency(sell_purchase=price_info[1], currency=price_info[2], bank=price_info[3], site=price_info[4], price=price_info[0])
        db.session.add(bin_bin)
        db.session.commit()


def db_binance():
    for key, sub_url in SUB_URLS_PROGRAMIMIMI.items():
        all_prices = []
        price = get_price(sub_url)
        all_prices.append(price)
        for i in key:
            all_prices.append(i)
        
        save_binance(all_prices)
