import pytest

'''2. function that takes two numbers as inputs and returns their sum'''

def calculate_sum(num1, num2):
    return num1 + num2

def test_simple_calculate_sum():
    expected_result = 8
    result = calculate_sum(-13,5)
    assert result == expected_result

def test_float_calculate_sum():
    expected_result = 4.5
    result = calculate_sum(4.5, 0)
    assert result == expected_result

def test_zero_calculate_sum():
    with pytest.raises(TypeError):
        calculate_sum("t", 3)
