"""
Allows users to authenticate a service account or installed application using
either:
    * A .json key file for service accounts (must be in root directory of
      where your script is run)
    * A .env file with a path to the .json key for service accounts
    * If no .env file is provided the environment variables will be checked
      for `GOOGLE_APPLICATION_CREDENTIALS`
    * A .json oauth2 credentials file for installed applications (must be in
      root directory of where your script is run)

Examples:
    To authenticate and retrieve a Google API service with a service account::

        import gapipy as ga

        # For .json files, from_service=True is on by default
        service = ga.authenticate(fileName="example.json")

        # For .env files
        service = ga.authenticate()

    To authenticate and retrieve a Google API service with a installed
    application::

        import gapipy as ga

        # Must always provide from_service=False and a file name
        service = ga.authenticate(fileName="example.json")

Attributes:
    BASEDIR (os.path): Gets the working directory of where the module is
                       imported to. This allows the authentication process
                       to find a specified .json or .env file.

    DEFAULT_SCOPE (list): List of scopes that will define what the
                          authenticated service can access. Access to profile,
                          email and openid is
                          needed with oauth2 verification.

    REQUIRED_ENV_VAR (string): Name of required environment variable for service
                               account authentication from environment. Variable
                               should point to the absolute path of the .json
                               file.

    API_NAME (string): Specifies the [Google Analytics Reporting API]
                       (https://developers.google.com/analytics/devguides/reporting/core/v4/).
                       The Google Analytics API v3 is still available but it is
                       recommended to use the Reporting API to get full access
                       to features.

    API_VERSION (string): Specifies the latest version of the Reporting API.
"""


import os

from google.oauth2 import service_account
from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google import auth
from dotenv import load_dotenv
from .query import build_query

BASEDIR = os.getcwd()
DEFAULT_SCOPE = ['https://www.googleapis.com/auth/analytics.readonly',
                 'https://www.googleapis.com/auth/userinfo.profile',
                 'https://www.googleapis.com/auth/userinfo.email',
                 'openid'
                 ]
REQUIRED_ENV_VAR = "GOOGLE_APPLICATION_CREDENTIALS"
API_NAME = "analyticsreporting"
API_VERSION = "v4"


def authenticate(from_service=True, fileName=None):
    """
    The primary function to authenticate a Google Analytics Reporting API
    service. Provides a way to authenticate service accounts
    (.json/.env/environment variables) and installed applications (.json).

    Args:
        from_service (bool, optional): Flag to specify whether authentication
                                       is from a service account or from an
                                       installed application. Defaults to True.
        fileName (string, optional): Name of the .json file that has either
                                     the service account key or the client
                                     secret for installed applications. Defaults
                                     to None.

    Raises:
        FileNotFoundError: Raised when a user tries to use oauth
        authentication without specifying a client secrets file.

    Returns:
        Resource: Returns a Google API Resource object that allows users to
        query and receive data from the API.
    """

    if not from_service and fileName:
        service = _authenticate_install(fileName)
    elif from_service:
        service = _authenticate_service(fileName)
    elif not from_service and not fileName:
        raise FileNotFoundError(
            "If using oauth you must specify a file name using fileName"
            "parameter.")

    return service


# TODO: Unit tests
def _authenticate_service(fileName=None):
    """
    Function will try to authenticate using either the file name provided or
    by accessing environment variable (GOOGLE_APPLICATION_CREDENTIALS) that
    provides a path to the client key .json file.

    Args:
        fileName (string, optional): File name passed through from
                                     authenticate(). Defaults to None.

    Raises:
        FileNotFoundError: Raised when provided file name cannot be found.
        RuntimeWarning: Warns user that a .env file cannot be found.
        ValueError: Raised when GOOGLE_APPLICATION_CREDENTIALS cannot be found
                    in the environment variables.

    Returns:
        Returns a Google API Resource object that allows users to query and
        receive data from the API.
    """

    if fileName:
        filePath = os.path.join(BASEDIR, fileName)

        if os.path.isfile(filePath):
            credentials = service_account.Credentials.from_service_account_file(
                filename=filePath, scopes=DEFAULT_SCOPE)
        else:
            raise FileNotFoundError("Cannot find your provided file. Please"
                                    "only pass a file name and .json extension."
                                    "File should be located in the same"
                                    "directory as where you are running your"
                                    "script from.")
    else:
        filePath = os.path.join(BASEDIR, ".env")

        if os.path.isfile(filePath):
            load_dotenv(filePath)
        else:
            raise RuntimeWarning("The .env file cannot be found, still"
                                 f"checking environment for {REQUIRED_ENV_VAR}."
                                 "Make sure you are storing the file in the"
                                 "same directory as where you are running your"
                                 "script from.")

        if REQUIRED_ENV_VAR in list(os.environ):
            credentials, _ = auth.default(scopes=DEFAULT_SCOPE)
        else:
            raise ValueError(f"Could not find {REQUIRED_ENV_VAR} in environment"
                             "variables. Make sure it is specified in your .env"
                             "file or in the environment.")

    return Client(_build(credentials))


# TODO: Add option to store and load credentials.
# TODO: Unit tests
def _authenticate_install(fileName):
    """
    Function will try to authenticate using a client secrets .json file provided
    via fileName.

    Args:
        fileName (string): File name passed through from authenticate().

    Raises:
        FileNotFoundError: Raised when provided file name cannot be found.

    Returns:
        Returns a Google API Resource object that allows users to query and
        receive data from the API.
    """

    filePath = os.path.join(BASEDIR, fileName)

    if os.path.isfile(filePath):
        flow = InstalledAppFlow.from_client_secrets_file(
            filePath, scopes=DEFAULT_SCOPE)
        flow.run_local_server()
        credentials = flow.credentials
    else:
        raise FileNotFoundError("Cannot find your provided file. Please only"
                                "pass a file name and .json extension. File"
                                "should be located in the same directory as"
                                "where you are running your script from.")

    return Client(_build(credentials))


def _build(credentials):
    return discovery.build(API_NAME, API_VERSION, credentials=credentials)


class Client(object):
    def __init__(self, service):
        self.service = service

    def get(self, view_id, start_date, end_date, metrics,
            dimensions=None):

        ga_query = build_query(
            view_id=view_id,
            startDate=start_date,
            endDate=end_date,
            metrics=metrics,
            dimensions=dimensions
        )

        return self.service.reports().batchGet(body=ga_query).execute()
