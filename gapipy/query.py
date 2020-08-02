"""
Functionality to query the Google Analytics API.
"""


def _prefix_ga(value):
    """
    Adds "ga:" to the beginning of provided metrics/dimensions if it does not
    already exist.

    Args:
        value (string): The string to add prefix to.

    Returns:
        string: The original string or a new string with the prefix attached.
    """
    if not value.startswith('ga:'):
        value = "ga:" + value

    return value


def _to_list(values):
    """
    Checks for whether the provided metric variable is singular (a string) or
    a list. If singular it is wrapped in a list.

    Args:
        values (string/list): String is singular or list if multiple.

    Returns:
        List: List of values
    """
    if type(values) is list:
        return values
    else:
        return [values]


def _unpack_metrics(metrics):
    """
    Creates a dictionary structure that matches the required shape for a Google
    Analytics API request.

    Args:
        metrics (list): List of metrics to be placed into dictionary.

    Returns:
        dict: Dictionary of metrics.
    """
    metrics = _to_list(metrics)
    new_metrics = []

    for metric in metrics:
        new_metrics.append({
            "expression": _prefix_ga(metric)
        })

    return new_metrics


def _unpack_dimensions(dimensions):
    """
    Creates a dictionary structure that matches the required shape for a Google
    Analytics API request.

    Args:
        metrics (list): List of metrics to be placed into dictionary.

    Returns:
        dict: Dictionary of metrics.
    """

    dimensions = _to_list(dimensions)
    new_dimensions = []

    for dimension in dimensions:
        new_dimensions.append({
            "name": _prefix_ga(dimension)
        })

    return new_dimensions


def build_query(view_id, startDate, endDate, metrics, dimensions=None):
    """
    Function to build query to obtain data from a specific Google Analytics
    view.

    List of metrics and dimensions to use can be found
    [here](https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/)

    Args:
        view_id (string/integer): ID of Google Analytics view
        startDate (string): Start Date in format 'YYYY-MM-DD'
        endDate (string): End Date in format 'YYYY-MM-DD'
        metrics (string/list): Single or multiple metrics
        dimensions (string/list, optional): Single or multiple dimensions.
                                            Defaults to None.

    Returns:
        dict: Returns formed query.
    """
    view_id = str(view_id)

    metrics = _unpack_metrics(metrics)

    if dimensions is None:
        dimensions = []
    else:
        dimensions = _unpack_dimensions(dimensions)

    query = {
        'reportRequests': [
            {
                'viewId': view_id,
                'dateRanges': [{"startDate": startDate, "endDate": endDate}],
                'metrics': metrics,
                'dimensions': dimensions
            }
        ]
    }

    return query
