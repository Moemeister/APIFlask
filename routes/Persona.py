from flask import Blueprint, jsonify, request, abort

# Entities
from models.entities.Persona import Persona, db

main = Blueprint('persona_blueprint', __name__)

@main.route('/obtenerTodos')
def get_personas():
    try:
        persona = Persona.query.all()
        return jsonify([p.to_json() for p in persona])


    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/one/<int:id>', methods=['GET']) 
def get_one_persona(id):
    try:
        persona = Persona.query.get(id)
        return jsonify(persona.to_json())

    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500
    
@main.route('/addPersona', methods=['POST'])
def create_persona():
    if not request.json:
        abort(400)
    persona = Persona(
        nombre=request.json.get('nombre'),
        apellido=request.json.get('apellido')
    )
    db.session.add(persona)
    db.session.commit()
    return jsonify(persona.to_json()), 201

@main.route("/delete/<int:id>", methods=["DELETE"])
def delete_persona(id):
    persona = Persona.query.get(id)
    if persona is None:
        abort(404)
    db.session.delete(persona)
    db.session.commit()
    return jsonify({'result': 'Se borro la persona'})

@main.route('/update/<int:id>', methods=['PUT'])
def update_persona(id):
    if not request.json:
        abort(400)
    persona = Persona.query.get(id)
    if persona is None:
        abort(404)
    persona.nombre = request.json.get('nombre', persona.nombre)
    persona.apellido = request.json.get('apellido', persona.apellido)
    db.session.commit()
    return jsonify(persona.to_json())