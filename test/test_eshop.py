import pytest
from app.eshop import calculate_discount

class TestEshop():

    #
    # Positive testing
    # 

    @pytest.mark.parametrize('amount, discount', [
        (0.0, 0.0),         # Partition 0-300: lower boundary value
        (0.01, 0.0),
        (150.00, 0.0),
        (299.99, 0.0),
        (300.00, 0.0),      # Partition 0-300: upper boundary value
        (300.01, 0.05),     # Partition 300.01-800: lower boundary value
        (300.02, 0.05),
        (550.00, 0.05),
        (799.99, 0.05),
        (800.00, 0.05),     # Partition 300.01-800: upper boundary value
        (800.01, 0.1),      # Partition 800-MAX DOUBLE: lower boundary value
        (800.02, 0.1),
        (900.00, 0.1),
    ])
    def test_eshop_discount_passes(self, amount, discount):
        assert calculate_discount(amount) == discount

    #
    # Negative testing
    #     

    @pytest.mark.parametrize('amount, discount', [
        ("900", 0.1),       # Edge case: implies string to float conversion
        ("900.01", 0.1)     # Edge case: implies string to float conversion with decimals
    ])
    def test_eshop_discount_passes(self, amount, discount):
        assert calculate_discount(amount) == discount

    def test_eshop_wrong_data_type_fails(self):
        with pytest.raises(ValueError) as error_info:
            calculate_discount('Hello')
        assert str(error_info.value)[0:35] == 'could not convert string to float: '        