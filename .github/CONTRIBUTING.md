# Contributing to gapipy

## Introduction and thanks

Hi! Thanks for taking a look at your contributing document. I'm assuming that since you're looking at it
you are considering contributing to building gapipy. Your contribution is very welcome and below will explain
what help is needed and how you can provide it. I look forward to hopefully working with you!

## Important Resources

### Docs

Docs are produced using [sphinx](https://www.sphinx-doc.org/en/master/) and are hosted on [readthedocs](https://google-analytics-python.readthedocs.io/en/latest/). You can build documentation on your local machine by using [nox](https://nox.thea.codes/en/stable/) (you'll need to install it using `Pipefile`). To build the docs run `nox --sessions docs` from the command line.

### Bug reporting/tracking

Bug tracking is handled through [Github Issues](https://github.com/HFulcher/gapipy/issues). When creating an issue you can choose an appropriate template that will
help guide you in how to structure the report. This is useful for us to be able to diagnose and solve bugs quicker.

### Communication

At the moment the only way we have to communicate with other contributers is through email and Github. If the amount of
contributors grows we will look into setting up a more robust form of communication.

## Ways to contribute

Contributing to open source projects isn't just about writing code. Whether it's helping answer queries in issues, writing documentation,
spreading the word or being a supporter, the more the merrier! Take a look at open issues and see how you can get stuck in. If you're new to
open source look for issues tagged "good first issue", these will get your feet wet.

### Contrbuting to code

If you find an issue that you want to work on, first of all, thanks! To get started:

1. Assign yourself to the open issue.
2. Fork and clone the repo to your machine.
3. Get set up by [creating a virtual environment](#setting-up-the-environment) and making sure everything runs using `nox` on the command line.
4. Create a branch to work on.
5. Implement your changes.
6. Use `nox` to ensure that [tests](#testing-the-package), [linting](#style-guide) and [docs](#docs) all run.
7. Push changes to your forked repository.
8. Create a Pull Request.
9. If Github Actions builds successfully and the implementation is correct, the request will be approved and merge.
10. Celebrate!

### Setting up the environment

It is strongly recommended that you have a dedicated virtual environment for working on gapipy. A strict method of creating
and maintaining virtual environments is not enforced for this project but the requirement of having a environment manager that can
produce and read `requirements.txt` files is required. A good option is to use [pip](https://pip.pypa.io/en/stable/) and [pipenv](https://pypi.org/project/pipenv/).

### Testing the package

Tests are written using [pytest](https://docs.pytest.org/en/latest/) and are located in the `tests` folder. To run the tests you will need to install
pytest and/or nox. To run the tests either use `pytest` in the root of the project or run `nox --sessions tests`.

### Style guide

[flake8](https://flake8.pycqa.org/en/latest/) is used to lint the project with some custom parameters found in `tox.ini`. To use the linter on the project install nox and
run `nox --sessions lint`.
