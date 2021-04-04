from coin_app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    pwd = db.Column(db.Integer)
    
    def __repr__(self):
        return f"User {self.id}"
