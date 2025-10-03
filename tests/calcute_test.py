from src.main import calculate_now


def test_calculate():
    assert calculate_now('2 2 *') == 4
    assert calculate_now('2 2 2 + *') == 8
    assert calculate_now('9 8 + 9 * 10 +') == 163
    assert calculate_now('1.0 20 *') == 20.0
    assert calculate_now('200 2 **') == 200**2