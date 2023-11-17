from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.holder_has_item import HolderHasItem

class HolderHasItemListResource(Resource):
    def get(self):
        data = HolderHasItem.get_all()

        if not data:
            return {'message': 'Holder Has Item not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        holder_has_item = HolderHasItem(
            holder_holder_id=data['holder_holder_id'],
            item_item_id=data['item_item_id'],
            quantity=data.get('quantity'),  # Assuming 'quantity' is an optional field
            serial_num=data.get('serial_num')  # Assuming 'serial_num' is an optional field
        )
        holder_has_item.save()

        return holder_has_item.data, HTTPStatus.CREATED

class HolderHasItemResource(Resource):
    def get(self, holder_holder_id, item_item_id):
        holder_has_item = HolderHasItem.get_by_ids(holder_holder_id, item_item_id)

        if not holder_has_item:
            return {'message': 'Holder Has Item not found'}, HTTPStatus.NOT_FOUND

        return holder_has_item.data, HTTPStatus.OK

    def put(self, holder_holder_id, item_item_id):
        data = request.get_json()
        updated_holder_has_item = HolderHasItem.update(holder_holder_id, item_item_id, data)

        if updated_holder_has_item:
            return updated_holder_has_item, HTTPStatus.OK
        else:
            return {'message': 'Holder Has Item not found'}, HTTPStatus.NOT_FOUND

    def delete(self, holder_holder_id, item_item_id):
        result = HolderHasItem.delete(holder_holder_id, item_item_id)

        if 'data' in result:
            return result['data'], HTTPStatus.OK
        else:
            return {'message': 'Holder Has Item not found'}, HTTPStatus.NOT_FOUND
