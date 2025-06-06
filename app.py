from flask import Flask, render_template, json, request, Response
import config
import requests
import banco
from datetime import datetime, timedelta

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index/sobre.html', titulo='Sobre Nós')

@app.get('/dashboard')
def dashboard():
    data_inicial = (datetime.today() + timedelta(days=-1)).strftime('%Y-%m-%d')
    data_final = datetime.today().strftime('%Y-%m-%d')
    return render_template('index/index.html', data_inicial=data_inicial, data_final=data_final)

@app.get('/tempoReal')
def tempoReal():
    return render_template('index/tempoReal.html')

@app.get('/obterDados')
def obterDados():
    data_inicial = request.args.get('data_inicial')
    data_final = request.args.get('data_final')

    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("temperatura")

    resultado = requests.get(f'{config.url_api}?sensor=temperature&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirTemperatura(dados_novos)

    temperatura = banco.listarTemperatura(data_inicial, data_final)

    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("passagem")

    resultado = requests.get(f'{config.url_api}?sensor=passage&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirPassagem(dados_novos)

    passagem = banco.listarPassagem(data_inicial, data_final)

    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("creative")

    if maior_id < 170000:
        maior_id = 170000

    resultado = requests.get(f'{config.url_api}?sensor=creative&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirCreative(dados_novos)

    creative = banco.listarCreative(data_inicial, data_final)

    return json.jsonify({
        "temperatura": temperatura,
        "passagem": passagem,
        "creative": creative
    })

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

@app.get('/obterPCATempoReal')
def obterPCATempoReal():
    # Obter o maior id do banco
    maior_id = banco.obterIdMaximo("pca")

    resultado = requests.get(f'{config.url_api}?sensor=pca&id_inferior={maior_id}')
    dados_novos = resultado.json()

	# Inserir os dados novos no banco
    if dados_novos and len(dados_novos) > 0:
        banco.inserirPCA(dados_novos)

    dados = banco.listarPCATempoReal()

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
