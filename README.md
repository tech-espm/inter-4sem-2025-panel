# Projeto Interdisciplinar IV - Sistemas de Informação ESPM

<p align="center">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>

# Painel de Monitoramento de Sensores em Tempo Real

### 2025-01

## Visão Geral

O projeto de painel de monitoramento de sensores em tempo real consiste em uma dashboard completa para monitorar, em tempo real, dados recebidos de sensores IoT com o intuito de melhorar a gestão do ambiente, reduzindo problemas de má administração que geram desperdício de recursos.

## Participantes

- [Nome](https://github.com/Marcio-Alexandroni)
- [Nome](https://github.com/impauloc)
- [Nome](https://github.com/xxx)
- [Nome](https://github.com/xxx)

## Objetivos do Projeto

A solução se baseia em três principais pilares:

- SaaS para monitorar e controlar ambientes
- Coleta de dados em tempo real
- Interface intuitiva

## Configuração do Projeto

Para executar, deve criar o arquivo `config.py` da seguinte forma:

```python
host = '0.0.0.0'
port = 3000
conexao_banco = 'mysql+mysqlconnector://usuario:senha@host/banco'
url_api = 'https://site.com'
```

Todos os comandos abaixo assumem que o terminal esteja com o diretório atual na raiz do projeto.

## Criação e Ativação do venv

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Execução

```
.venv\Scripts\activate
python app.py
```

## Mais Informações

https://flask.palletsprojects.com/en/3.0.x/quickstart/
https://flask.palletsprojects.com/en/3.0.x/tutorial/templates/

# Licença

Este projeto é licenciado sob a [MIT License](https://github.com/tech-espm/inter-4sem-2025-panel/blob/main/LICENSE).

<p align="right">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo-si-512.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>
