from webapp import create_app
from webapp.function_date_binance import db_binance

app = create_app()
with app.app_context():
    db_binance()