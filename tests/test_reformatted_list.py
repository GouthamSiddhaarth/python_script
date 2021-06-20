import pytest

from scripts.reformat_list import reformat_list


@pytest.mark.parametrize('input, expected_value', [
    (
        {"start_num": 95},
        ['Five', 'Three', '97', '98', 'Three', 'Five']
    ),
    (
        {"end_num":  10},
        ['1', '2', 'Three', '4', 'Five', 'Three', '7', '8', 'Three', 'Five']
    ),
    (
        {"start_num": 7, "end_num":  15},
        ['7', '8', 'Three', 'Five', '11', 'Three', '13', '14', 'ThreeFive']
    ),
    (
        {"start_num": 7, "end_num":  15, "config_list": [(5, 'Five'), (3, 'Three')]},
        ['7', '8', 'Three', 'Five', '11', 'Three', '13', '14', 'FiveThree']
    ),
    (
        {"start_num": 25, "end_num":  45, "config_list": [(2, 'Two'), (3, 'Three'), (5, 'Five')]},
        ['Five', 'Two', 'Three', 'Two', '29', 'TwoThreeFive', '31', 'Two', 'Three', 'Two', 'Five',
         'TwoThree', '37', 'Two', 'Three', 'TwoFive', '41', 'TwoThree', '43', 'Two', 'ThreeFive']
    ),
])
def test_reformat_list(input, expected_value):
    assert reformat_list(**input) == expected_value


@pytest.mark.parametrize('input, expected_value', [
    (
        {"start_num": 7, "end_num":  15},
        "INFO"
    ),
    (
        {"start_num": 7, "end_num":  15, "config_list": [(5, 'Five'), (3, 'Three')]},
        "INFO"
    ),
    (
        {"start_num": 7, "end_num":  15, "config_list":  []},
        "WARNING"
    )
])
def test_loglevel(caplog, input, expected_value):
    reformat_list(**input)
    for record in caplog.records:
        assert record.levelname == expected_value
