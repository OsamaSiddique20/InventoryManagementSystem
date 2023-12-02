import sys
from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.category import Category


class CategoryListResourse(Resource):

    def get(self):
        data = Category.get_all()

        if data is None:
            return {'message': 'Category not found'}, HTTPStatus.NOT_FOUND

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        for i in data:
            if data.get(i) == '':
                return {'Message':'Please fill all fields'},HTTPStatus.NOT_FOUND
        category = Category(cat_name=data['cat_name'],
                    cat_desc=data['cat_desc'])
        category.save()

        return category.data, HTTPStatus.CREATED


class CategoryResourse(Resource):

    def get(self, recipe_id):
        category = category.get_by_id(recipe_id)

        if category is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return category.data, HTTPStatus.OK

    def put(self, cat_id):
        data = request.get_json()
        return Category.update(cat_id, data)

    def delete(self, cat_id):
        return Category.delete(cat_id)


