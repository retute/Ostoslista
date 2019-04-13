from application import db

from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
    
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    
    items = db.relationship("Item", backref='account', lazy=True)
    categories = db.relationship("Category", backref='account', lazy=True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(selfself):
        return["ADMIN"]
    
    @staticmethod
    def list_users():
        stmt = text("SELECT Account.username FROM Account"
                    " GROUP BY Account.id")
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"username":row[0]})
            
        return response