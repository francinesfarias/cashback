Frontend estático + backend em Flask para cálculo de cashback.

## Tecnologias usadas

- Python 3
- Flask
- Flask-SQLAlchemy
- MySQL ou PostgreSQL
- HTML, CSS e JavaScript puro

## Estrutura do projeto

- `app.py` - API Flask e roteamento do frontend
- `cashback.py` - lógica de cálculo do cashback
- `database.py` - configuração do SQLAlchemy e modelo `Consulta`
- `requirements.txt` - dependências Python
- `static/index.html` - frontend estático

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

3. Configure o banco de dados local:
   - Para MySQL, atualize `app.py` se necessário.
   - Para PostgreSQL, defina a variável de ambiente `DATABASE_URL`.

4. Execute o servidor Flask:
   ```bash
   python3 app.py
   ```

5. Acesse no navegador:
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

### Railway

1. Crie um repositório no GitHub e faça push do projeto.
2. Acesse https://railway.app e conecte sua conta GitHub.
3. Crie um novo projeto a partir do repositório.
4. Railway instalará dependências a partir de `requirements.txt`.
5. Defina `DATABASE_URL` automaticamente ou manualmente.
6. Rode o deploy e use a URL pública fornecida.


## Observações

- O frontend é totalmente estático e consome a API Flask via `fetch`.
- O histórico é filtrado por IP para exibir apenas as consultas do mesmo usuário.
- Para produção, use um servidor WSGI adequado em vez do servidor de desenvolvimento Flask.
