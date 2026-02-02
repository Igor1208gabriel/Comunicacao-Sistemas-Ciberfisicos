from . import db


class Robo(db.Model):
    __tablename__ = "robos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(30), nullable=False)

    missoes = db.relationship("Missao", backref="robo", lazy=True)
    sensores = db.relationship("Sensor", backref="robo", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "status": self.status,
        }


class Missao(db.Model):
    __tablename__ = "missoes"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(30), nullable=False)

    robo_id = db.Column(db.Integer, db.ForeignKey("robos.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "local": self.local,
            "status": self.status,
            "robo_id": self.robo_id,
        }


class Sensor(db.Model):
    __tablename__ = "sensores"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(30), nullable=False)

    robo_id = db.Column(db.Integer, db.ForeignKey("robos.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "modelo": self.modelo,
            "status": self.status,
            "robo_id": self.robo_id,
        }
