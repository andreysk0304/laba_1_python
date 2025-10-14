from src.utils.calculator import Calculator
from src.utils.exceptions import IncorrectPlacementOfBrackets, IncorrectOperationsCount


def check_bracket(tokens: list, index: int) -> (bool, list):
    '''
    Проверяем можно ли посчитать эту скобочку, если да, то возвращаем True и удаляем скобочки

    :param tokens: Токены примера
    :param index: Индекс на котором находится откртие проверяемой скобки
    :return: возможно ли посчитать содержимое кнопки и новый список токенов без скобочек
    '''

    while ('OPEN_BRACKET', '(') in tokens:
        check_calculator = Calculator()

        for index_now in range(index+1, len(tokens)):

            token_type, element = tokens[index_now]

            if token_type == 'NUMBER' or token_type == 'FLOAT':
                check_calculator.add(element=element)

            elif token_type == 'OPERATION':
                check_calculator.use_operation(operation=element)

            elif token_type == 'OPEN_BRACKET':

                status, tokens = check_bracket(tokens=tokens, index=index_now)

                if not status:
                    raise IncorrectOperationsCount

                else:
                    break

            elif token_type == 'CLOSE_BRACKET':

                if len(check_calculator.get()) == 1:

                    del tokens[index_now]
                    del tokens[index]

                    return True, tokens

                else:
                    return False, tokens