FROM python:3.10.11-slim-bullseye


WORKDIR /code

COPY api/req.txt .
COPY api/initial_migration.sh .
COPY api/migrate.sh .


RUN pip install --upgrade pip
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r /code/req.txt

COPY api/src ./src
COPY api/data ./data
COPY env/backend.env .

RUN alembic init alembic
RUN rm -rf ./alembic/versions/*
COPY api/alembic/env.py ./alembic/
COPY api/alembic.ini .

ENV UVICORN_PORT 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]

EXPOSE $UVICORN_PORT