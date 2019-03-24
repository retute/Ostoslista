from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.items.forms import ItemForm
from flask_login.utils import login_required

@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
@login_required
def items_form():
    return render_template("items/new.html", form = ItemForm())

@app.route("/items/<item_id>/", methods=["POST"])
@login_required
def items_set_checked(item_id):

    i = Item.query.get(item_id)
    i.check = True
    db.session().commit()
  
    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)
    
    if not form.validate():
        return render_template("items/new.html", form = form)
    
    i = Item(form.name.data)
    i.check = form.check.data

    db.session().add(i)
    db.session().commit()
  
    return redirect(url_for("items_index"))

#@app.route("/items/<item_id>/", methods=["POST"])
#def items_remove(item_id):
#    i = Item.query.remove(item_id)
#    
#    return redirect(url_for("items_index"))