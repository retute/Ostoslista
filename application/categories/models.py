from application import db

from sqlalchemy.sql import text
from flask_login.utils import current_user, login_required

class Category(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    items = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, cname):
        self.cname = cname
        self.size = 0
        
    @staticmethod
    @login_required
    def list_categories_for_user(account=0):
        stmt = text("SELECT Category.id, Category.cname, Category.size FROM Category"
                    " JOIN Account ON Category.account_id = Account.id"
                    " WHERE (Category.account_id = :account)"
                    " ORDER BY Category.size DESC").params(account=account)
        
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"id": row[0], "cname":row[1], "size":row[2]})
            
        return response

    def __repr__(self):
        return str(id)