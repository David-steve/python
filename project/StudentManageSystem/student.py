class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'


def test_a():
    print("test_a")
    pass
