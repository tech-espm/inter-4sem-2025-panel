# Vamos utilizar o pacote SQLAlchemy para acesso a banco de dados:
# https://docs.sqlalchemy.org
#
# Para isso, ele precisa ser instalado via pip (de preferência com o VS Code fechado):
# python -m pip install SQLAlchemy
#
# Além disso, o SQLAlchemy precisa de um driver do conexão ao banco. Isso depende do servidor
# (MySQL, Postgres, SQL Server, Oracle...) e do driver real. Vamos utilizar o driver MySQL-Connector,
# que também precisa ser instalado (de preferência com o VS Code fechado):
# python -m pip install mysql-connector-python
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from config import conexao_banco

# Como criar uma comunicação com o banco de dados:
# https://docs.sqlalchemy.org/en/14/core/engines.html
#
# Detalhes específicos ao MySQL
# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector
#
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
engine = create_engine(conexao_banco)

# A função text(), utilizada ao longo desse código, serve para encapsular um comando
# SQL qualquer, de modo que o SQLAlchemy possa entender!

def listarPessoas():
	# O with do Python é similar ao using do C#, ou o try with resources do Java.
	# Ele serve para limitar o escopo/vida do objeto automaticamente, garantindo
	# que recursos, como uma conexão com o banco, não sejam desperdiçados!
	with Session(engine) as sessao:
		pessoas = sessao.execute(text("SELECT id, nome, email FROM pessoa ORDER BY nome"))

		# Como cada registro retornado é uma tupla ordenada, é possível
		# utilizar a forma de enumeração de tuplas:
		for (id, nome, email) in pessoas:
			print(f'\nid: {id} / nome: {nome} / email: {email}')

		# Ou, se preferir, é possível retornar cada tupla, o que fica mais parecido
		# com outras linguagens de programação:
		#for pessoa in pessoas:
		#	print(f'\nid: {pessoa.id} / nome: {pessoa.nome} / email: {pessoa.email}')

def obterPessoa(id):
	with Session(engine) as sessao:
		parametros = {
			'id': id
		}

		# Mais informações sobre o método execute e sobre o resultado que ele retorna:
		# https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.execute
		# https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Result
		pessoa = sessao.execute(text("SELECT id, nome, email FROM pessoa WHERE id = :id"), parametros).first()

		if pessoa == None:
			print('Pessoa não encontrada!')
		else:
			print(f'\nid: {pessoa.id} / nome: {pessoa.nome} / email: {pessoa.email}')

def criarPessoa(nome, email):
	# É importante utilizar o método begin() para que a sessão seja comitada
	# automaticamente ao final, caso não ocorra uma exceção!
	# Isso não foi necessário nos outros exemplos porque nenhum dado estava sendo
	# alterado lá! Caso alguma exceção ocorra, rollback() será executado automaticamente,
	# e nenhuma alteração será persistida. Para mais informações de como explicitar
	# esse processo de commit() e rollback():
	# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#framing-out-a-begin-commit-rollback-block
	with Session(engine) as sessao, sessao.begin():
		pessoa = {
			'nome': nome,
			'email': email
		}

		sessao.execute(text("INSERT INTO pessoa (nome, email) VALUES (:nome, :email)"), pessoa)

		# Para inserir, ou atualizar, vários registros ao mesmo tempo, a forma mais rápida
		# é passar uma lista como segundo parâmetro:
		# lista = [ ... ]
		# sessao.execute(text("INSERT INTO pessoa (nome, email) VALUES (:nome, :email)"), lista)

# Para mais informações:
# https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html

def obterIdMaximo(tabela):
	with Session(engine) as sessao:
		registro = sessao.execute(text(f"SELECT MAX(id) id FROM {tabela}")).first()

		if registro == None or registro.id == None:
			return 0
		else:
			return registro.id

# Sensor Temperatura
def inserirTemperatura(registros):
	with Session(engine) as sessao, sessao.begin():
		for registro in registros:
			sessao.execute(text("INSERT INTO temperatura (id, data, id_sensor, delta, umidade, temperatura) VALUES (:id, :data, :id_sensor, :delta, :umidade, :temperatura)"), registro)

