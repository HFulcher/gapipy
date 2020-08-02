import pytest
from gapipy.query import (_prefix_ga, _to_list, _unpack_metrics, 
                          _unpack_dimensions, build_query)


def test_prefix_ga_no_exist():
    test_string = "string"
    expected_result = "ga:string"

    assert expected_result == _prefix_ga(test_string)

def test_prefix_ga_exists():
    test_string = "ga:string"
    expected_result = "ga:string"

    assert expected_result == _prefix_ga(test_string)


def test_to_list_string():
    test_string = "string"
    expected_result = ["string"]

    assert expected_result == _to_list(test_string)

def test_to_list_list():
    test_list = ["string", "string1", "string2"]
    expected_result = ["string", "string1", "string2"]

    assert expected_result == _to_list(test_list)


def test_unpack_metrics_singular():
    test_string = "metric"
    expected_result = [{
            "expression": "ga:metric"
        }]

    assert expected_result == _unpack_metrics(test_string)

def test_unpack_metrics_multiple():
    test_list = ["metric", "metric1", "metric2"]
    expected_result = [{
            "expression": "ga:metric"
        },
        {
            "expression": "ga:metric1"
        },
        {
            "expression": "ga:metric2"
        }]

    assert expected_result == _unpack_metrics(test_list)


def test_build_query_singular_nodim():
    test_view_id = "11111111"
    test_startDate = "2020-01-01"
    test_endDate = "2020-01-02"
    test_metric = "metric"

    expected_result = {
        'reportRequests': [
            {
                'viewId': test_view_id,
                'dateRanges': [{"startDate": test_startDate,
                                "endDate": test_endDate}],
                'metrics': [{"expression": "ga:metric"}],
                'dimensions': []
            }
        ]
    }

    assert expected_result == build_query(test_view_id, test_startDate,
                                          test_endDate, test_metric)

def test_build_query_multiple_nodim():
    test_view_id = "11111111"
    test_startDate = "2020-01-01"
    test_endDate = "2020-01-02"
    test_metrics = ["metric", "metric1", "metric2"]

    expected_result = {
        'reportRequests': [
            {
                'viewId': test_view_id,
                'dateRanges': [{"startDate": test_startDate,
                                "endDate": test_endDate}],
                'metrics': [
                    {"expression": "ga:metric"},
                    {"expression": "ga:metric1"},
                    {"expression": "ga:metric2"}
                ],
                'dimensions': []
            }
        ]
    }

    assert expected_result == build_query(test_view_id, test_startDate,
                                          test_endDate, test_metrics)

def test_build_query_singular_dim():
    test_view_id = "11111111"
    test_startDate = "2020-01-01"
    test_endDate = "2020-01-02"
    test_metric = "metric"
    test_dim = "dimension"

    expected_result = {
        'reportRequests': [
            {
                'viewId': test_view_id,
                'dateRanges': [{"startDate": test_startDate,
                                "endDate": test_endDate}],
                'metrics': [{"expression": "ga:metric"}],
                'dimensions': [{"name": "ga:dimension"}]
            }
        ]
    }

    assert expected_result == build_query(test_view_id, test_startDate,
                                          test_endDate, test_metric, test_dim)

def test_build_query_multiple_dim():
    test_view_id = "11111111"
    test_startDate = "2020-01-01"
    test_endDate = "2020-01-02"
    test_metrics = ["metric", "metric1", "metric2"]
    test_dims = ["dimension", "dimension1", "dimension2"]

    expected_result = {
        'reportRequests': [
            {
                'viewId': test_view_id,
                'dateRanges': [{"startDate": test_startDate,
                                "endDate": test_endDate}],
                'metrics': [
                    {"expression": "ga:metric"},
                    {"expression": "ga:metric1"},
                    {"expression": "ga:metric2"}
                ],
                'dimensions': [
                    {"name": "ga:dimension"},
                    {"name": "ga:dimension1"},
                    {"name": "ga:dimension2"}
                ]
            }
        ]
    }

    assert expected_result == build_query(test_view_id, test_startDate,
                                          test_endDate, test_metrics, test_dims)