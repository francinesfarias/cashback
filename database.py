from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))
    valor = db.Column(db.Float)
    desconto = db.Column(db.Float)
    cashback = db.Column(db.Float)