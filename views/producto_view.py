from flask import render_template
def list(productos):
    return render_template('blog/index.html',productos=productos)
def create():
    return render_template('blog/create.html')
def edit(producto):
    return render_template('blog/edit.html',producto=producto)
    