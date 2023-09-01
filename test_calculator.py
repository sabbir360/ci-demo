"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 10 == calculator.multiply(5, 2)

    def test_division(self):
        assert 2 == calculator.division(4, 2)

    def test_division_with_zero(self):
        return 0 == calculator.division(4, 0)
