from flask import Flask, request
from controllers import usuario_controller,producto_controller
from database import db

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ventas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

app.register_blueprint(producto_controller.producto_bp)
    

@app.route("/")
def home():
    return "<h1>Aplicacion ventas</h1>"





if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)