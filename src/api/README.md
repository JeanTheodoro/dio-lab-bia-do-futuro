# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de src/api/poetry.lock

```
annotated-doc        0.0.4     Document parameters, class attributes, return types, and variables inline, with Annotated.
annotated-types      0.7.0     Reusable constraint types to use with typing.Annotated
anyio                4.12.1    High-level concurrency and networking framework on top of asyncio or Trio
asyncpg              0.31.0    An asyncio PostgreSQL driver
certifi              2026.2.25 Python package for providing Mozilla's CA Bundle.
charset-normalizer   3.4.5     The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
click                8.3.1     Composable command line interface toolkit
distro               1.9.0     Distro - an OS platform information API
dnspython            2.8.0     DNS toolkit
email-validator      2.3.0     A robust email address syntax and deliverability validation library.
fastapi              0.133.1   FastAPI framework, high performance, easy to learn, fast to code, ready for production
fastapi-cli          0.0.24    Run and manage FastAPI apps from the command line with FastAPI CLI. 🚀
fastapi-cloud-cli    0.14.1    Deploy and manage FastAPI Cloud apps from the command line 🚀
fastar               0.8.0     High-level bindings for the Rust tar crate
greenlet             3.3.2     Lightweight in-process concurrent programming
h11                  0.16.0    A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
httpcore             1.0.9     A minimal low-level HTTP client.
httptools            0.7.1     A collection of framework independent HTTP protocol utils.
httpx                0.28.1    The next generation HTTP client.
idna                 3.11      Internationalized Domain Names in Applications (IDNA)
jinja2               3.1.6     A very fast and expressive template engine.
jiter                0.13.0    Fast iterable JSON parser.
jsonpatch            1.33      Apply JSON-Patches (RFC 6902)
jsonpointer          3.0.0     Identify specific nodes in a JSON document (RFC 6901)
langchain-core       1.2.17    Building applications with LLMs through composability
langchain-ollama     1.0.1     An integration package connecting Ollama and LangChain
langchain-openai     1.1.10    An integration package connecting OpenAI and LangChain
langsmith            0.7.14    Client library to connect to the LangSmith Observability and Evaluation Platform.
markdown-it-py       4.0.0     Python port of markdown-it. Markdown parsing, done right!
markupsafe           3.0.3     Safely add untrusted strings to HTML/XML markup.
mdurl                0.1.2     Markdown URL utilities
ollama               0.6.1     The official Python client for Ollama.
openai               2.26.0    The official Python library for the openai API
orjson               3.11.7    Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
packaging            26.0      Core utilities for Python packages
pydantic             2.12.5    Data validation using Python type hints
pydantic-core        2.41.5    Core functionality for Pydantic validation and serialization
pydantic-extra-types 2.11.0    Extra Pydantic types.
pydantic-settings    2.13.1    Settings management using Pydantic
pygments             2.19.2    Pygments is a syntax highlighting package written in Python.
python-dotenv        1.2.2     Read key-value pairs from a .env file and set them as environment variables
python-multipart     0.0.22    A streaming multipart parser for Python
pyyaml               6.0.3     YAML parser and emitter for Python
regex                2026.2.28 Alternative regular expression module, to replace re.
requests             2.32.5    Python HTTP for Humans.
requests-toolbelt    1.0.0     A utility belt for advanced users of python-requests
rich                 14.3.3    Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
rich-toolkit         0.19.7    Rich toolkit for building command-line applications
rignore              0.7.6     Python Bindings for the ignore crate
sentry-sdk           2.54.0    Python client for Sentry (https://sentry.io)
shellingham          1.5.4     Tool to Detect Surrounding Shell
sniffio              1.3.1     Sniff out which async library your code is running under
sqlalchemy           2.0.48    Database Abstraction Library
starlette            0.52.1    The little ASGI library that shines.
tenacity             9.1.4     Retry code until it succeeds
tiktoken             0.12.0    tiktoken is a fast BPE tokeniser for use with OpenAI's models
tqdm                 4.67.3    Fast, Extensible Progress Meter
typer                0.24.1    Typer, build great CLIs. Easy to code. Based on Python type hints.
typing-extensions    4.15.0    Backported and Experimental Type Hints for Python 3.9+
typing-inspection    0.4.2     Runtime typing introspection tools
urllib3              2.6.3     HTTP library with thread-safe connection pooling, file post, and more.
uuid-utils           0.14.1    Fast, drop-in replacement for Python's uuid module, powered by Rust.
uvicorn              0.41.0    The lightning-fast ASGI server.
uvloop               0.22.1    Fast implementation of asyncio event loop on top of libuv
watchfiles           1.1.1     Simple, modern and high performance file watching and code reload in python.
websockets           16.0      An implementation of the WebSocket Protocol (RFC 6455 & 7692)
xxhash               3.6.0     Python binding for xxHash
zstandard            0.25.0    Zstandard bindings for Python
```

