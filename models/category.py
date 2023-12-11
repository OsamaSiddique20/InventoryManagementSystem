import sys
from extensions import db
from http import HTTPStatus

class Category(db.Model):
    __tablename__ = 'Category'
    cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cat_name = db.Column(db.String(255), nullable=False)
    cat_desc = db.Column(db.Text)
    items = db.relationship("Item", backref="Category")
    
    @property
    def data(self):
        return {
            'cat_id': self.cat_id,
            'cat_name': self.cat_name,
            'cat_desc': self.cat_desc}
        
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
    def get_id_by_id(cls, cat_id):
        print(cat_id)
        return cls.query.filter_by(cat_id=cat_id).first().cat_id

    @classmethod
    def update(cls, cat_id, data):
        category = cls.query.get(cat_id)
        if category:
            category.cat_name = data.get('cat_name', category.cat_name)
            category.cat_desc = data.get('cat_desc', category.cat_desc)
            db.session.commit()
            return category.data
        else:
            return None

    @classmethod
    def delete(cls, id):
        item  = cls.query.filter(cls.cat_id==id).first()
        if item is None:
            return {'message': 'Category not found'}, HTTPStatus.NOT_FOUND
        db.session.delete(item)
        db.session.commit()
        updated_items = cls.get_all()
        return {'data': updated_items}, HTTPStatus.OK
