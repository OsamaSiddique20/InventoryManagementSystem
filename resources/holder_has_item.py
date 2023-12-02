from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.holder_has_item import HolderHasItem
from models.holder import Holder
from models.item import Item

class HolderHasItemListResource(Resource):
    def get(self):
        data = HolderHasItem.get_all()

        if not data:
            return {'message': 'Holder Has Item not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        for i in data:
            print(data.get(i))
            if data.get(i) == '':
                return {'Message':'Please fill all fields'},HTTPStatus.NOT_FOUND
        x = Holder.get_id_by_id(data['holder_holder_id'])
        y = Item.get_id_by_id(data['item_item_id'])
        if x == None:
            return {"message":'Holder_id doesnt exist'}
        if y == None:
            return {"message":'Item_id doesnt exist '}

        holder_has_item = HolderHasItem(
            holder_holder_id=data['holder_holder_id'],
            item_item_id=data['item_item_id'],
            quantity=data.get('quantity'),  
            serial_num=data.get('serial_num')  
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
        return {'Message':'You do not have permission to delete '}
