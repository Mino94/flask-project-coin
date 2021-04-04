from coin_app import db

class Coin(db.Model):
    __tablename__ = 'coin'

    id  = db.Column(db.Integer(), nullable=False,primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    opening_price = db.Column(db.Float())
    closing_price = db.Column(db.Float())
    prev_closing_price = db.Column(db.Float())

    min_price = db.Column(db.Float())
    max_price = db.Column(db.Float())
    units_traded = db.Column(db.Float())
    units_traded_24H = db.Column(db.Float()) 

    acc_trade_value = db.Column(db.Float())
    acc_trade_value_24H = db.Column(db.Float())


    fluctate_24H = db.Column(db.Float()) # 24시간 변동금액
    fluctate_rate_24H = db.Column(db.Float()) # 24시간 변동률

    # user = db.relationship('User', back_populates='coin', cascade="all,delete")

    def __repr__(self):
        return f"Coin {self.id}"