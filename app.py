from flask import Flask, render_template, json, request, Response
import config
import requests
import banco
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def index():
    hoje = datetime.today().strftime('%Y-%m-%d')
    return render_template('index/index.html', hoje=hoje)

@app.get('/sobre')
def sobre():
    return render_template('index/sobre.html', titulo='Sobre Nós')

@app.get('/obterTemperaturas')
def obterTemperaturas():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("temperatura")

    resultado = requests.get(f'{config.url_api}?sensor=temperature&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirTemperaturas(dados_novos)

    dados = banco.listarTemperaturas()

    return json.jsonify(dados)

@app.get('/obterPresenca')
def obterPresenca():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("ocupado")

    resultado = requests.get(f'{config.url_api}?sensor=presenca&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirPresenca(dados_novos)

    dados = banco.listarPresenca()

    return json.jsonify(dados)

@app.post('/criar')
def criar():
    dados = request.json
    print(dados['id'])
    print(dados['nome'])
    return Response(status=204)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
