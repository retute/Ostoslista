from application import db

from sqlalchemy.sql import text
from flask_login.utils import current_user

class Item(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    bought = db.Column(db.Boolean, nullable=False)
    
#    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
#    category_name = db.Column(db.String(144), db.ForeignKey('category.name'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.account_id = current_user.id
        
    
    @staticmethod
    def list_items_of_user(account=0):
        stmt = text("SELECT Item.id, Item.name, Item.bought FROM Item"
                    " JOIN Account ON Item.account_id = Account.id"
                    " WHERE (Item.account_id = :account)"
                    " GROUP BY Item.id").params(account=account)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "bought":row[2]})
            
        return response