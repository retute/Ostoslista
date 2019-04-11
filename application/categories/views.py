from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.items.forms import ItemForm
from flask_login import login_required, current_user

@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all())

@app.route("/categories/new/")
@login_required
def categories_form():
    return render_template("categories/new.html", form = GategoryForm())

@app.route("/categories/<category_id>/", methods=["POST"])
@login_required
def categories_remove(category_id):
    return redirect(url_for("categories_index"))

@app.route("/categories/", methods=["POST"])
@login_required
def category_create():
    form = CategoryForm(request.form)
    
    if not form.validate():
        return render_template("category/new.html", form = form)
    
    c = Category(form.category.data)
#    c.size = 0
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("items_index"))

