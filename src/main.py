from src.utils.calculator import Calculator
from src.utils.components.check_bracket_component import check_bracket
from src.utils.tokenizer import tokenize_fsm


def calculate(tokens: list) -> float | int:
    '''
    Функция считает пример в обратной польской нотации

    :param tokens: пример в виде токенов
    :return: посчитанный пример в обратной польской нотации
    '''

    calculator = Calculator()

    if tokens.count(('OPEN_BRACKET', '(')) != tokens.count(('CLOSE_BRACKET', ')')):
        raise SyntaxError('Не правильно расставлены скобки в примере.')

    while ('OPEN_BRACKET', '(') in tokens:
        for index, token in enumerate(tokens):

            token_type, element = token

            if token_type == 'OPEN_BRACKET':

                status, tokens = check_bracket(index=index, tokens=tokens)

                if not status:
                    raise SyntaxError(f'Не правильно расставлены скобки в примере.')

                else:
                    break

    for index, token in enumerate(tokens):

        token_type, element = token

        if token_type == 'NUMBER' or token_type == 'FLOAT':
            calculator.add(element)

        elif token_type == 'OPERATION':
            calculator.use_operation(operation=element)

        elif token_type == 'CLOSE_BRACKET':
            raise SyntaxError('Не правильно расставлены скобки в примере.')

        else:
            raise TypeError(f'Не известный тип токена: {token_type}')

    if len(calculator.get()) > 1:
        raise 'Невозможно посчитать введённый пример ( введено не достаточно знаков операций )'

    else:
        return calculator.get()[0]


def calculate_now(input_data: str) -> int | float:
    '''
    :param input_data: Входная строка (пример в обратной польской нотации)
    :return: Значение входной строки
    '''

    tokens = tokenize_fsm(input_data)

    answer = calculate(tokens)

    return answer



def main():
    while True:
        input_data: str = input('Введите пример (команда break остановит программу): ')

        if input_data.lower() == 'break':
            print('Выполнение кода прекращено.')

            break

        print(calculate_now(input_data=input_data))



if __name__ == '__main__':
    main()