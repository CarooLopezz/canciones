# crear ,leer,actualizar y eliminar los datos de los vengadores logica
import os
from flask import Blueprint
from backend.models.db import db
from backend.models.canciones import Musica  # tu modelo se llama Musica, está bien así

# El blueprint se llama 'musica', pero el archivo sigue en la carpeta 'canciones'
musica = Blueprint('musica', __name__, url_prefix='/musica')


@musica.route('/', methods=['GET'])
def listar_canciones():
    canciones_activas = Musica.query.filter_by(activo=True).order_by(Musica.id).all()
    salida = ""
    for c in canciones_activas:
        salida += f"{c.id} | {c.cancion} | {c.artista} | {c.duracion} seg\n"
    return f"<pre>{salida}</pre>"


@musica.route('/duracion', methods=['GET'])
def listar_por_duracion():
    canciones = Musica.query.filter_by(activo=True).order_by(Musica.duracion).all()
    salida = ""
    for c in canciones:
        salida += f"{c.id} | {c.cancion} | {c.artista} | {c.duracion} seg\n"
    return f"<pre>{salida}</pre>"


@musica.route('/baja/<int:id>', methods=['GET'])
def dar_de_baja(id):
    cancion = Musica.query.get_or_404(id)
    if not cancion.activo:
        return f"<pre>La canción '{cancion.cancion}' ya estaba dada de baja.</pre>"
    cancion.activo = False
    db.session.commit()
    return f"<pre>Canción '{cancion.cancion}' dada de baja correctamente.</pre>"
