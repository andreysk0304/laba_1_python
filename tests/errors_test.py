from pytest import raises as raise_test

from src.main import calculate_now
from src.utils.exceptions import IncorrectPlacementOfBrackets, IncorrectOperationsCount


def test_errors():
    with raise_test(IncorrectOperationsCount):
        calculate_now('2 +')

    with raise_test(ZeroDivisionError):
        calculate_now('2 0 /')

    with raise_test(TypeError):
        calculate_now('10 2.0 //')

    with raise_test(TypeError):
        calculate_now('20 2.2 %')

    with raise_test(IncorrectPlacementOfBrackets):
        calculate_now('( 1 2 + ) ( 1 2 +')

    with raise_test(IncorrectOperationsCount):
        calculate_now('( 1 ( 1 2 ) + ) ( 23 12 )')

    with raise_test(IncorrectPlacementOfBrackets):
        calculate_now('1 2 ) +')