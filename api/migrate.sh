#!/bin/bash
python data/drop_tables.py
alembic revision --autogenerate -m "New Migration"
alembic upgrade head

python data/fill_db.py
# python data/fill_db_author.py