from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from webapp.model import db, BitCurrency



def get_price(sub_url):
    driver = Chrome()
    driver.get(f"https://www.bybit.com/fiat/trade/otc/?{sub_url}")
    sleep(2)
    driver.get(f"https://www.bybit.com/fiat/trade/otc/?{sub_url}")
    sleep(4)
    search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
    price = search_price.text
    return price


def save_binance(all_prices):
    for price_info in all_prices:
        bin_bin = BitCurrency(sell_purchase=price_info[1], currency=price_info[3], bank=price_info[4], site=price_info[-1], price=price_info[0])
        db.session.add(bin_bin)
        db.session.commit()

def fill_bybit_data_table():
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
    pp = 'RUB'
    all_prices = []
    for token in tokens:
        for bank, bank_id in payment_methods.items():
            for action, action_id in action_types.items():
                price_info = []
                key = (action, token, pp, bank, 'Bybit')
                sub_url = f"actionType={action_id}&token={token}&fiat={pp}&paymentMethod={bank_id}"
                print(key, sub_url)
                try:
                    price = get_price(sub_url)
                    price_info.append(price)
                except NoSuchElementException:
                    continue
                for i in key:
                    price_info.append(i)
                
                all_prices.append(price_info)    

    save_binance(all_prices)


