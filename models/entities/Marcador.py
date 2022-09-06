from app import db

class Marcador(db.Model):
    __tablename__ = 'marcador'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)

    def __init__(self, id, fecha, hora):
        self.id = id
        self.fecha = fecha
        self.hora = hora