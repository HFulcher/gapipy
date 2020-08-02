.PHONY: test clean package docs

test:
	python3 setup.py test

clean:
	rm -rf gapipy.egg-info
	rm -rf build
	rm -rf docs/_build
	rm -rf dist
	rm -rf coverage.xml
	rm -rf .coverage

package:
	python3 setup.py sdist upload

docs:
	sphinx-apidoc -o docs/ gapipy
	make -C docs html
