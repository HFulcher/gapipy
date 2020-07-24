.ONESHELL:

.PHONY: test clean package docs

test:
	python3 setup.py test

clean:
	rm -rf gapipy.egg-info
	rm -rf build
	rm -rf dist

package: readme
	python3 setup.py sdist upload

docs:
	cd docs && make html
