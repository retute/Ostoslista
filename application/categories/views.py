from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.items.forms import ItemForm
from flask_login import login_required, current_user

@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", items = Item.query.all())

#@app.route("/items/new/")
#@login_required
#def categories_form():
#    return render_template("items/new.html", form = ItemForm())

#@app.route("/categories/<item_id>/", methods=["POST"])
#@login_required
#def categories_set_empty(category_id):
#    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
@login_required
def category_create(name):
    form = CategoryForm(request.form)
    
    if not form.validate():
        return render_template("items/new.html", form = form)
    
    c = Category(name)
    c.size = 1
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("items_index"))

