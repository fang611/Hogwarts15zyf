from Hogwarts15.calculator import Calculator
import pytest


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [0, 1, 1]],
                             ids=['int_case', 'init_big_case', 'float_case', 'zero_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect
