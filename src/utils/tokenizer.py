from src.utils.components.format_component import get_format


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

                if char == '~' or char == '$':
                    current_token = char.replace('~', '-', 1).replace('$', '', 1)

                else:
                    current_token = char

            elif char in ['+', '-', '*', '/', '%']:
                state = 'OPERATION'
                current_token = char

            elif char == '(':
                state = 'OPEN_BRACKET'
                current_token = char

            elif char == ')':
                state = 'CLOSE_BRACKET'
                current_token = char

        elif state == 'NUMBER':
            if char.isdigit():
                current_token += char

            elif char == '.':
                state = 'FLOAT'

                current_token += char

            else:
                state = 'START'


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