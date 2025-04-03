build:
	python3 -m build

test-upload:
	python3 -m twine upload --repository testpypi dist/*

upload:
	python3 -m twine upload dist/*

clean:
	rm -rf dist build
