

class InvalidDataException(Exception):
    def __init__(self, massage):
        self.massage = massage


class ProcessingException(Exception):
    def __init__(self, massage):
        self.massage = massage


def generate_exception (a , b):
    if a == 1:
        raise InvalidDataException('вы ввели вообще не то')

    if b == 0:
        raise ProcessingException('вы не понимаете что надо делать')

def cal_exception ():
    try:
        print(generate_exception(a=0, b=0))
    except InvalidDataException as exept_1:
        print(f"Сообщение об ошибки {exept_1.massage}")
    except ProcessingException as exept_2:
        print(f"Сообщение об ошибки {exept_2.massage}")

cal_exception()












