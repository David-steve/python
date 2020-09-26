
def get_name():
    file_name = input('请输入要备份的文件')
    print(file_name)

    return file_name


# 备份文件
def backup(file_name):
    index = file_name.rfind('.')
    if index <= 0:
        exit(-1)

    new_name = file_name[:index] + '[备份]' + file_name[index:]
    print(new_name)

    old_file = open(file_name, 'rb')
    new_file = open(new_name, 'wb')

    # content = old_file.read()
    # 当不确定文件大小时，应循环读取写入
    for line in old_file:
        new_file.write(line)

    old_file.close()
    new_file.close()


if __name__ == '__main__':
    backup(get_name())
