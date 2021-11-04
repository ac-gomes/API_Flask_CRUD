from flask import Blueprint, session, request, render_template, redirect, flash, url_for
from werkzeug.security import check_password_hash
from ..extentions.database import mongo

User = Blueprint("User", __name__)


@User.route("/")
def index():
    return redirect(url_for("User.login"))


@User.route("/home")
def home():
    if "username" in session:
        return render_template("usuarios/main.html")
    else:
        return redirect(url_for("User.index"))


@User.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("User.home"))
    elif request.method == "POST":
        username = request.form.get("usuario")
        password = request.form.get("senha")

        userFound = mongo.db.users.find_one({"name": username})
        if userFound:
            validUser = userFound["name"]
            validPassword = userFound["password"]

            if check_password_hash(validPassword, password):
                session["username"] = validUser
                return redirect(url_for("User.home"))
            else:
                flash("Senha Incorreta", "error")
                return render_template("usuarios/login.html")
    else:
        flash("Usuário não encontrado")
        render_template("usuarios/login.html")
    return render_template("usuarios/login.html")


@User.route("/logout", methods=["GET"])
def logout():
    session.pop("username", None)
    flash("Logout Efetuado!")
    return redirect(url_for("User.login"))