## Exemplo de src/streamlit/poetry.lock 
```
altair                    6.0.0        Vega-Altair: A declarative statistical visualization library for Python.
attrs                     25.4.0       Classes Without Boilerplate
blinker                   1.9.0        Fast, simple object-to-object and broadcast signaling
cachetools                7.0.3        Extensible memoizing collections and decorators
certifi                   2026.2.25    Python package for providing Mozilla's CA Bundle.
charset-normalizer        3.4.5        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
click                     8.3.1        Composable command line interface toolkit
gitdb                     4.0.12       Git Object Database
gitpython                 3.1.46       GitPython is a Python library used to interact with Git repositories
idna                      3.11         Internationalized Domain Names in Applications (IDNA)
jinja2                    3.1.6        A very fast and expressive template engine.
jsonschema                4.26.0       An implementation of JSON Schema validation for Python
jsonschema-specifications 2025.9.1     The JSON Schema meta-schemas and vocabularies, exposed as a Registry
markupsafe                3.0.3        Safely add untrusted strings to HTML/XML markup.
narwhals                  2.17.0       Extremely lightweight compatibility layer between dataframe libraries
numpy                     2.4.2        Fundamental package for array computing in Python
packaging                 26.0         Core utilities for Python packages
pandas                    2.3.3        Powerful data structures for data analysis, time series, and statistics
pillow                    12.1.1       Python Imaging Library (fork)
protobuf                  6.33.5       
pyarrow                   23.0.1       Python library for Apache Arrow
pydeck                    0.9.1        Widget for deck.gl maps
python-dateutil           2.9.0.post0  Extensions to the standard Python datetime module
python-dotenv             1.2.2        Read key-value pairs from a .env file and set them as environment variables
pytz                      2026.1.post1 World timezone definitions, modern and historical
referencing               0.37.0       JSON Referencing + Python
requests                  2.32.5       Python HTTP for Humans.
rpds-py                   0.30.0       Python bindings to Rust's persistent data structures (rpds)
six                       1.17.0       Python 2 and 3 compatibility utilities
smmap                     5.0.2        A pure Python implementation of a sliding window memory map manager
streamlit                 1.55.0       A faster way to build and share data apps
tenacity                  9.1.4        Retry code until it succeeds
toml                      0.10.2       Python Library for Tom's Obvious, Minimal Language
tornado                   6.5.4        Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
typing-extensions         4.15.0       Backported and Experimental Type Hints for Python 3.9+
tzdata                    2025.3       Provider of IANA time zone data
urllib3                   2.6.3        HTTP library with thread-safe connection pooling, file post, and more.
watchdog                  6.0.0        Filesystem events monitoring
```

## Como Rodar

```bash
# Build do projeto
## Aacces o diretóri

$ cd src

### Execute o comando de build do docker
docker compose up --build


# Acessar aplicação a agente Aurora
http://localhost:8501/

#Acessar a api
http://127.0.0.1:8000/docs#/
```
