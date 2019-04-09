from application import db
from application.models import Base

from sqlalchemy.sql import text
from flask_login.utils import current_user

class Item(Base):
    
    name = db.Column(db.String(144), nullable=False)
    check = db.Column(db.Boolean, nullable=False)
    
#    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
#    category_name = db.Column(db.String(144), db.ForeignKey('category.name'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.check = False
        
        
    
    @staticmethod
    def list_items_of_user(account=0):
        stmt = text("SELECT Item.name FROM Item"
                    " JOIN Account ON Item.account_id = Account.id"
                    " WHERE (Item.account_id = :account)"
                    " GROUP BY Item.id").params(account=account)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"name":row[0]})
            
        return response
