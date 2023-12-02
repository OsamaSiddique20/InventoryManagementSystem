import sys
from extensions import db

from http import HTTPStatus
from models.item import Item
from models.holder import Holder


class HolderHasItem(db.Model):
    __tablename__ = 'holder_has_item'

    holder_holder_id = db.Column(db.Integer, db.ForeignKey('holder.holder_id'), primary_key=True)
    item_item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'), primary_key=True)
    quantity = db.Column(db.String(45))
    serial_num = db.Column(db.String(45))

    item = db.relationship('Item', backref='holder_has_item')
    holder = db.relationship('Holder', backref='holder_has_item')

    @property
    def data(self):
        return {
            'holder_holder_id': self.holder_holder_id,
            'item_item_id': self.item_item_id,
            'quantity': self.quantity,
            'serial_num': self.serial_num,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()

        result = []

        for i in r:
            result.append(i.data)

        return result
    
    # @classmethod
    # def get_id_by_id(cls, cat_id):
    #     print(cat_id)
    #     return cls.query.filter_by(cat_id=cat_id).first().cat_id
    

    @classmethod
    def update(cls, holder_id, item_id, data):
        holder_has_item = cls.query.get((holder_id, item_id))

        if holder_has_item:
            holder_has_item.quantity = data.get('quantity', holder_has_item.quantity)
            holder_has_item.serial_num = data.get('serial_num', holder_has_item.serial_num)

            db.session.commit()

            return holder_has_item.data
        else:
            return None


    @classmethod
    def delete(cls, holder_id, item_id):
        holder_has_item = cls.query.filter_by(holder_holder_id=holder_id, item_item_id=item_id).first()

        if holder_has_item is None:
            return {'message': 'HolderHasItem not found'}, HTTPStatus.NOT_FOUND

        db.session.delete(holder_has_item)
        db.session.commit()

        updated_holder_has_items = cls.get_all()  # Assuming you have a get_all method to fetch all records

        return {'data': updated_holder_has_items}, HTTPStatus.OK