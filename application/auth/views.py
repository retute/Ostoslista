from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
#from test.test_logging import TestUDPServer

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # lis‰‰ t‰h‰n ehk‰

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Username or password didn't match. Try again!")

    login_user(user)
    
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/create", methods=["GET", "POST"])
def auth_create():
    form = LoginForm(request.form)
    
    if not form.validate():
        return render_template("auth/new.html", form = form)
    
    u = User(form.username.data, form.password.data)
    tryu = User.query.filter_by(username=form.username.data).first()
    if tryu:
        return render_template("auth/new.html", form = form,
                               error = "Username is not available.")

    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("index"))

