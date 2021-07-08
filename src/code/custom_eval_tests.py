import pytest

from custom_eval.custom_eval import custom_eval

def test_custom_eval_addition():
    assert custom_eval("1 + 2") == 3

def test_custom_eval_subtraction():
    assert custom_eval("11 - 34") == -23

def test_custom_eval_multiplication():
    assert custom_eval("4 * 7") == 28

def test_custom_eval_division():
    assert custom_eval("45 / 5") == 9


@pytest.mark.parametrize("complex_expression, expected_result", [
    ("30 + 6 - 2 + 8", 42),
    ("55 - 13 + 5 - 12", 35),
    ("12 - 3 * 6", -6),
    ("9 * 2 - 8 / 4 + 5", 21)
])
def test_custom_eval_expression(complex_expression, expected_result):
    assert custom_eval(complex_expression) == expected_result


def test_custom_eval_blank():
    with pytest.raises(RuntimeError, match="Empty or None input not allowed !!"): 
        custom_eval("")

def test_custom_eval_blank():
    with pytest.raises(RuntimeError, match="Empty input not allowed !!"): 
        custom_eval("   ")

def test_custom_eval_null():
    with pytest.raises(RuntimeError, match="Empty or None input not allowed !!"): 
        custom_eval(None)

def test_custom_eval_malformed():
    with pytest.raises(RuntimeError, match="Malformed Input not allowed !!"): 
        custom_eval(" 4 + 7 -")
    