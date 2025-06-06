# Projeto Interdisciplinar IV - Sistemas de Informação ESPM

<p align="center">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>

# 🌐 Panel – Painel de Monitoramento de Sensores em Tempo Real

### 2025-01

## 🔍 Visão Geral

O **Panel** é uma solução SaaS desenvolvida para monitoramento inteligente de ambientes físicos em tempo real. Através da integração com sensores IoT e dashboards interativos alimentados por inteligência artificial, a plataforma entrega insights relevantes para melhorar a gestão de espaços, otimizando recursos e promovendo decisões mais eficazes.

## 🎯 Objetivos do Projeto

A solução parte de três pilares principais:

- 💻 **SaaS** para monitorar e controlar ambientes remotamente  
- 📡 **Coleta de dados em tempo real** via sensores físicos
- 📊 **Interface intuitiva**, com dashboards interativos e análises gráficas com I.A.

## Participantes

- [Márcio Alexandroni](https://github.com/Marcio-Alexandroni)
- [Paulo César](https://github.com/impauloc)
- [Isabella Soares](https://github.com/IsabellaSMarin)

## 🤝 Parceria Estratégica

Este projeto conta com o apoio da **Absolut Technologies**, que fornece sensores de alta precisão e patrocina a implementação. Essa parceria permite integrar hardware de ponta com software inteligente, elevando a confiabilidade das análises em tempo real.

## 💡 Como o Panel muda sua visualização?

Com o Panel, você não apenas vê dados — você **enxerga oportunidades**.  
Transformamos ambientes em fontes vivas de informação com dashboards interativos, gráficos dinâmicos e previsões inteligentes.  
Visualizar com o Panel é entender, agir e evoluir.

---

## ⚙️ Configuração do Projeto

Para executar, deve criar o arquivo `config.py` da seguinte forma:

```python
host = '0.0.0.0'
port = 3000
conexao_banco = 'mysql+mysqlconnector://usuario:senha@host/banco'
url_api = 'https://localhost:port'
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
