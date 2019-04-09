from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ItemForm(FlaskForm):
    name = StringField("Item name: ", [validators.Length(min=2)])
    bought = BooleanField("Bought: ")
#    category_name = StringField("Category: " [validators.Length(min=2)])
#    category_id = n
    
    class Meta:
        csrf = False