from src.utils.exceptions import IncorrectOperationsCount
from src.utils.stack import Stack


class Calculator(Stack):

    def use_operation(self, operation: str) -> None:
        '''
        Функция производит переданную операция с последними двумя числами стека и кладет обратно полученное значение

        :param operation: Используемый оператор
        :return:
        '''

        if not(self.can_use_operation()):
            if operation != '~':
                raise IncorrectOperationsCount()

            else:
                digit = self.stack[-1]

                self.stack.pop()

                answer = -digit

        else:
            first_digit = self.stack[-2]
            second_digit = self.stack[-1]

            self.pop()

            match operation:
                case '+':
                    answer = first_digit + second_digit

                case '-':
                    answer = first_digit - second_digit

                case '*':
                    answer = first_digit * second_digit

                case '**':
                    answer = first_digit ** second_digit

                case '/':
                    if second_digit != 0:
                        answer = first_digit / second_digit

                    else:
                        raise ZeroDivisionError("Делить на ноль нельзя.")


                case '//':
                    if type(first_digit) == float or type(second_digit) == float:
                        raise TypeError("Целочисленное деление доступно только для целых чисел.")

                    elif second_digit == 0:
                        raise ZeroDivisionError("Делить на ноль нельзя.")

                    else:
                        answer = first_digit // second_digit

                case '%':
                    if type(first_digit) == float or type(second_digit) == float:
                        raise TypeError("Деление с остатком доступно только для целых чисел.")

                    elif second_digit == 0:
                        raise ZeroDivisionError("Делить на ноль нельзя.")

                    else:
                        answer = first_digit % second_digit

                case '~':
                    raise SyntaxError('Не верно использован унарный минус')

                case '$':
                    raise SyntaxError('Не верно использован унарный плюс')

                case _:
                    raise SyntaxError('Не известная операция')

        self.stack.append(answer)