from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.item import Item

class ItemListResource(Resource):
    def get(self):
        data = Item.get_all()

        if not data:
            return {'message': 'Item not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        for i in data:
           
            if data.get(i) == '':
                return {'Message':'Please fill all fields'},HTTPStatus.NOT_FOUND
        item = Item(
            name=data['name'],
            description=data['description'],
            category_cat_id=data['category_cat_id'],
        )
        item.save()

        return item.data, HTTPStatus.CREATED

class ItemResource(Resource):
    def get(self, item_id):
        item = Item.get_by_id(item_id)

        if not item:
            return {'message': 'Item not found'}, HTTPStatus.NOT_FOUND

        return item.data, HTTPStatus.OK

    def put(self, item_id):
        data = request.get_json()
        updated_item = Item.update(item_id, data)

        if updated_item:
            return updated_item, HTTPStatus.OK
        else:
            return {'message': 'Item not found'}, HTTPStatus.NOT_FOUND

    def delete(self, item_id):
        result = Item.delete(item_id)

        if 'data' in result:
            return result['data'], HTTPStatus.OK
        else:
            return {'message': 'Item cannot be deleted because a holder pocesses it'}, HTTPStatus.NOT_FOUND

