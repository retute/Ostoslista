from application import db
from application.models import Base

from sqlalchemy.sql import text
from flask_login.utils import current_user

class Item(Base):
    
    name = db.Column(db.String(144), nullable=False)
    check = db.Column(db.Boolean, nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
#    category_name = db.Column(db.String(144), db.ForeignKey('category.name'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.check = False
        
        
    
    @staticmethod
    def list_items_of_user():
        stmt = text("SELECT Item.name, Item.check FROM Item"
                    "Left JOIN Account ON Item.account_id = Account.id"
                    " WHERE Item.account_id = 1"
                    " GROUP BY Item.id")
#        stmt.setInteger(1, current_user.id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"name":row[0]}, {"check":row[1]})
            
        return response

    @staticmethod
    def remove_item(item_id):
        stmt = text("DELETE FROM Item"
                    " WHERE item.id = ?")