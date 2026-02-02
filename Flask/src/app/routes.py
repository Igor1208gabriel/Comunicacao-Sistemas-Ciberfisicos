from flask import Blueprint, request, jsonify
from .models import Robo, Missao, Sensor
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """
    Endpoint de verificação da API
    ---
    tags:
      - Sistema
    responses:
      200:
        description: API em execução
    """
    return jsonify({"message": "API ON!"})


# =========================
# CRUD ROBÔ
# =========================


@main.route("/robos", methods=["POST"])
def criar_robo():
    """
    Cria um novo robô
    ---
    tags:
      - Robôs
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - nome
              - tipo
              - status
            properties:
              nome:
                type: string
                example: Robo Explorador
              tipo:
                type: string
                example: exploracao
              status:
                type: string
                example: ativo
    responses:
      201:
        description: Robô criado com sucesso
    """
    data = request.json
    robo = Robo(nome=data["nome"], tipo=data["tipo"], status=data["status"])
    db.session.add(robo)
    db.session.commit()
    return jsonify(robo.to_dict()), 201


@main.route("/robos", methods=["GET"])
def listar_robos():
    """
    Lista todos os robôs cadastrados
    ---
    tags:
      - Robôs
    responses:
      200:
        description: Lista de robôs
    """
    robos = Robo.query.all()
    return jsonify([r.to_dict() for r in robos])


@main.route("/robos/<int:id>", methods=["GET"])
def obter_robo(id):
    """
    Obtém os dados de um robô específico
    ---
    tags:
      - Robôs
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Robô encontrado
      404:
        description: Robô não encontrado
    """
    robo = Robo.query.get_or_404(id)
    return jsonify(robo.to_dict())


@main.route("/robos/<int:id>", methods=["PUT"])
def atualizar_robo(id):
    """
    Atualiza os dados de um robô
    ---
    tags:
      - Robôs
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
                example: Robo Atualizado
              tipo:
                type: string
                example: vigilancia
              status:
                type: string
                example: manutencao
    responses:
      200:
        description: Robô atualizado com sucesso
      404:
        description: Robô não encontrado
    """
    robo = Robo.query.get_or_404(id)
    data = request.json

    robo.nome = data.get("nome", robo.nome)
    robo.tipo = data.get("tipo", robo.tipo)
    robo.status = data.get("status", robo.status)

    db.session.commit()
    return jsonify(robo.to_dict())


@main.route("/robos/<int:id>", methods=["DELETE"])
def deletar_robo(id):
    """
    Remove um robô do sistema
    ---
    tags:
      - Robôs
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Robô removido com sucesso
      404:
        description: Robô não encontrado
    """
    robo = Robo.query.get_or_404(id)
    db.session.delete(robo)
    db.session.commit()
    return "", 204


# =========================
# CRUD SENSOR
# =========================


@main.route("/robos/<int:robo_id>/sensores", methods=["POST"])
def criar_sensor(robo_id):
    """
    Adiciona um sensor a um robô
    ---
    tags:
      - Sensores
    parameters:
      - in: path
        name: robo_id
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - tipo
              - modelo
              - status
            properties:
              tipo:
                type: string
                example: ultrassonico
              modelo:
                type: string
                example: HC-SR04
              status:
                type: string
                example: ativo
    responses:
      201:
        description: Sensor criado com sucesso
      404:
        description: Robô não encontrado
    """
    data = request.json
    sensor = Sensor(
        tipo=data["tipo"], modelo=data["modelo"], status=data["status"], robo_id=robo_id
    )
    db.session.add(sensor)
    db.session.commit()
    return jsonify(sensor.to_dict()), 201


@main.route("/robos/<int:robo_id>/sensores", methods=["GET"])
def listar_sensores(robo_id):
    """
    Lista todos os sensores de um robô
    ---
    tags:
      - Sensores
    parameters:
      - in: path
        name: robo_id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Lista de sensores do robô
    """
    sensores = Sensor.query.filter_by(robo_id=robo_id).all()
    return jsonify([s.to_dict() for s in sensores])


@main.route("/sensores/<int:id>", methods=["DELETE"])
def deletar_sensor(id):
    """
    Remove um sensor do sistema
    ---
    tags:
      - Sensores
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      204:
        description: Sensor removido com sucesso
      404:
        description: Sensor não encontrado
    """
    sensor = Sensor.query.get_or_404(id)
    db.session.delete(sensor)
    db.session.commit()
    return "", 204
