from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_listed = db.Column(db.DateTime, default=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    check = db.Column(db.Boolean, nullable=False)
#    important = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.check = False
#        self.important = False