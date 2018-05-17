
.PHONY: test publish

test:
	python -m unittest discover test/

publish:
	rm -r dist/*
	python setup.py bdist_wheel 
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
