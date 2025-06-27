
from backend.models.db import db

class Musica(db.Model):
    __tablename__ = 'musica'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cancion = db.Column(db.String(100), nullable=False)
    artista = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100), nullable=True)
    anio = db.Column(db.Integer, nullable=True)
    duracion = db.Column(db.Integer, nullable=True)  # en segundos
    fecha_lanzamiento = db.Column(db.Date, nullable=True)
    hora_estreno = db.Column(db.Time, nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    email_contacto = db.Column(db.String(100), nullable=True)
    activo = db.Column(db.Boolean, default=True)

    """ def __init__(self, cancion, artista, album=None, anio=None, duracion=None,
                fecha_lanzamiento=None, hora_estreno=None, descripcion=None, email_contacto=None, activo=True):
        self.cancion = cancion
        self.artista = artista
        self.album = album
        self.anio = anio
        self.duracion = duracion
        self.fecha_lanzamiento = fecha_lanzamiento
        self.hora_estreno = hora_estreno
        self.descripcion = descripcion
        self.email_contacto = email_contacto
        self.activo = activo """

    def serialize(self):
        return {
            'id': self.id,
            'cancion': self.cancion,
            'artista': self.artista,
            'album': self.album,
            'anio': self.anio,
            'duracion': self.duracion,
            'fecha_lanzamiento': self.fecha_lanzamiento.isoformat() if self.fecha_lanzamiento else None,
            'hora_estreno': self.hora_estreno.isoformat() if self.hora_estreno else None,
            'descripcion': self.descripcion,
            'email_contacto': self.email_contacto,
            'activo': self.activo
        }