import sys
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from config import Config
from extensions import db
from resources.category import CategoryListResourse, CategoryResourse
from resources.item import ItemListResource, ItemResource
from resources.holder_has_item import HolderHasItemListResource, HolderHasItemResource
from resources.holder import HolderListResource, HolderResourse

def create_app():
    print("Hello", file=sys.stderr)
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)
    api.add_resource(CategoryListResourse, '/category')
    api.add_resource(CategoryResourse, '/category/<int:cat_id>')
    api.add_resource(ItemListResource, '/item')
    api.add_resource(ItemResource, '/item/<int:item_id>')
    api.add_resource(HolderHasItemListResource, '/holderhasitem')
    # api.add_resource(HolderHasItemResource, '/holderhasitem/<int:holder_has_item.id>')
    api.add_resource(HolderListResource, '/holder')
    api.add_resource(HolderResourse, '/holder/<int:holder_id>')

if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
