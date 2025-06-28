import os
from flask import Blueprint, jsonify
from backend.models.db import db
from backend.models.canciones import Musica 


musica = Blueprint('musica', __name__, url_prefix='/musica')

@musica.route('/api/spotify/canciones', methods=['GET'])
def get_canciones_activas():
    canciones = Musica.query.filter_by(activo=True).all()
    return jsonify([c.serialize() for c in canciones])


@musica.route('/api/spotify/canciones/<int:id>', methods=['DELETE'])
def baja_logica_cancion(id):
    cancion = Musica.query.get_or_404(id)
    if not cancion.activo:
        return jsonify({"mensaje": "La canción ya estaba inactiva."}), 400
    cancion.activo = False
    db.session.commit()
    return jsonify({"mensaje": f"Canción '{cancion.cancion}' dada de baja."})


@musica.route('/api/spotify/canciones/clasificadas', methods=['GET'])
def clasificar_por_duracion():
    canciones = Musica.query.filter_by(activo=True).all()

    cortas = []
    medias = []
    largas = []

    for c in canciones:
        if c.duracion is None:
            continue 
        if c.duracion < 180:
            cortas.append(c.serialize())
        elif 180 <= c.duracion <= 240:
            medias.append(c.serialize())
        elif c.duracion > 340:
            largas.append(c.serialize())

    return jsonify({
        "cortas": cortas,
        "medias": medias,
        "largas": largas
    })
