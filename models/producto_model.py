from database import db
from flask import request,redirect,url_for
from datetime import datetime


class Producto(db.Model):
    __tablename__='producto'

    id=db.Column(db.Integer,primary_key=True)
    titulo=db.Column(db.String(80),nullable=False)
    descripcion=db.Column(db.String(80),nullable=False)
    fecha=db.Column(db.DateTime,nullable=False)
    contenido=db.Column(db.String(80),nullable=False)
    url=db.Column(db.String(80),nullable=False)
    
    #ventas=db.relationship('Venta',back_populates='producto')

    def __init__(self,descripcion,titulo,fecha,contenido,url):
        self.descripcion=descripcion
        self.titulo=titulo
        self.fecha=fecha
        self.contenido=contenido
        self.url=url


    def save(self):
        db.session.add( self)
        db.session.commit()
    @staticmethod
    def get_all():
        return Producto.query.all()
    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)
    
    def update(self,descripcion=None,titulo=None,fecha=None,contenido=None,url=None):
        if descripcion and titulo and fecha and contenido and url:
            self.descripcion=descripcion
            self.titulo=titulo
            self.fecha=fecha
            self.contenido=contenido
            self.url=url
    
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
