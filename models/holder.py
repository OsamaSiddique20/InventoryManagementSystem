import sys
from extensions import db
from datetime import datetime

from http import HTTPStatus

class Holder(db.Model):
    __tablename__ = 'holder'

    holder_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, default=None, nullable=True)
    location = db.Column(db.String(45), nullable=True)

    associated_items  = db.relationship('Item', secondary='holder_has_item', backref='holders')
    @property
    def data(self):
        return {
            'holder_id': self.holder_id,
            'name': self.name,
            'type': self.type,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date) if self.end_date else None,
            'location': self.location,
        }
    

    @classmethod
    def update(cls, holder_id, data):
        holder = cls.query.get(holder_id)

        if holder:
            holder.name = data.get('name', holder.name)
            holder.type = data.get('type', holder.type)
            holder.start_date = data.get('start_date', holder.start_date)
            holder.end_date = data.get('end_date', holder.end_date)
            holder.location = data.get('location', holder.location)

            db.session.commit()
            return holder.data 
        else:
            return None

    @classmethod
    def delete(cls, holder_id):
        from models.holder_has_item import HolderHasItem
        x = HolderHasItem.get_all()
        for i in x:
            
            if i['holder_holder_id'] == holder_id:

                return {'message': 'Holder cannot be deleted '}


        holder = cls.query.get(holder_id)

        if holder is None:
            return {'message': 'Holder not found'}

        db.session.delete(holder)
        db.session.commit()

        updated_holders = cls.get_all()  

        return {'data': updated_holders}
    

    @classmethod
    def get_id_by_id(cls, holder_id):
        print(holder_id)
        return cls.query.get(holder_id)
    

    @classmethod
    def get_all(cls):
        r = cls.query.all()

        result = []
        for i in r:
            result.append(i.data)

        return result
    
    def save(self):
        db.session.add(self)
        db.session.commit()