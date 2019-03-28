from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
  
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    items = db.relationship("Item", backref='account', lazy=True)

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
    
    @staticmethod
    def list_users():
        stmt = text("SELECT Account.username FROM Account"
                    " GROUP BY Account.id")
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1]})
            
        return response