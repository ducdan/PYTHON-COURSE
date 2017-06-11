from project import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, or_


db = SQLAlchemy(app)

class Song(db.Model):
    __tablename__ = 'songs'

    id = Column('id',Integer, primary_key=True)
    file_id = Column('file_id',Integer, ForeignKey('files.id'))
    file = db.relationship('File', backref='song', uselist=False)

    def as_dictionary(self):
        specific_song = Song.query.filter_by(id=self.id).first()
        specific_file = File.query.filter_by(id=specific_song.file_id).first()
        data = {'id': specific_song.id,
                'file': {
                    'id': specific_file.id,
                    'name': specific_file.filename
                        }
                }
        return data

class File(db.Model):
    __tablename__ = 'files'

    id = Column('id',Integer, primary_key=True)
    filename = Column('filename', String)

    def __init__(self,id, filename):
        self.id = id
        self.filename = filename

    def as_dictionary(self):
        specific_file = File.query.filter_by(id=self.id).first()
        data = {'id' : specific_file.id,
                'name': specific_file.filename}
        return data