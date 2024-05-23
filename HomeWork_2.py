
class InvalidDataException(Exception):
    def __init__(self, massage):
        self.massage = massage


class ProcessingException(Exception):
    def __init__(self, massage):
        self.massage = massage


def generate_exception (a , b):
    if a == 2:
        raise InvalidDataException('вы ввели вообще не то')

    if b == 1:
        raise ProcessingException('вы не понимаете что надо делать')


try:
    print(generate_exception(a=1, b=1))
except InvalidDataException as exept_1:
    print(f"Сообщение об ошибки {exept_1.massage}")
except ProcessingException as exept_2:
    print(f"Сообщение об ошибки {exept_2.massage}")






