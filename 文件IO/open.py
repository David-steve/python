if __name__ == '__main__':
    f = open("client.c", 'r+')
    # f = open("client.c")          # 如果省略访问模式，则默认访问模式为只读
    # content = f.readlines()       # 读取文件全部内容，以列表的形式返回，每一行为一个元素
    # print(content)

    print(f.readline())             # 读取一行

    # print(f.read())               # 不填数量代表读取文件的全部内容

    # print(f.read(100))            # 读取100个字
    f.close()
