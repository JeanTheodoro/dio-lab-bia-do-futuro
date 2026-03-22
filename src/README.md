# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
## 📁 Estrutura do Projeto

```bash
.
├── README.md
├── docker-compose.yml
│
├── api → (Backend (FastAPI + IA + regras de negócio))
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── poetry.lock
│   ├── main.py
│   │
│   ├── core
│   │   ├── database.py
│   │   └── shared
│   │       ├── config_logging.py
│   │       ├── dependencies.py
│   │       └── settings.py
│   │
│   ├── llm → (Integração com modelos de linguagem)
│   │   ├── factory
│   │   │   └── factory_llm.py
│   │   │
│   │   ├── prompt
│   │   │   ├── bank_human.py
│   │   │   └── bank_system.py
│   │   │
│   │   ├── provider
│   │   │   ├── base_proviser.py
│   │   │   ├── grok_provider.py
│   │   │   └── ollma_provider.py
│   │   │
│   │   ├── serializer
│   │   │   └── serialization.py
│   │   │
│   │   └── services
│   │       ├── bank_assistente.py
│   │       ├── context_builder.py
│   │       └── intent_classifier.py
│   │
│   ├── models
│   │   └── bank
│   │       └── models_bank.py
│   │
│   ├── repository → acesso a dados
│   │   ├── bank_profile
│   │   │   └── cliente.py
│   │   │
│   │   ├── bank_transection
│   │   │   └── conta.py
│   │   │
│   │   └── ia
│   │       └── asssitante.py
│   │
│   ├── router → (endpoints da API)
│   │   ├── bank_profile
│   │   │   └── cliente.py
│   │   │
│   │   ├── bank_transection
│   │   │   └── conta.py
│   │   │
│   │   └── ia
│   │       └── assistant.py
│   │
│   ├── schemas → (validação (Pydantic))
│   │   ├── ai
│   │   │   └── assistant.py
│   │   │
│   │   └── bank
│   │       ├── cliente.py
│   │       ├── conta.py
│   │       ├── historico.py
│   │       ├── metas.py
│   │       └── transacao.py
│   │
│   └── service
│       ├── bank_profile
│       │   └── cliente.py
│       │
│       ├── bank_transection
│       │   └── conta.py
│       │
│       └── ia
│           └── assistant.py
│
├── db → (scripts SQL)
│   ├── init.sql
│   └── init_create_table.sql
│
├── ollama → (container do modelo LLM)
│   └── Dockerfile
│
└── streamlit → (UI(interface do usuário))
    ├── Dockerfile
    ├── pyproject.toml
    ├── poetry.lock
    ├── main.py
    └── service.py
```

## Exemplo da biblioteca ultlizdas src/api/poetry.lock
```
asyncpg              0.31.0    An asyncio PostgreSQL driver
fastapi              0.133.1   FastAPI framework, high performance, easy to learn, fast to code, ready for production
langchain-ollama     1.0.1     An integration package connecting Ollama and LangChain
langchain-openai     1.1.10    An integration package connecting OpenAI and LangChain
pydantic             2.12.5    Data validation using Python type hints
pydantic-settings    2.13.1    Settings management using Pydantic
python-dotenv        1.2.2     Read key-value pairs from a .env file and set them as environment variables
requests             2.32.5    Python HTTP for Humans.
sqlalchemy           2.0.48    Database Abstraction Library
```

## Exemplo da biblioteca ultlizdas src/streamlit/poetry.lock
```
python-dotenv             1.2.2        Read key-value pairs from a .env file and set them as environment variables
requests                  2.32.5       Python HTTP for Humans.
streamlit                 1.55.0       A faster way to build and share data apps
```

## 🚀 Como Rodar o Projeto

### 1️⃣ Acessar o diretório do projeto

```bash
cd src
```

---

### 2️⃣ Criar o arquivo de variáveis de ambiente

Na raiz da pasta `src`, crie um arquivo `.env`.

Você pode utilizar o arquivo `env.example` como referência, pois ele contém todas as **variáveis de ambiente necessárias para executar a aplicação**.

Exemplo:

```bash
cp env.example .env
```

Depois disso, revise o arquivo `.env` e ajuste os valores conforme necessário para o seu ambiente.

---

### 3️⃣ Build e inicialização dos containers

Execute o comando abaixo para construir e subir todos os serviços com **Docker Compose**:

```bash
docker compose up --build
```

---

### 4️⃣ Inicializar o modelo no Ollama

Após os containers estarem em execução, execute o comando abaixo para rodar o modelo **Gemma** dentro do container do Ollama:

```bash
docker exec -ti dio_ollama ollama run gemma3
```

---

### 5️⃣ Inserir os dados da base de conhecimento

Para que a assistente Aurora possa responder às perguntas, é necessário inserir os dados que serão utilizados como **base de conhecimento**.

O script SQL está disponível em:

```
data/sql/inserir_dados.sql
```

Siga os passos abaixo:

1. Acesse o banco de dados **PostgreSQL** utilizando um cliente de banco de dados, como:

   * **pgAdmin**
   * **DBeaver**
   * ou qualquer outro cliente PostgreSQL.

2. Utilize as informações definidas no arquivo `.env` para realizar a conexão com o banco.

3. Após conectar na base de dados:

   * Abra o **editor SQL**
   * Copie o conteúdo do arquivo [`data/sql/inserir_dados.sql`](../data/sql/inserir_dados.sql)
   * Cole no editor
   * Execute o script

Isso irá inserir os dados necessários para que a aplicação funcione corretamente.

---

## 🌐 Acessar a Aplicação

Após subir os containers e inserir os dados, você poderá acessar:

### Interface da Assistente Aurora

```
http://localhost:8501
```

### Documentação da API (Swagger)

```
http://127.0.0.1:8000/docs
```
