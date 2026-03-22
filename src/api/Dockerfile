FROM python:3.12

WORKDIR /api

RUN pip install poetry

COPY pyproject.toml poetry.lock* /api/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

COPY . /api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
