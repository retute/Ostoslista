from application import db

from sqlalchemy.sql import text
from flask_login.utils import current_user, login_required

class Category(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False, unique=True)
    size = db.Column(db.Integer, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    items = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
        self.size = 1
        
    @staticmethod
    @login_required
    def list_categories_for_user(account=0):
        stmt = text("SELECT Category.name, Category.size FROM Category"
                    " WHERE (Category.account_id = :account OR Category.account_id=0)"
                    " ORDER BY Category.size").params(account=account)
        
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"name":row[0], "size":row[1]})
            
        return response

