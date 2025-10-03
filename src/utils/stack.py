class Stack:

    def __init__(self) -> None:
        self.stack = []


    def __len__(self) -> int:
        '''
        Функция возвращает длинну стэка

        :return: Длинна стэка
        '''

        return len(self.stack)


    def is_empty(self) -> bool:
        '''
        Функция показывает есть ли какие то значения внутри стэка

        :return: истинна или ложь, то что стэк пуст
        '''

        if self.__len__() == 0:
            return True

        else:
            return False


    def add(self, element: float | int) -> None:
        '''
        Функция добавляет число в конец стэка

        :param element: число ( токен )
        :return: ничего
        '''

        self.stack.append(element)


    def pop(self) -> None:
        '''
        Функция удаляет два последних элемента стэка

        :return: ничего
        '''

        for _ in range(2):
            self.stack.pop()


    def can_use_operation(self) -> bool:
        '''
        Проверяет есть ли два элемента внутри стэка

        :return: истинно ли то что в стэка достаточно элементов для вычисления операции
        '''

        if self.__len__() >= 2:
            return True

        else:
            return False


    def get(self) -> list:
        '''
        Функция возвращает весь стэк

        :return: стэк
        '''

        return self.stack