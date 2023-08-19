from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido
        }