def listarTemperatura(data_inicial, data_final):

	with Session(engine) as sessao:
		parametros = {
			'data_inicial': data_inicial + ' 00:00:00',
			'data_final': data_final + ' 23:59:59'
		}

		registros = sessao.execute(text("""
select date_format(date(data), '%d/%m') dia, extract(hour from data) hora, cast(avg(temperatura) as float) temperatura
from temperatura
where id_sensor = 1 and data between :data_inicial and :data_final
group by dia, hora
order by dia, hora
		"""), parametros)
		temperaturas = []
		for registro in registros:
			temperaturas.append({
				"dia": registro.dia,
				"hora": registro.hora,
				"temperatura": registro.temperatura,
			})
		return temperaturas

# Sensor Presenca
def inserirPresenca(registros):
	with Session(engine) as sessao, sessao.begin():
		for registro in registros:
			sessao.execute(text("INSERT INTO presenca (id, data, id_sensor, delta, bateria, ocupado) VALUES (:id, :data, :id_sensor, :delta, :bateria, :ocupado)"), registro)

def listarPresenca():
	with Session(engine) as sessao:
		registros = sessao.execute(text("select id_sensor, date(data) dia, avg(delta) presenca_media from presenca where data between '2025-03-10 00:00:00' and '2025-03-14 23:59:59' and ocupado = 0 group by id_sensor, dia order by id_sensor, dia;"))
		presenca = []
		for registro in registros:
			presenca.append({
				"id": registro.id,
				"delta": registro.delta,
				"bateria": registro.bateria,
				"ocupado": registro.ocupado,
			})
		return presenca

# Sensor Passagem    
def inserirPassagem(registros):
	with Session(engine) as sessao, sessao.begin():
		for registro in registros:
			sessao.execute(text("INSERT INTO passagem (id, data, id_sensor, delta, bateria, entrada, saida) VALUES (:id, :data, :id_sensor, :delta, :bateria, :entrada, :saida)"), registro)

def listarPassagem(data_inicial, data_final):
	with Session(engine) as sessao:
		parametros = {
			'data_inicial': data_inicial + ' 00:00:00',
			'data_final': data_final + ' 23:59:59'
		}

		registros = sessao.execute(text("""
select date_format(date(data), '%d/%m') dia, extract(hour from data) hora, cast(sum(entrada) as signed) entrada, cast(sum(saida) as signed) saida
from passagem
where id_sensor = 2 and data between :data_inicial and :data_final
group by dia, hora
		"""), parametros)
		passagem = []
		for registro in registros:
			passagem.append({
				"dia": registro.dia,
				"hora": registro.hora,
				"entrada": registro.entrada,
				"saida": registro.saida,
			})
		return passagem

# Sensor Odor    
def inserirOdor(registros):
	with Session(engine) as sessao, sessao.begin():
		for registro in registros:
			sessao.execute(text("INSERT INTO odor (id, data, id_sensor, delta, bateria, h2s, umidade, nh3, temperatura) VALUES (:id, :data, :id_sensor, :delta, :bateria, :h2s, :umidade, :nh3, :temperatura)"), registro)

def listarOdor():
	with Session(engine) as sessao:
		registros = sessao.execute(text("select date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, avg(bateria) bateria, avg(h2s) h2s, avg(umidade) umidade, avg(nh3) nh3, avg(temperatura) temperatura from odor where id_sensor = 1 and data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59' group by dia, hora order by dia, hora;"))
		odor = []
		for registro in registros:
			odor.append({
				"id": registro.id,
				"delta": registro.delta,
				"bateria": registro.bateria,
				"h2s": registro.h2s,
				"umidade": registro.umidade,
				"nh3": registro.nh3,
				"temperatura": registro.temperatura,
    			})
		return odor

# Sensor PCA    
def inserirPCA(registros):
	with Session(engine) as sessao, sessao.begin():
		for registro in registros:
			sessao.execute(text("INSERT INTO pca (id, data, id_sensor, delta, pessoas, luminosidade, umidade, temperatura) VALUES (:id, :data, :id_sensor, :delta, :pessoas, :luminosidade, :umidade, :temperatura)"), registro)

