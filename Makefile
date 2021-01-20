clean:
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	rm -rf dist/

lint:
	flake8 .

.PHONY: mypy
mypy:
	mypy .
