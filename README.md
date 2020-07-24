# Google Analytics for Python and the command-line (soon)

`gapipy` provides a clean and simple wrapper around the Google Analytics Reporting API to allow for custom queries and report generation.

* **Authentication.** Authenticating service accounts or installed applications is now even easier only requiring one function call.
* **Querying.** *Coming soon*
* **Reporting.** *Coming soon*
* **Exports.** *Coming soon*

This package is built on top of [Google's own API client for Python][apiclient].

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
