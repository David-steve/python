import functools


def func(a, b):
    return a+b


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    result = functools.reduce(func, list1)    # 对列表的数据进行累加
    print(result)
