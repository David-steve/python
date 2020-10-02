import multiprocessing
import os
import time
import django


def dance():
    print('dance PID：', os.getpid())            # 获取当前进程的PID
    print('dance PPID：', os.getppid())          # 获取父进程的PID
    print(multiprocessing.current_process())     # 获取当前进程信息

    for i in range(3):
        print('dancing')
        time.sleep(1)


def sing():
    print('sing PID：', os.getpid())
    print('sing PPID：', os.getppid())
    print(multiprocessing.current_process())

    for i in range(3):
        print('singing')
        time.sleep(1)


if __name__ == '__main__':
    # 创建子进程
    dance_process = multiprocessing.Process(target=dance, name='dance_process')
    dance_process.start()       # 启动子进程

    sing_process = multiprocessing.Process(target=sing, name="sing_process")
    sing_process.start()

    sing()  # 父进程
