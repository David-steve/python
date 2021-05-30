import os


def print_author_info():
    print("This is a small tool which in order to help rename your files with \n"
          "just a click, any confusion contact me with no hesitate")
    print("author:  David")
    print("email:   David@163.com\n")


if __name__ == '__main__':
    # os.mkdir('test_dir')              # 创建文件夹
    # os.rmdir('test_dir')              # 删除文件夹
    print_author_info()

    while(True):
        dir = input("\n请输入路径:")
        os.chdir(dir)
        print(os.getcwd())                  # 打印当前工作路径
        print(os.listdir())                 # 列出当前目录的所有文件，返回的是一个列表

        # 重命名文件或文件夹
        # os.rename('demo1[备份].py', 'demo1重命名.py')
        del_name = input("请输入要替换的字符：")
        replace_name = input("请输入要新的字符：")

        for name in os.listdir():
            new_name = name.replace(del_name, replace_name)     # 替换字符
            os.rename(name, new_name)                           # 重命名文件
            print(new_name)

        str = input('\n would you wanna continue? Y|yes, N|no\n')
        if(str == 'N'):
            break
        
    os.system("pause")
