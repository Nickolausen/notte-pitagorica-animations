reset:
	rm -rf .venv

env:
	python3 -m venv .venv

install:
	pip3 install -r requirements.txt

freeze:
	pip3 freeze > requirements.txt