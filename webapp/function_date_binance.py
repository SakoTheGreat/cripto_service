from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from webapp.model import db, BitCurrency



def get_price(sub_url):
    driver = Chrome()
    driver.get(f"https://p2p.binance.com/ru/trade/{sub_url}")
    sleep(6)
    search_price = driver.find_element(By.CSS_SELECTOR, '[class="css-1m1f8hn"]')
    price = search_price.text
    return price

def save_binance(all_prices):
    for price_info in all_prices:
        bin_bin = BitCurrency(sell_purchase=price_info[1], currency=price_info[3], bank=price_info[4], site=price_info[-1], price=price_info[0])
        db.session.add(bin_bin)
        db.session.commit()


def proba_pera():
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
    pp = 'RUB'
    all_prices = []
    for token in tokens:
        for bank, bank_id in payment_methods.items():
            for action, action_id in action_types.items():
                price_info = []
                key = (action, token, pp, bank, 'Binance')
                try:
                    if action == 'Sell':
                        price = get_price(f"{action_id}/{token}?fiat={pp}&payment={bank_id}")
                        price_info.append(price)
                    elif action == 'Buy':
                        price = get_price(f"{bank_id}/{token}?fiat={pp}")
                        price_info.append(price)                        
                except NoSuchElementException:
                    continue
                for i in key:
                    price_info.append(i)
                all_prices.append(price_info)    

    save_binance(all_prices)    
    

