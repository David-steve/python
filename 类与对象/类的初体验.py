class Washer:
    def washer(self):
        print('洗衣服')

    def __init__(self, height, width):  # 类构造函数
        self.height = height
        self.width = width

    def __str__(self):
        return '这是洗衣机的说明书'


if __name__ == '__main__':
    haier1 = Washer(1001, 500)
    print(haier1)               # 当没有定义__str__方法时，默认打印对象的地址，否则打印__str__返回的数据
    haier1.washer()
    print(f'{haier1.height},{haier1.width} ')
