from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from webapp.model import db, BitCurrency

def get_price(sub_url):
    driver = Chrome()
    driver.get(f"https://bitzlato.bz/p2p/{sub_url}")
    sleep(3)
    search_price = driver.find_element(By.CSS_SELECTOR, 'div.dt7xz70._1uuzz133._1uuzz13i > div:nth-child(1) > div > div:nth-child(3)')
    price = search_price.text
    driver.close()
    return price

def save_bitzlato(all_prices):
    for price_info in all_prices:
        bin_bin = BitCurrency(sell_purchase=price_info[1], currency=price_info[3], bank=price_info[4], site=price_info[-1], price=price_info[0])
        db.session.add(bin_bin)
        db.session.commit()


def fill_binance_data_table():
    action_types ={
    'Sell': 'sell',
    'Buy': 'buy',
}

    tokens = {'USDT': 'usdt', 'BTC': 'btc',}
    payment_methods = {
    'Tinkoff': 'tinkoff',
    'RosBank': 'rosbank',
    'RaiffeisenBank': 'raiffeisen-bank',
}
    pp = 'rub'
    all_prices = []
    for token, token_id in tokens.items():
        for bank, bank_id in payment_methods.items():
            for action, action_id in action_types.items():
                price_info = []
                key = (action, token, pp, bank, 'Bitzlato')
                sub_url = f"{action_id}-{token_id}-{pp}-{bank_id}"
                try:
                    price = get_price(sub_url)
                    price_info.append(price)                       
                except NoSuchElementException:
                    continue
                for i in key:
                    price_info.append(i)
                all_prices.append(price_info)    

    save_bitzlato(all_prices)    
    

