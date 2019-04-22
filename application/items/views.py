from application import app, db
from flask import redirect, render_template, request, url_for
from application.categories.models import Category
from application.categories.forms import CategoryForm
from application.items.models import Item
from application.items.forms import ItemForm
from flask_login import login_required, current_user
from _overlapped import NULL

@app.route("/items", methods=["GET","POST"])
def items_index():
    return render_template("items/list.html", items=Item.list_items_of_user(current_user.id))

@app.route("/items/new/")
@login_required
def items_form():
    return render_template("items/new.html", form = ItemForm())

@app.route("/items/<item_id>/", methods=["POST"])
@login_required
def items_set_bought(item_id):
    i = Item.query.get(item_id)
    if i.bought == True:
        i.bought = False
    else:
        i.bought = True
    db.session().commit()
  
    return redirect(url_for("items_index"))

@app.route("/items/remove/<item_id>/", methods=["POST"])
@login_required
def items_remove(item_id):
    form = ItemForm(request.form)
    i = Item.query.get(item_id)
    c = Category.query.get(i.category_id)
    c.size = c.size - 1
    db.session().delete(i)
    db.session().commit()
    
    return redirect(url_for("items_index"))


@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)
    form2 = CategoryForm(request.form)
    
    if not form.validate():
        return render_template("items/new.html", form = form)
    
    i = Item(form.name.data)
    i.bought = form.bought.data
    i.category_id = 1
    i.account_id = current_user.id
    
    c = Category.query.get(i.category_id)
    if not c:
        return render_template("categories_index", error="Create a new category first!")
    c.size = c.size + 1

    db.session().add(i)
    db.session().commit()
  
    return redirect(url_for("items_index"))