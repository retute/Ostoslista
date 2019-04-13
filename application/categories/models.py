from application import db

class Category(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    items = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
        self.size = 1
        
    @staticmethod
    @staticmethod
    def list_category():
        stmt = text("SELECT Category.name, Category.size FROM Category"
                    " WHERE Category.size > -1"
                    " GROUP BY Category.size")
        
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"item":row[0]})
            
        return response