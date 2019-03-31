from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Item name: ", [validators.Length(min=2)])
 
    class Meta:
        csrf = False