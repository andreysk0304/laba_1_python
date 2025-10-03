from src.utils.calculator import Calculator
from src.utils.stack import Stack

def get_format(state: str, current_token: str) -> int | float | str:
    '''
    Функция преобразует токен в типе str в необходимый для счета тип

    :param state: тип токена ( OPERATION | NUMBER | FLOAT )
    :param current_token: токен
    :return: возвращает преобразованный в нужный тип токен
    '''


    if state == 'NUMBER':
        return int(current_token)

    elif state == 'FLOAT':
        return float(current_token)

    else:
        return current_token


def tokenize_fsm(expr: str) -> list:
    '''
    Функция разбивает на токены входную строку

    :param expr: входная строка с польской нотацией
    :return: Список токенов с их типами ("тип", "токен")
    '''

    tokens = []
    state = 'START'
    current_token = ''

    for index, char in enumerate(expr):
        if char == ' ':

            if state != 'START':
                tokens.append((state, get_format(state=state, current_token=current_token)))

            else:
                pass

            state = 'START'
            current_token = ''


        elif state == 'START':
            if char.isdigit() or char == '~':
                state = 'NUMBER'

                if char == '~':
                    current_token = '-'

                else:
                    current_token = char

            elif char in ['+', '-', '*', '/', '%']:
                state = 'OPERATION'
                current_token = char

        elif state == 'NUMBER':
            if char.isdigit():
                current_token += char

            elif char == '.':
                state = 'FLOAT'

                current_token += char


        elif state == 'FLOAT':
            if char.isdigit():
                current_token += char


        elif state == 'OPERATION':
            if char in ['/', '*']:
                current_token += char


    else:
        if state != 'START':
            tokens.append((state, get_format(state=state, current_token=current_token)))

        else:
            pass

    return tokens



def calculate(tokens: list) -> float | int:
    '''
    Функция считает пример в обратной польской нотации

    :param tokens: пример в виде токенов
    :return: посчитанный пример в обратной польской нотации
    '''

    calulator = Calculator()

    for token in tokens:

        state, element = token

        if state == 'NUMBER' or state == 'FLOAT':
            calulator.add(element)

        elif state == 'OPERATION':
            calulator.use_opertation(operation=element)

        else:
            raise 'Не известный тип токена'

    if len(calulator.get()) > 1:
        raise 'Невозможно посчитать введённый пример ( введено не достаточно знаков операций )'

    else:
        return calulator.get()[0]




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
        input_data: str = input()

        if input_data.lower() == 'break':
            print('Выполнение кода прекращено.')

            break

        print(calculate_now(input_data=input_data))



if __name__ == '__main__':
    main()