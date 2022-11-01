from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep



SUB_URLS = {
    ('Buy', 'USDT', 'RUB', 'Tinkoff', 'Bybit'): "1&token=USDT&fiat=RUB&paymentMethod=75",
    ('Sell', 'USDT', 'RUB', 'Tinkoff', 'Bybit'): "0&token=USDT&fiat=RUB&paymentMethod=75",
    ('Buy', 'USDT', 'RUB', 'RosBank', 'Bybit'): "1&token=USDT&fiat=RUB&paymentMethod=185",
    ('Sell', 'USDT', 'RUB', 'RosBank', 'Bybit'): "0&token=USDT&fiat=RUB&paymentMethod=185",
    ('Buy', 'USDT', 'RUB', 'RaiffeisenBank', 'Bybit'): "1&token=USDT&fiat=RUB&paymentMethod=64",
    ('Sell', 'USDT', 'RUB', 'RaiffeisenBank', 'Bybit'): "0&token=USDT&fiat=RUB&paymentMethod=64",
    ('Buy', 'BTC', 'RUB', 'Tinkoff', 'Bybit'): "1&token=BTC&fiat=RUB&paymentMethod=75",
    ('Sell', 'BTC', 'RUB', 'Tinkoff', 'Bybit'): "0&token=BTC&fiat=RUB&paymentMethod=75",
    ('Buy', 'BTC', 'RUB', 'RosBank', 'Bybit'): "1&token=BTC&fiat=RUB&paymentMethod=185",
    ('Sell', 'BTC', 'RUB', 'RosBank', 'Bybit'): "0&token=BTC&fiat=RUB&paymentMethod=185",
    ('Buy', 'BTC', 'RUB', 'RaiffeisenBank', 'Bybit'): "1&token=BTC&fiat=RUB&paymentMethod=64",
    ('Sell', 'BTC', 'RUB', 'RaiffeisenBank', 'Bybit'): "0&token=BTC&fiat=RUB&paymentMethod=64",
}



def get_price(sub_url):
    driver.get(f"https://www.bybit.com/fiat/trade/otc/?actionType={sub_url}")
    sleep(3)
    search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
    return search_price.text


if __name__=='__main__':
    all_prices_lol = []
    driver = Chrome()
    for key, sub_url in SUB_URLS.items():
        all_prices = []
        price = get_price(sub_url)
        all_prices.append(price)
        for i in key:
            all_prices.append(i)
        all_prices_lol.append(all_prices)
        
    print(all_prices_lol)
    driver.close()
