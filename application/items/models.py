from application import db

from sqlalchemy.sql import text
from flask_login.utils import current_user, login_required

class Item(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bought = db.Column(db.Boolean, nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.account_id = current_user.id
        
    
    
    @staticmethod
    @login_required
    def list_items_of_user(account=0):
        stmt = text("SELECT Item.id, Item.name, Category.cname, Item.bought FROM Item"
                    " JOIN Account ON Item.account_id = Account.id"
                    " JOIN Category ON Item.category_id = Category.id"
                    " WHERE (Item.account_id = :account)"
                    " GROUP BY Item.id").params(account=account)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "cname":row[2], "bought":row[3]})
            
        return response