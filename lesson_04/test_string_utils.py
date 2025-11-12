import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# 1. capitalize
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("text", "Text"),
        ("word and sentence", "Word and sentence"),
        ("second is 2", "Second is 2")

    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# 2. trim
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   text", "text"),
        ("   word and sentence", "word and sentence"),
        (" second is 2", "second is 2")

    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", ""),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# 3. contains
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("text", "x", True),
        ("   word and sentence", "a", True),
        (" second is 2", "2", True)

    ],
)
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", "", True),
        ("   ", ".", False),
        ("3", "4", False)
    ],
)
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# 4. delete symbol
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("text", "x", "tet"),
        ("   word and sentence", "a", "   word nd sentence"),
        ("second is 2", "2", "second is ")

    ],
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", "", ""),
        ("   ", " ", ""),
        ("3", "4", "3")
    ],
)
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
