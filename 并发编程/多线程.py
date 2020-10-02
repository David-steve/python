import threading
import time

# 主线程会等待所有的子线程结束后再退出


def dance():
    for i in range(10):
        print('dance', i)
        time.sleep(0.2)


def sing():
    for i in range(10):
        print('sing', i)
        time.sleep(0.2)


def greep(name):
    print('hello ', name)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)     # 创建线程
    dance_thread = threading.Thread(target=dance)
    # 以元组的形式传递参数
    hello_thread1 = threading.Thread(target=greep, args=('David1',))
    # 以字典的形式传递参数
    hello_thread2 = threading.Thread(target=greep, kwargs={'name': 'David2'})

    # 启动线程
    sing_thread.start()
    dance_thread.start()
    hello_thread1.start()
    hello_thread2.start()
