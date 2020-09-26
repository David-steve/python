

def func(a):
    return a % 2 == 0


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    result = filter(func, list1)    # 过滤器，过滤掉不符合条件的数据

    print(result)                   # result 为一个地址
    print(list(result))             # 转换为列表
    print(list1)
