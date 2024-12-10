from flask import request,redirect,url_for,Blueprint
from datetime import datetime

from models.producto_model import Producto
from views import producto_view

producto_bp=Blueprint('blog',__name__,url_prefix="/blog")

@producto_bp.route("/")
def index():
    productos=Producto.get_all()
    return producto_view.list(productos)
@producto_bp.route("/create",methods=['GET','POST'])
def create():
    if request.method=="POST":
        descripcion=request.form["descripcion"]
        titulo=request.form["titulo"]
        fecha_str=request.form["fecha"]
        fecha=datetime.strptime(fecha_str,'%Y-%m-%d').date()
        contenido=request.form["contenido"]
        url=request.form["url"]

        producto=Producto(descripcion,titulo,fecha,url,contenido)
        producto.save()
        return redirect(url_for('blog.edit',id=producto.id))
    return producto_view.create()

@producto_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    producto=Producto.get_by_id(id)   
    if request.method=='POST':
        descripcion=request.form['descripcion']
        titulo=request.form['titulo']
        fecha_str=request.form['fecha']
        fecha=datetime.strptime(fecha_str,'%Y-%m-%d').date()
        contenido=request.form['contenido']
        url=request.form['url']
      
        #actualizar
        producto.update(descripcion=descripcion,titulo=titulo,fecha=fecha,contenido=contenido,url=url)
        return redirect(url_for('blog.index'))
    return producto_view.edit(producto)
@producto_bp.route("/delete/<int:id>")
def delete(id):
    producto=Producto.get_by_id(id)
    producto.delete()
    return redirect(url_for('blog.index'))