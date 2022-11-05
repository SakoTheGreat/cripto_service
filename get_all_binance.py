from webapp import create_app
from webapp.function_date_binance import proba_pera
#from webapp.function_date_bybit import fill_bybit_data_table


app = create_app()
with app.app_context():
    proba_pera()
    #fill_bybit_data_table()