# Cashback App

Frontend estático + backend em Flask para cálculo de cashback.

## Tecnologias usadas

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite (banco local, arquivo-based)
- HTML, CSS e JavaScript puro

## Estrutura do projeto

- `app.py` - API Flask e roteamento do frontend
- `cashback.py` - lógica de cálculo do cashback
- `database.py` - configuração do SQLAlchemy e modelo `Consulta`
- `requirements.txt` - dependências Python
- `static/index.html` - frontend estático
- `instance/cashback.db` - banco SQLite (criado automaticamente)

## Como rodar localmente

1. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor Flask:
   ```bash
   python3 app.py
   ```
   - O banco SQLite será criado automaticamente em `instance/cashback.db`.

4. Acesse no navegador:
   ```
   http://127.0.0.1:5000
   ```

## Uso

- Insira o valor da compra.
- Insira o desconto em porcentagem.
- Marque se o cliente for VIP.
- Clique em "Calcular Cashback".
- O histórico exibirá apenas as consultas feitas pelo mesmo IP.

## Deploy gratuito recomendado

### Render

1. Crie um repositório no GitHub e faça push do projeto.
2. Acesse https://render.com e crie uma conta.
3. Crie um novo "Web Service" e conecte o repositório GitHub.
4. Configure:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python3 app.py`
5. Render criará uma URL pública (ex: `https://cashback-app.onrender.com`).
6. O banco SQLite será criado no container, mas note que em Render, dados podem ser perdidos em restarts (use Postgres para persistência total).

### Railway (alternativa)

1. Similar ao Render, conecte o GitHub.
2. Railway suporta SQLite, mas para persistência, considere Postgres.


## Observações

- O frontend é totalmente estático e consome a API Flask via `fetch`.
- O histórico é filtrado por IP para exibir apenas as consultas do mesmo usuário.
- SQLite é ideal para desenvolvimento e deploys simples, mas para produção com muitos usuários, considere PostgreSQL.
- Para produção, use um servidor WSGI adequado em vez do servidor de desenvolvimento Flask.
