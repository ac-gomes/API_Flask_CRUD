from flask import Blueprint, cli
from ..extentions.database import mongo
import pandas as pd
import click
import json


product_cm = Blueprint("product_cm", __name__)


@product_cm.cli.command("import")
@click.argument("file")
def import_file(file):
    collection = mongo.db.products
    data = pd.read_csv(file)
    json_data = json.loads(data.to_json(orient='records'))
    collection.insert(json_data)
    return collection.count
