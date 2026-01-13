VENV = .venv


venv:
	python3 -m venv $(VENV)


install: venv
	$(VENV)/bin/pip install -r requirements.txt


run:
	$(VENV)/bin/fastapi dev src/main.py


clean:
	rm -rf $(VENV)


# Docker / DB


db-up:
	docker compose up -d


db-down:
	docker compose down


db-logs:
	docker compose logs -f db


db-shell:
	docker exec -it db_mysql mariadb -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME)