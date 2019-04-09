from application import db
from application.models import Base

class Category(Base):
    
    name = db.Column(db.String(144), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    
#    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
#    items = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
        self.size = 1
        
#    @staticmethod
#   @staticmethod
#    def find_category():
#        stmt = text("SELECT Category_name FROM Category c"
#                    "0N c.name = name")
#        
#        res = db.engine.execute(stmt)
        
#        response = []
#        for row in res:
#            response.append({"item":row[0]})
            
 #       return response