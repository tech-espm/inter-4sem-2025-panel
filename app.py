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
        banco.inserirTemperatura(dados_novos)

    dados = banco.listarTemperatura()

    return json.jsonify(dados)

@app.get('/obterPresenca')
def obterPresenca():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("presenca")

    resultado = requests.get(f'{config.url_api}?sensor=presenca&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirPresenca(dados_novos)

    dados = banco.listarPresenca()

    return json.jsonify(dados)

@app.get('/obterPassagem')
def obterPassagem():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("passagem")

    resultado = requests.get(f'{config.url_api}?sensor=passagem&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirPassagem(dados_novos)

    dados = banco.listarPassagem()

    return json.jsonify(dados)

@app.get('/obterOdor')
def obterOdor():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("odor")

    resultado = requests.get(f'{config.url_api}?sensor=odor&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirOdor(dados_novos)

    dados = banco.listarOdor()

    return json.jsonify(dados)

@app.get('/obterPCA')
def obterPCA():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("pca")

    resultado = requests.get(f'{config.url_api}?sensor=pca&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirPCA(dados_novos)

    dados = banco.listarPCA()

    return json.jsonify(dados)

@app.get('/obterCreative')
def obterCreative():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("creative")

    resultado = requests.get(f'{config.url_api}?sensor=creative&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirCreative(dados_novos)

    dados = banco.listarCreative()

    return json.jsonify(dados)

@app.get('/obterSolo')
def obterSolo():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("solo")

    resultado = requests.get(f'{config.url_api}?sensor=solo&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirSolo(dados_novos)

    dados = banco.listarSolo()

    return json.jsonify(dados)


@app.post('/criar')
def criar():
    dados = request.json
    print(dados['id'])
    print(dados['nome'])
    return Response(status=204)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
