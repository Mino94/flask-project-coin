from coin_app import db

class UserCoin(db.Model):
    __tablename__ = 'usercoin'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    coin_id = db.Column(db.Integer(), db.ForeignKey('coin.id'), nullable=False)
    
    user = db.relationship('User', backref='usercoin_set', cascade="all,delete")
    coin = db.relationship('Coin', backref='usercoin_set')

    def __repr__(self):
        return f"User Coin {self.id}"