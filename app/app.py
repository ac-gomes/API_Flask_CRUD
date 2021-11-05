from flask import Flask
from .routes.User import User
from .routes.product import product
from .extentions import database
from .commands.userCommands import userCommands
from .config.hellpers import config
from .commands.productCommands import product_cm


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = config["MONGO_URI"]
    app.config["SECRET_KEY"] = config["SECRET_KEY"]
    app.register_blueprint(User)
    app.register_blueprint(product)
    app.register_blueprint(userCommands)
    app.register_blueprint(product_cm)
    database.init_app(app)

    return app
