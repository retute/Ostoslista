from application import db
from application.models import Base

class Item(Base):
    
    name = db.Column(db.String(144), nullable=False)
    check = db.Column(db.Boolean, nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.check = False
