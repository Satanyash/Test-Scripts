import pytest
from string_utils import StringUtils

@pytest.main.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("text", "Text"),
        ("word and sentence", "Word and sentence"),
        ("second is 2", "Second is 2")

    ],
)
def test_capitalize_positive(input_str, expected):
    string = StringUtils()
    assert string.capitalize(input_str) == expected

@pytest.main.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(input_str, expected):
    string = StringUtils()
    assert string.capitalize(input_str) == expected
