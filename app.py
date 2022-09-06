from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from configuration import configuration
from routes import Marcador

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config('DB_URI')
app.debug = True

db = SQLAlchemy(app)

def page_not_found(e):
    return '<h1>Page not found</h1', 404

if __name__ == '__main__':
    app.config.from_object(configuration['development'])

    # Blueprints
    app.register_blueprint(Marcador.main, url_prefix='/api/marcador')

    app.register_error_handler(404, page_not_found)
    app.run()