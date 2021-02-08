import nox

locations = "gapipy", "noxfile.py", "gapipy/tests", "docs/conf.py"
nox.options.sessions = "lint", "tests"


@nox.session
def tests(session):
    session.install("-r", "requirements.txt")
    session.install(".")
    session.install('pytest')
    session.run('pytest')


@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8', *locations)


@nox.session
def docs(session):
    session.install('sphinx', 'sphinx-autodoc-typehints', 'sphinx-rtd-theme',
                    '-r', 'requirements.txt')
    # session.install('.')
    # session.run('sphinx-apidoc', '-o', 'docs/', 'gapipy')
    # session.run('make', '-C', 'docs', 'html', external=True)
    session.run('sphinx-build', "docs", "docs/build")


@nox.session
def coverage(session):
    session.install("-r", "requirements.txt")
    session.install("coverage[toml]", "codecov", "pytest")
    session.install(".")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)
