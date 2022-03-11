import os


def file_op(path):
    file_list = os.listdir(path)

    for file in file_list:
        # 获得绝对路径
        cur_path = os.path.join(path, file)

        if os.path.isdir(cur_path):
            print(f"{cur_path} is a dir")
            file_op(cur_path)

        elif file[-4:] == '.gif':
            os.remove(file)
            print(f"remove file:{file}")
    return


if __name__ == '__main__':
    file_op('C:/Users/David/Documents/WeChat Files/wxid_0bfgek6dtqjn22/FileStorage/File/')
