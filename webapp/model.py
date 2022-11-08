from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BitCurrency(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    currency = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bank = db.Column(db.String, nullable=False)
    sell_purchase = db.Column(db.String, nullable=False)
    site = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Currency {} {} {}>'.format(self.price, self.bank, self.currency)