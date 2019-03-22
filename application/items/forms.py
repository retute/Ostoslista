from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField

class ItemForm(FlaskForm):
    name = StringField("Item name: ")
    check = BooleanField("Check")
 
    class Meta:
        csrf = False