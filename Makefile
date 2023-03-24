install:
	pip install --upgrade pip && pip install -r requirements.txt
install-spacy-lang:
	python3 -m spacy download en_core_web_lg
format:
	black src/*.py src/spacelab/spacelab.py
lint:
	pylint --disable=R,C src/*.py src/spacelab/spacelab.py
	flake8 --max-line-length 100 --per-file-ignores=src/json-http-injector.py:F401 --per-file-ignores=src/spacelab/spacelab.py:F401 src/*.py src/spacelab/spacelab.py
	#pylint --overgeneral-exceptions '' --disable=R,C src/*.py src/spacelab/spacelab.py
	#flake8 --max-line-length 90 app/*.py app/lib/*.py
test:
	python -m pytest -vv --cov=app/lib test_logic.py
build:
	docker build -t json-http-injector:latest .
deploy:
	docker compose up
all: install format lint test build deploy

buildhelo: 
	#docker build -t helo:latest .
debug:
	#python -m flask --app app.py run
	#gunicorn -w 2 --reload 'app:app'
	cd app;uvicorn json-http-injector:app --reload --host 0.0.0.0
freeze:
	pip freeze > requirements.txt