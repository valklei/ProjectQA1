from calculator import Calculator

import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_sum_pos_muns(calculator):
    assert calculator.sum(1, 6) == 7

@pytest.mark.skip(reason='тест отключен')
def test_sum_neg_muns(calculator):
    assert calculator.sum(-1, -2) == -3

def test_div_by_zero(calculator):
    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
        calculator.div(10,0)

def test_mul_pos_muns(calculator):
    assert calculator.mul(2, 2) == 4

Teacher 27 Teacher 27  кому  Все 13:05
from calculator import Calculator

import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_sum_pos_muns(calculator):
    assert calculator.sum(1, 6) == 7

@pytest.mark.skip(reason='тест отключен')
def test_sum_neg_muns(calculator):
    assert calculator.sum(-1, -2) == -3

def test_div_by_zero(calculator):
    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
        calculator.div(10,0)

def test_mul_pos_muns(calculator):
    assert calculator.mul(2, 2) == 4
@pytest.mark.skipif(condition='sys.version_info < (3, 8)', reason="Требуется Python 3.8")

@pytest.mark.parametrize("arg1, arg2, res", [
    (4, 5, 9),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 3.5, 6.0),
])
def test_sum_pos_muns(arg1, arg2, res, calculator):
    assert calculator.sum(arg1, arg2)  == res

============================================

rom calculator import Calculator

cal = Calculator()

# тестируем метод sum

res = cal.sum(4, 6)
assert res == 10, 'результат не совпал'

res1 = cal.sum(-4, -2)
assert res1 == -6, 'результат не совпал'

res2 = cal.avg([1,2,3])
assert res2 == 2, 'результат не совпал'
class Calculator:

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ArithmeticError("На ноль делить нельзя")
        return a / b

    def pow(self, a, b=2):
        return a ** b

    def avg(self, nums):
        if len(nums) == 0:
            return 0
        s = sum(nums)
        return self.div(s, len(nums))
from calculator import Calculator

import pytest

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize('num1, num2, result', [(4, 5, 9), (2, 8, 10), (11, 0, 11)])
def test_sum_nums(calculator, num1, num2, result):
    res = calculator.sum(num1, num2)
    assert res == result

@pytest.mark.skip(reason='тест отключен')
def test_sum_neg_muns(calculator):
    assert calculator.sum(-1, -2) == -3

@pytest.mark.skipif(condition='sys.version_info < (3, 8)', reason="Требуется Python 3.8")
def test_div_by_zero(calculator):
    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
        calculator.div(10,0)

def test_mul_pos_muns(calculator):
    assert calculator.mul(2, 2) == 4
