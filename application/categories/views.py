from application import app, db
from flask import redirect, render_template, request, url_for
from application.categories.models import Category
from application.categories.forms import CategoryForm
from flask_login import login_required, current_user

@app.route("/categories", methods=["GET", "POST"])
@login_required
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all())

@app.route("/categories/new/")
@login_required
def categories_form():
    return render_template("categories/new.html", form = CategoryForm())

@app.route("/categories/remove/<category_id>/", methods=["POST"])
@login_required
def categories_remove(category_id):
    form=CategoryForm(request.form)
    c = Category.query.get(category_id)
    if c.size <= 0:
        db.session().delete(c)
        db.session().commit()
        return redirect(url_for("categories_index"))
    return redirect(url_for("categories_index"))

@app.route("/categories/", methods=["POST"])
@login_required
def category_create():
    form = CategoryForm(request.form)
    
    if not form.validate():
        return render_template("category/new.html", form = form)
    
    c = Category(form.name.data)
    c.account_id = current_user.id
    c.size = 0;

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("categories_index"))
