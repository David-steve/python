import os


if __name__ == '__main__':
    # os.mkdir('test_dir')              # 创建文件夹
    # os.rmdir('test_dir')              # 删除文件夹
    print(os.getcwd())                  # 打印当前工作路径
    os.chdir('../')                     # 改变工作路径
    print(os.getcwd())
    print(os.listdir())                 # 列出当前目录的所有文件，返回的是一个列表
    # 重命名文件或文件夹
    # os.rename('demo1[备份].py', 'demo1重命名.py')
    print(os.listdir())
