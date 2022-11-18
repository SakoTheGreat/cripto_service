from webapp import create_app
#from webapp.function_date_binance import fill_binance_data_table
from webapp.function_date_bybit import fill_bybit_data_table
#from webapp.function_date_bitzlato import fill_binance_data_table

app = create_app()
with app.app_context():
    #fill_binance_data_table()
    fill_bybit_data_table()
    #fill_binance_data_table()