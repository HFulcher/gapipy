def _prefix_ga(value):
    if not value.startswith('ga:'):
        value = "ga:" + value

    return value


def _to_list(values):
    if type(values) is list:
        return values
    else:
        return [values]


def _unpack_metrics(metrics):
    metrics = _to_list(metrics)
    print(metrics)
    new_metrics = []

    for metric in metrics:
        new_metrics.append({
            "expression": _prefix_ga(metric)
        })

    return new_metrics


def _unpack_dimensions(dimensions):
    dimensions = _to_list(dimensions)
    new_dimensions = []

    for dimension in dimensions:
        new_dimensions.append({
            "name": _prefix_ga(dimension)
        })

    return new_dimensions


def build_query(view_id, startDate, endDate, metrics, dimensions=None):
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

    print(query)

    return query
