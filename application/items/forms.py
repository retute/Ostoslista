from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, validators
from application.categories.models import Category
from flask_login import current_user

class ItemForm(FlaskForm):
    name = StringField("Item name: ", [validators.Length(min=2)])
    bought = BooleanField("Bought: ")
    category_id = SelectField("Category: ", coerce=int)
    
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(x.id, x.name) for x in Category.query.filter_by(account_id=current_user.id)]
    
    class Meta:
        csrf = False