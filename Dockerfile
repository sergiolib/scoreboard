FROM python:3.11-buster as builder

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=/root/.local/bin/:$PATH \
	POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --only main --no-root

FROM python:3.11-slim-buster as runtime

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY manage.py ./
COPY poto ./poto
COPY win ./win

CMD ["uvicorn", "poto.asgi:application", "--port", "8080", "--host", "0.0.0.0", "--reload"]