def listarPCATempoReal():
	with Session(engine) as sessao:
		registros = sessao.execute(text("""
(select id_sensor, pessoas from pca where id_sensor = 1 order by id desc limit 1)
union all
(select id_sensor, pessoas from pca where id_sensor = 2 order by id desc limit 1)
union all
(select id_sensor, pessoas from pca where id_sensor = 3 order by id desc limit 1)
union all
(select id_sensor, pessoas from pca where id_sensor = 4 order by id desc limit 1)
union all
(select id_sensor, pessoas from pca where id_sensor = 5 order by id desc limit 1)
union all
(select id_sensor, pessoas from pca where id_sensor = 6 order by id desc limit 1)
union all
(select id_sensor, pessoas from pca where id_sensor = 7 order by id desc limit 1)
union all
(select id_sensor, pessoas from pca where id_sensor = 8 order by id desc limit 1)
		"""))
		pca = []
		for registro in registros:
			pca.append({
				"id_sensor": registro.id_sensor,
				"pessoas": registro.pessoas,
    			})
		return pca

def listarPCA():
	with Session(engine) as sessao:
		registros = sessao.execute(text("select tmp.id_sensor, tmp.dia, tmp.hora, tmp.pessoas, u.pessoas ultimo_pessoas from (select id_sensor, date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, max(pessoas) pessoas, max(id) id_ultimo from pca where data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59' group by id_sensor, dia, hora order by id_sensor, dia, hora) tmp inner join pca u on u.id = tmp.id_ultimo;"))
		pca = []
		for registro in registros:
			pca.append({
				"id": registro.id,
				"delta": registro.delta,
				"pessoas": registro.pessoas,
				"luminosidade": registro.luminosidade,
				"umidade": registro.umidade,
				"temperatura": registro.temperatura,
    			})
		return pca

# Sensor Creative    
def inserirCreative(registros):
	with Session(engine) as sessao, sessao.begin():
		for registro in registros:
			sessao.execute(text("INSERT INTO creative (id, data, id_sensor, delta, luminosidade, umidade, voc, co2, pressao_ar, ruido, aerosol_parado, aerosol_risco, ponto_orvalho, temperatura) VALUES (:id, :data, :id_sensor, :delta, :luminosidade, :umidade, :voc, :co2, :pressao_ar, :ruido, :aerosol_parado, :aerosol_risco, :ponto_orvalho, :temperatura)"), registro)

def listarCreative(data_inicial, data_final):
	with Session(engine) as sessao:
		parametros = {
			'data_inicial': data_inicial + ' 00:00:00',
			'data_final': data_final + ' 23:59:59'
		}

		registros = sessao.execute(text("""
select date_format(date(data), '%d/%m') dia, extract(hour from data) hora, cast(avg(luminosidade) as float) luminosidade, cast(avg(umidade) as float) umidade, cast(avg(ruido) as float) ruido
from creative
where data between :data_inicial and :data_final
group by dia, hora
order by dia, hora
		"""), parametros)
		creative = []
		for registro in registros:
			creative.append({
				"dia": registro.dia,
				"hora": registro.hora,
				"luminosidade": registro.luminosidade,
				"umidade": registro.umidade,
				"ruido": registro.ruido,
    			})
		return creative

# Sensor Solo    
def inserirSolo(registros):
	with Session(engine) as sessao, sessao.begin():
		for registro in registros:
			sessao.execute(text("INSERT INTO solo (id, data, id_sensor, delta, condutividade, umidade, temperatura) VALUES (:id, :data, :id_sensor, :delta, :condutividade, :umidade, :temperatura"), registro)

def listarSolo():
	with Session(engine) as sessao:
		registros = sessao.execute(text("select date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, avg(condutividade) condutividade, avg(umidade) umidade, avg(temperatura) temperatura from solo where data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59' group by dia, hora order by dia, hora;"))
		solo = []
		for registro in registros:
			solo.append({
				"id": registro.id,
				"delta": registro.delta,
				"condutividade": registro.condutividade,
				"umidade": registro.umidade,
				"temperatura": registro.temperatura,
    			})
		return solo