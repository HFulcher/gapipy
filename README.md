# Google Analytics for Python

[![Documentation Status](https://readthedocs.org/projects/google-analytics-python/badge/?version=latest)](https://google-analytics-python.readthedocs.io/en/latest/?badge=latest)
![gapipy](https://github.com/HFulcher/gapipy/workflows/gapipy/badge.svg)
[![codecov](https://codecov.io/gh/HFulcher/gapipy/branch/master/graph/badge.svg)](https://codecov.io/gh/HFulcher/gapipy)

**WARNING: This package is not ready for production yet. If you would like to help make that happen quicker please consider [contributing](https://github.com/HFulcher/gapipy/blob/master/CONTRIBUTING.md)**

`gapipy` provides a clean and simple wrapper around the Google Analytics Reporting API (v4) to allow for custom queries and report generation.

* **Authentication.** Authenticating service accounts or installed applications only requires one function call.
* **Querying.** *Coming soon*
* **Exporting Reports.** *Coming soon*
* **Realtime API.** *Coming soon*
* **Command Line execution.** *Coming soon*
* **Account Configuration & Management.** *Coming soon*

This package is built on top of [Google's own API client for Python][apiclient]. This package also stands on the shoulders of previous Google API packages. Notably:

* [debrouwere/google-analytics](https://github.com/debrouwere/google-analytics)
* [alphagov/gapy](https://github.com/alphagov/gapy)


## Quickstart

First, install the package using [pip](https://pip.pypa.io/en/latest/)

`pip3 install gapipy`

Then, create a new project in the [Google Developers Console](https://console.developers.google.com), enable the  Analytics API under "APIs & auth > APIs" and generate credentials for either:

* An installed application under "APIs & auth > Credentials > OAuth client ID"
* Or a service account under "APIs & auth > Credentials > Service account"

After that, authentication for installed applications is as easy as

```python
import gapipy as ga

service = ga.authenticate(from_service=False, fileName="client-secret.json")
```

For service accounts

```python
import gapipy as ga

service = ga.authenticate(from_service=True, fileName="key.json")
```

Or by storing path to `key.json` in an environment variable

```python
import gapipy as ga

service = ga.authenticate(from_service=True)
```


## Contributing
At the moment this project is being developed and maintained by just me but I am looking for more people to help in the effort.
If you would like to help out please take a look at the [contributing document.](https://github.com/HFulcher/gapipy/blob/master/CONTRIBUTING.md)


## Need a hand?
[Get in touch](mailto:fulcherhuw@gmail.com?subject=gapipy) or [raise an issue.](https://github.com/HFulcher/gapipy/issues)
