

class IncorrectPlacementOfBrackets(Exception):
    def __init__(self) -> None:
        self.error_msg = "Не верно расставлены скобки."
        super().__init__(self.error_msg)


class IncorrectOperationsCount(Exception):
    def __init__(self) -> None:
        self.error_msg = "Не верно введён пример, невозможно посчитать, количество чисел не удовлетворяет количеству действий."
        super().__init__(self.error_msg)