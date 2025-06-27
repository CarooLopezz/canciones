from flask import Flask
from backend.config.config import DATABASE_CONNECTION_URI
from backend.models.db import db
from backend.routes.canciones_routes import musica
from backend.models.canciones import Musica

app = Flask(__name__)
app.register_blueprint(musica)  

app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True  
app.secret_key = 'clave-repiola'

db.init_app(app)

with app.app_context():
    from backend.models.canciones import Musica
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
     app.run(host='127.0.0.1', port=5002,debug=True) #cambiar de puerto