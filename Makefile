.PHONY: clean package

clean:
	rm -rf gapipy.egg-info
	rm -rf build
	rm -rf dist
	rm -rf coverage.xml
	rm -rf .coverage

package:
	python3 setup.py sdist upload

requirements:
	pip freeze > requirements.txt