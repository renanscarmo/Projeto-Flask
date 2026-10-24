from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route("/")
def home():
    return{'mensagem':'Olá, DevSecOps!'}

@app.route("/saude")
def saude():
    return jsonify({"status":"ok"})

@app.route("/saudacao/<nome>")
def saudacao(nome):
    return jsonify ({"mensagem": f"Ola, {nome}!"})

@app.route("/mensagem", methods=["POST"])
def receber_mensagem():
    dados = request.get_json(silent=True)
    if not dados or "texto" not in dados:
        return jsonify({"erro":"Envie um Json com o campo texto"}), 400
    texto=str(dados["texto"])[:200]
    return jsonify({"recebido":texto}),201

@app.errorhandler(404)
def nao_encontrado(erro):
     return jsonify({"erro":"Rota não encontrada"}), 404
    
if __name__=="__main__":
    app.run()
    