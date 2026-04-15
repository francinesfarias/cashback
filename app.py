from flask import Flask, request, jsonify, send_from_directory
from cashback import calcular_cashback
from database import db, Consulta
import os

app = Flask(__name__)

# Usar DATABASE_URL para hospedagem ou SQLite local
database_url = os.environ.get('DATABASE_URL', 'sqlite:///cashback.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return send_from_directory('static', 'index.html')

@app.route("/cashback", methods=["POST"])
def cashback():
    data = request.get_json()

    valor = float(data.get("valor"))
    desconto = float(data.get("desconto"))
    vip = bool(data.get("vip"))

    resultado = calcular_cashback(valor, desconto, vip)

    ip = request.remote_addr

    nova = Consulta(
        ip=ip,
        valor=valor,
        desconto=desconto,
        cashback=resultado
    )

    db.session.add(nova)
    db.session.commit()

    return jsonify({
        "cashback": resultado
    })

@app.route("/historico", methods=["GET"])
def historico():
    ip = request.remote_addr

    consultas = Consulta.query.filter_by(ip=ip).all()

    return jsonify([
        {
            "valor": c.valor,
            "desconto": c.desconto,
            "cashback": c.cashback
        }
        for c in consultas
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)