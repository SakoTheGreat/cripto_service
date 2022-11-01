from webapp import create_app
from webapp.function_date_binance import db_binance
from webapp.function_date_bybit import db_bybit


app = create_app()
with app.app_context():
    db_binance()
    db_bybit()