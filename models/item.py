import sys
from extensions import db
from models.category import Category

from http import HTTPStatus

# User Attributes
class Item(db.Model):
    
    __tablename__ = 'item'

    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(225), nullable=False)
    category_cat_id = db.Column(db.Integer, db.ForeignKey('Category.cat_id'), nullable=False)

    associated_holders = db.relationship('Holder', secondary='holder_has_item', backref='items', overlaps="associated_items,items")
  

    @property
    def data(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'description': self.description,
            'category_cat_id': self.category_cat_id,
        }
    
    # Save the record
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
    
    @classmethod
    def get_id_by_id(cls, item_id):
        print(item_id)
        return cls.query.get(item_id)


    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(id == id).first()
    
  
    @classmethod
    def update(cls, item_id, data):
        item = cls.query.get(item_id)

        if item:
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            item.category_cat_id = data.get('category_cat_id', item.category_cat_id)

            db.session.commit()

            return item.data 
        else:
            return None

    @classmethod
    def delete(cls, item_id):
        from models.holder_has_item import HolderHasItem
        x = HolderHasItem.get_all()
        for i in x:
            
            if i['item_item_id'] == item_id:

                return {'message': 'Item cannot be deleted '}


        Item = cls.query.get(item_id)

        if Item is None:
            return {'message': 'Item not found'}

        db.session.delete(Item)
        db.session.commit()

        updated_holders = cls.get_all()  

        return {'data': updated_holders}
    