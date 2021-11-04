from flask import Blueprint, request, session, redirect, url_for, flash
from flask.templating import render_template
from ..extentions.database import mongo

product = Blueprint('product', __name__)


@product.route('/list')
def listProducts():
    if "username" in session:
        products = mongo.db.products.find()
        return render_template("produtos/list.html", produtos=products)
    else:
        return redirect(url_for("User.index"))


@product.route('/insert', methods=["GET", "POST"])
def insetProduct():
    if request.method == "GET":
        return render_template("produtos/insert.html")
    else:
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        preco = request.form.get('preco')
        categoria = request.form.get('categoria')
        estoque = request.form.get('estoque')

    if not nome or len(nome) > 50:
        flash("Campo 'nome é obrigatório e deve der menor que 50 caracteres")
    elif not quantidade or not quantidade.isdigit() or int(quantidade) <= 0:
        flash("Campo 'quantidade' é o brigatório!")
    elif not preco:
        flash("Campo 'preco' é obrigatório")
    elif not categoria:
        flash("Campo 'categoria' é obrigatório")
    elif not estoque:
        flash("Campo 'estoque' é obrigatório")
    else:
        mongo.db.products.insert_one({
            "produto": nome,
            "quantidade": quantidade,
            "preco": preco,
            "categoria": categoria,
            "estoque": estoque,
            "valor total": (float(quantidade) * float(preco))
        })

        flash("produto cadastrado")
    return redirect(url_for("product.listProducts"))


@product.route('/edit')
def editProduct():
    return "edit"


@product.route('/delete')
def deleteProduct():
    return "delete"
