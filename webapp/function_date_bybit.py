from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

from webapp.model import db, BitCurrency

action_types = {
    'Buy': '1',
    'Sell': '0',
}

tokens = ['USDT', 'BTC']
payment_methods = {
    'Tinkoff': '75',
    'RosBank': '185',
    'RaiffeisenBank': '64',
}

SUB_URLS_PROGRAMMATICAL = {}
for token in tokens:
    for bank, bank_id in payment_methods.items():
        for action, action_id in action_types.items():
            key = (action, token, 'RUB', bank, 'Bybit')
            SUB_URLS_PROGRAMMATICAL[key] = f"actionType={action_id}&token={token}&fiat=RUB&paymentMethod={bank_id}"



def get_price(sub_url):
    driver = Chrome()
    driver.get(f"https://www.bybit.com/fiat/trade/otc/?{sub_url}")
    sleep(6)
    search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
    driver.close()
    return search_price.text


def save_binance(all_prices):
    for price_info in all_prices:
        bin_bin = BitCurrency(sell_purchase=price_info[1], currency=price_info[2], bank=price_info[3], site=price_info[4], price=price_info[0])
        db.session.add(bin_bin)
        db.session.commit()

def db_bybit():
    for key, sub_url in SUB_URLS_PROGRAMMATICAL.items():
        all_prices = []
        price = get_price(sub_url)
        all_prices.append(price)
        for i in key:
            all_prices.append(i)
        
        save_binance(all_prices)
