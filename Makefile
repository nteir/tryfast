requirements:
	poetry export -f requirements.txt -o requirements.txt --without-hashes

rebuild:
	docker-compose up -d --build

migrations:
	docker-compose run web alembic revision --autogenerate -m "New migration"

migrate:
	docker-compose run web alembic upgrade head

.PHONY: requirements rebuild migrations migrate