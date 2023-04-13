FROM python:3.10

WORKDIR /code

COPY api/req.txt .
COPY api/initial_migration.sh .
COPY api/migrate.sh .


RUN pip install --upgrade pip
RUN pip install -r /code/req.txt

COPY api/src ./src
COPY api/data ./data

RUN alembic init alembic
COPY api/alembic/env.py ./alembic/

ENV UVICORN_PORT 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]

EXPOSE $UVICORN_PORT