class Writeexcept(Exception):
    clsnumber = 0

    def __init__(self):
        self.number = self.clsnumber
        self.raise_clsnumber()

    @classmethod
    def raise_clsnumber(cls):
        cls.clsnumber += 1

    def __str__(self):
        print(
            f"номер данной ошибки {self.number}, общее количество таких ошибок {self.clsnumber}"
        )


class number:
    def __init__(self, x, y):
        self.check_x(x)
        self.check_x(y)
        self.x = x
        self.y = y

    @classmethod
    def check_x(cls, x):
        if type(x) != int:
            raise Writeexcept


z = number(1, "s")
