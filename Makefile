install:
	pip install --upgrade pip && pip install -r requirements.txt
install-spacy-lang:
	python3 -m spacy download en_core_web_lg
format:
	black src/*.py src/lib/spacelab.py
lint:
	pylint --disable=R,C src/*.py src/lib/spacelab.py
	flake8 --max-line-length 120 --per-file-ignores=src/json-http-injector.py:F401 --per-file-ignores=src/lib/spacelab.py:F401 src/*.py src/lib/spacelab.py
	#pylint --overgeneral-exceptions '' --disable=R,C src/*.py src/spacelab/spacelab.py
	#flake8 --max-line-length 90 app/*.py app/lib/*.py
apitest:
	docker-compose up --abort-on-container-exit --exit-code-from api-test
test:
	coverage run --source=src -m pytest test_spacelab.py
coverage:
	coverage html
profile:
	python -m scalene --html --- -m pytest test_spacelab.py > test_spacelab_profile.html
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
	cd src;./json-http-injector.py
freeze:
	pip freeze > requirements.txt
