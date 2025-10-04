from src.utils.stack import Stack


class Calculator(Stack):

    def use_operation(self, operation: str) -> None:
        '''
        Функция производит переданную операция с последними двумя числами стека и кладет обратно полученное значение

        :param operation: Используемый оператор
        :return:
        '''

        if not(self.can_use_operation()):
            if operation != '-':
                raise TypeError('Не верно введён пример, невозможно посчитать, количество чисел не удовлетворяет количеству действий')

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
                        raise "Деление с остатком доступно только для целых чисел."

                    elif second_digit == 0:
                        raise "Делить на ноль нельзя."

                    else:
                        answer = first_digit % second_digit

                case _:
                    raise SyntaxError('Не известная операция')

        self.stack.append(answer)