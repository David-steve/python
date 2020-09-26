class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}')


class Apprentice(Master):
    pass


if __name__ == '__main__':
    sun = Apprentice()
    sun.make_cake()
