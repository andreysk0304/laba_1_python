from src.main import calculate_now


def test_calculate():

    #Без скобочек
    assert calculate_now('2 2 *') == 4
    assert calculate_now('2 2 2 + *') == 8
    assert calculate_now('9 8 + 9 * 10 +') == 163
    assert calculate_now('1.0 20 *') == 20.0
    assert calculate_now('200 2 **') == 200**2

    #Со скобочками
    assert calculate_now('( ( 52 3 * ) 3 - )    ( 267 5 * ) +') == 1488
    assert calculate_now('( 1 ( 2 3 + ) * ) ( 1 2 + ) +') == 8
    assert calculate_now('( 3 4 + ) ( 5 2 - ) *') == 21 #Пример Самира 1
    assert calculate_now('( 8 ( 3 2 + ) - ) 4 *') == 12 #Пример Самира 2
    assert calculate_now('( 3 ( 4 5 + ) - ) 2 ( 3 4 + ) * *') == -84