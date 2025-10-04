def get_format(state: str, current_token: str) -> int | float | str:
    '''
    Функция преобразует токен в типе str в необходимый для счета тип

    :param state: тип токена (OPERATION | NUMBER | FLOAT)
    :param current_token: токен
    :return: возвращает преобразованный в нужный тип токен
    '''


    if state == 'NUMBER':
        return int(current_token)

    elif state == 'FLOAT':
        return float(current_token)

    else:
        return current_token