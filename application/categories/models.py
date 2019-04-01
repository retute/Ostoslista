from application import db
from application.models import Base

class Category(Base):
    
    name = db.Column(db.String(144), nullable=False)
    empty = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    items = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
        self.empty = False
