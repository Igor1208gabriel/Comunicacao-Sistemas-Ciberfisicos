from . import db


class Robo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    status = db.Column(db.String(30))


class Missao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200))
    local = db.Column(db.String(100))
    status = db.Column(db.String(30))
    robo_id = db.Column(db.Integer, db.ForeignKey("robo.id"))
