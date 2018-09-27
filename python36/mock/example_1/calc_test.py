def mock_sum_op(a, b):
    return 10


class SubCalculator:
    @staticmethod
    def sum(a, b):
        return a + b


class Calculator:
    sub_calc = SubCalculator()

    @staticmethod
    def sum(a, b):
        return Calculator.sub_calc.sum(a, b)


class TestCalculator:
    @staticmethod
    def test_sum():
        calculator = Calculator
        a, b = 2, 3

        assert a + b == calculator.sum(a, b)

    @staticmethod
    def test_monkey_sum():
        calculator = Calculator
        a, b = 2, 3

        calculator.sub_calc.sum = mock_sum_op

        assert 10 == calculator.sum(a, b)

    @staticmethod
    def test_mocked_sum(mocker):
        calculator = Calculator
        a, b = 2, 3

        mocker.patch.object(calculator, 'sub_calc')
        calculator.sum = mock_sum_op

        assert 10 == calculator.sum(a, b)
