

build:
	rm -fr dist/*
	python3 setup.py sdist

publish:
	twine upload dist/*
