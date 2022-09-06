from flask import Blueprint, jsonify

# Entities
from models.entities.Marcador import Marcador

main = Blueprint('marcador_blueprint', __name__)

@main.route('/')
def get_marcador():
    try:
        marcador = Marcador.query.all()
        output = []
        for marc in marcador:
            currMarcador = {}
            currMarcador['id']=marc.id
            currMarcador['fecha']=str(marc.fecha)
            currMarcador['hora']=str(marc.hora)
            output.append(currMarcador)
        return jsonify(output)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

