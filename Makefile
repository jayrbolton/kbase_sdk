
.PHONY: test publish

test:
	flake8 kbase_sdk
	flake8 test
	mypy --ignore-missing-imports kbase_sdk
	mypy --ignore-missing-imports test
	python -m unittest discover test/

publish:
	rm -rf dist/*
	python setup.py bdist_wheel 
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
