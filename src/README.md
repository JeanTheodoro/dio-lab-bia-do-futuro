# 🚀 Visão Geral Do Projeto

Este projeto implementa uma assistente financeira inteligente (Aurora) utilizando modelos de linguagem (LLM) executados localmente com Ollama, backend em FastAPI e interface construída com Streamlit.

A aplicação permite que usuários consultem informações financeiras por meio de linguagem natural, com base em dados estruturados armazenados no banco de dados.

## Arquitetura do projeto

![estrutura do projto](../assets/estrutura_do_projeto.png)
A arquitetura é baseada em containers orquestrados com Docker Compose e é composta pelos seguintes serviços:

### 🔹 Componentes principais

* **Streamlit (Frontend)**

  * Interface do usuário
  * Responsável pela interação com o usuário (chat)

* **FastAPI (Backend)**

  * Gerencia as requisições
  * Contém as regras de negócio
  * Integra com banco de dados e LLM

* **Ollama (LLM)**

  * Executa o modelo de linguagem (ex: Gemma)
  * Responsável pela geração das respostas

* **PostgreSQL**

  * Armazena os dados financeiros do usuário
  * Fonte de dados da aplicação

* **Volumes Docker**

  * `postgres_data`: persistência do banco
  * `ollama_data`: persistência dos modelos
---

## 🚀 Como Executar o Projeto

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
