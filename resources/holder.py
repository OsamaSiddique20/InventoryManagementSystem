from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.holder import Holder

class HolderListResource(Resource):
    def get(self):
        data = Holder.get_all()

        if not data:
            return {'message': 'Holder not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        for i in data:
            print(data.get(i))
            if data.get(i) == '':
                return {'Message':'Please fill all fields'},HTTPStatus.NOT_FOUND    
        holder = Holder(
            name=data['name'],
            type=data['type'],
            start_date=data['start_date'],
            end_date=data.get('end_date'), 
            location=data.get('location')  
        )
        holder.save()

        return holder.data, HTTPStatus.CREATED
    
 
class HolderResourse(Resource):
    def get(self, holder_id):
        holder = Holder.get_by_id(holder_id)

        if not holder:
            return {'message': 'Holder not found'}, HTTPStatus.NOT_FOUND

        return holder.data, HTTPStatus.OK

    def put(self, holder_id):
        data = request.get_json()
        updated_holder = Holder.update(holder_id, data)

        if updated_holder:
            return updated_holder, HTTPStatus.OK
        else:
            return {'message': 'Holder not found'}, HTTPStatus.NOT_FOUND

    def delete(self, holder_id):
        result = Holder.delete(holder_id)

        if 'data' in result:
            return result['data'], HTTPStatus.OK
        else:
            return {'message': 'Holder cannot be deleted because it has an item in possession'}, HTTPStatus.NOT_FOUND
