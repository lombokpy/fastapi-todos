run-server:
	PYTHONPATH=src/fastapi_todos uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8001

db-init:
	PYTHONPATH=src/fastapi_todos alembic init migrations

db-migrate:
	PYTHONPATH=src/fastapi_todos alembic revision --autogenerate
	PYTHONPATH=src/fastapi_todos alembic upgrade head

db-upgrade:
	PYTHONPATH=src/fastapi_todos alembic upgrade head

db-prestart:
	PYTHONPATH=src/fastapi_todos python ./src/fastapi_todos/initial_data.py

run-test:
ifdef dst
	PYTHONPATH=src/fastapi_todos python -m pytest $(dst) -v
else
	PYTHONPATH=src/fastapi_todos python -m pytest -v
endif