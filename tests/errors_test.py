from pytest import raises as raise_test

from src.main import calculate_now


def test_errors():
    with raise_test(TypeError):
        calculate_now('2 +')

    with raise_test(ZeroDivisionError):
        calculate_now('2 0 /')

    with raise_test(TypeError):
        calculate_now('10 2.0 //')

    with raise_test(TypeError):
        calculate_now('20 2.2 %')

    with raise_test(SyntaxError):
        calculate_now('( 1 2 + ) ( 1 2 +')

    with raise_test(SyntaxError):
        calculate_now('( 1 ( 1 2 ) + ) ( 23 12 )')