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

    i = 0 # enumerate не подошел потому что мне нужно отконтролить индекс когда я пишу // или **

    while i < len(expr):
        char = expr[i]

        if char.isspace():
            if current_token:
                tokens.append((state, get_format(state, current_token)))
                current_token = ''

            state = 'START'

            i += 1

            continue

        if state == 'START':
            if char.isdigit() or char in ['~', '$']:
                state = 'NUMBER'

                current_token = char.replace('~', '-', 1).replace('$', '', 1)

            elif char in ['+', '-', '*', '/', '%']:
                if i + 1 < len(expr) and expr[i + 1] == char and char in ['*', '/']: # Проверяем двойные операции ** и //
                    current_token = char * 2

                    i += 1  # Скипаем второй символ (бо он нам не нужен тут)

                else:
                    current_token = char

                tokens.append(('OPERATION', current_token))

                state = 'START'
                current_token = ''

            elif char == '(':
                tokens.append(('OPEN_BRACKET', char))

            elif char == ')':
                tokens.append(('CLOSE_BRACKET', char))

            else:
                raise ValueError(f"Неизвестный символ: {char}")

        elif state == 'NUMBER':
            if char.isdigit():
                current_token += char

            elif char == '.':
                if '.' in current_token:
                    raise ValueError("Некорректное число: две точки подряд")

                state = 'FLOAT'
                current_token += char

            else:
                tokens.append((state, get_format(state, current_token)))

                current_token = ''
                state = 'START'

                continue

        elif state == 'FLOAT':
            if char.isdigit():
                current_token += char

            else:
                tokens.append((state, get_format(state, current_token)))

                current_token = ''
                state = 'START'

                continue

        i += 1

    if current_token:
        tokens.append((state, get_format(state, current_token)))

    return tokens