FROM python:3.12

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

COPY . /app

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
