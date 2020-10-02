import threading

g_num = 0
lock = threading.Lock()


def task1():
    for i in range(10000):
        # 上锁
        lock.acquire()

        global g_num
        g_num += 1

        # 释放锁
        lock.release()

        print('task1')


def task2():
    for i in range(10000):
        # 上锁
        lock.acquire()

        global g_num
        g_num += 1

        # 释放锁
        lock.release()

        print('task2', g_num)


if __name__ == '__main__':
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread1.start()
    thread2.start()
