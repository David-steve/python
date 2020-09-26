def add_num(a, b):
    return abs(a) + abs(b)


def func(x):
    return x ** 2


if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    print(add_num(6, -5))
    print(round(1.50))

    result = map(func, list1)   #调用func，传入list1，返回一个迭代器
    print(result)
    print(list(result))
